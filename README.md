# Bitcoin Wallet Bruteforcer

This Python script is a Bitcoin wallet bruteforcer that generates and checks mnemonic seeds to find a specific Bitcoin address. It utilizes BIP39 mnemonic generation and BIP44 address derivation to efficiently search for the target address. The script can be run with multiple instances to speed up the search process.

| **Feature**                          | **Previous Version**                                                                                     | **Updated Version**                                                                                          |
|--------------------------------------|----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| **Address Type Handling**            | The script only handled the default Bitcoin address type.                                                  | Added support for multiple address types: "legacy", "p2sh", and "segwit".                                  |
| **Result File Name**                 | The results were written to `"wallets_with_balance.txt" file.                                              | Changed to `"wallets_with_balance_found.txt"`.                                                              |
| **Error Handling for Balance Check** | Basic error handling for checking balances.                                                                | Improved error handling using `requests.RequestException` and specific retry logic for balance checking.    |
| **Address Matching**                 | The script only checked for a specific target address.                                                    | Now supports matching against a list of target addresses loaded from a file or URL.                          |
| **Multithreading and Queue**         | Single process bruteforce.                                                                                 | Introduced `Queue` for communication between processes and added a separate process for handling results.   |
| **URL Support for Target Addresses** | Target addresses were manually entered or loaded from a file.                                             | Added the option to automatically load rich Bitcoin addresses from a URL (using `-u` flag).                  |
| **Command-Line Arguments**           | Only basic arguments for target address and number of instances.                                          | Enhanced with more options, including address type (`legacy`, `p2sh`, `segwit`, `all`) and file/URL input.    |
| **Window Title Update**              | Updated window title with the number of seeds attempted.                                                  | No changes to the window title feature.                                                                      |
| **Address Generation Logic**         | Generates addresses only in the default (legacy) format.                                                   | Can now generate addresses in "legacy", "p2sh", or "segwit" formats, depending on user choice.              |
| **Logging Improvements**             | Standard logging to console and file.                                                                      | Enhanced logging with more detailed error messages and improved clarity in logging output.                    |

```
usage: btc.py [-h] [-f FILE] [-u] -i INSTANCES [-t {legacy,p2sh,segwit,all}]

Bitcoin Wallet Bruteforcer

options:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  File containing Bitcoin addresses
  -u, --url             Automatically use URL for rich Bitcoin addresses
  -i INSTANCES, --instances INSTANCES
                        Number of instances to run
  -t {legacy,p2sh,segwit,all}, --type {legacy,p2sh,segwit,all}
                        Type of Bitcoin address
```


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
## Usage (old)
```
python bitcoin_wallet_bruteforcer.py -a <target_address> -i <num_instances>

- `<target_address>`: The Bitcoin address you want to find.
- `<num_instances>`: Number of instances to run in parallel for faster search.
```
