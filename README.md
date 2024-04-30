# Bitcoin Wallet Bruteforcer

This Python script is a Bitcoin wallet bruteforcer that generates and checks mnemonic seeds to find a specific Bitcoin address. It utilizes BIP39 mnemonic generation and BIP44 address derivation to efficiently search for the target address. The script can be run with multiple instances to speed up the search process.

## Requirements

- Python 3.x
- bip-utils
- requests
- dotenv

## Installation

1. Clone the repository:
```
git clone https://github.com/Cr0mb/BreadBruteForce.git
```
2. Install dependencies:
```
pip install bip-utils requests python-dotenv
```
- if issues installing bip-utils or dotenv:
   - download notenv
    ```
    git clone https://github.com/theskumar/python-dotenv.git
    ```
   - install
    ```
    pip install .
    ```
   - download bip-utils
    ```
    git clone https://github.com/ebellocchia/bip_utils.git
    ```
  - install
    ```
    pip install .
    ```
## Usage
```
python bitcoin_wallet_bruteforcer.py -a <target_address> -i <num_instances>

- `<target_address>`: The Bitcoin address you want to find.
- `<num_instances>`: Number of instances to run in parallel for faster search.
```
