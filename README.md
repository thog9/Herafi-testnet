# Herafi Testnet Scripts

This repository contains a collection of Python scripts designed to interact with the **Herafi Testnet**, a high-performance blockchain test network. The main script, main.py, serves as a user-friendly command-line interface (CLI) to execute various operations on the Herafi Testnet, such as claiming faucet tokens, swapping tokens, managing vaults, and providing/removing liquidity. Built with web3.py, the scripts support asynchronous execution and offer bilingual output (English and Vietnamese) for enhanced user interaction.

Faucet: [Herafi Testnet Faucet](https://testnet.herafi.xyz/faucet)

## Features Overview

### General Features

- **Multi-Account Support**: Reads private keys from `pvkey.txt` to perform actions across multiple accounts.
- **Colorful CLI**: Uses `colorama` for visually appealing output with colored text and borders.
- **Asynchronous Execution**: Built with `asyncio` for efficient blockchain interactions.
- **Error Handling**: Comprehensive error catching for blockchain transactions and RPC issues.
- **Bilingual Support**: Supports both English and Vietnamese output based on user selection.

### Included Scripts

1. **Faucet**: Claims tokens (WETH, CRV, SUSHI, UNI, USDC) from the faucet.
2. **Faucet Max**: Claims maximum available tokens (WETH, CRV, SUSHI, UNI, USDC, wBTC) from the faucet.
3. **Swap**: Swaps tokens between hDEFI and other tokens (WETH, CRV, SUSHI, UNI, USDC).
4. **Vault**: Issues or redeems tokens via a vault contract.
5. **Liquidity**: Provides and removes liquidity for token pools.

## Prerequisites

Before running the scripts, ensure you have the following installed:

- Python 3.8+
- `pip` (Python package manager)
- **Dependencies**: Install via `pip install -r requirements.txt` (ensure `web3.py`, `colorama`, `asyncio`, `eth-account`, `aiohttp_socks` and `inquirer` are included).
- **pvkey.txt**: Add private keys (one per line) for wallet automation.
- Access to the Herafi Testnet RPC (e.g., https://sepolia.optimism.io).
- **proxies.txt** (optional): Add proxy addresses for network requests, if needed.

## Installation

1. **Clone this repository:**
- Open cmd or Shell, then run the command:
```sh
git clone https://github.com/thog9/Herafi-testnet.git
```
```sh
cd Herafi-testnet
```
2. **Install Dependencies:**
- Open cmd or Shell, then run the command:
```sh
pip install -r requirements.txt
```
3. **Prepare Input Files:**
- Open the `pvkey.txt`: Add your private keys (one per line) in the root directory.
```sh
nano pvkey.txt 
```
```sh
nano proxies.txt
```
4. **Run:**
- Open cmd or Shell, then run command:
```sh
python main.py
```
- Choose a language (Vietnamese/English).

## Contact

- **Telegram**: [thog099](https://t.me/thog099)
- **Channel**: [CHANNEL](https://t.me/thogairdrops)
- **Group**: [GROUP CHAT](https://t.me/thogchats)
- **X**: [Thog](https://x.com/thog099) 
