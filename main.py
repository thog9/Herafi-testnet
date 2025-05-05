import os
import sys
import asyncio
from colorama import init, Fore, Style
import inquirer

# Initialize colorama
init(autoreset=True)

# Fixed border width
BORDER_WIDTH = 80

# Display border function
def print_border(text: str, color=Fore.CYAN, width=BORDER_WIDTH):
    text = text.strip()
    if len(text) > width - 4:
        text = text[:width - 7] + "..."
    padded_text = f" {text} ".center(width - 2)
    print(f"{color}┌{'─' * (width - 2)}┐{Style.RESET_ALL}")
    print(f"{color}│{padded_text}│{Style.RESET_ALL}")
    print(f"{color}└{'─' * (width - 2)}┘{Style.RESET_ALL}")

# Display banner
def _banner():
    banner = r"""


██╗░░██╗███████╗██████╗░░█████╗░███████╗██╗  ██████╗░██████╗░░█████╗░████████╗░█████╗░░█████╗░░█████╗░██╗░░░░░
██║░░██║██╔════╝██╔══██╗██╔══██╗██╔════╝██║  ██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██║░░░░░
███████║█████╗░░██████╔╝███████║█████╗░░██║  ██████╔╝██████╔╝██║░░██║░░░██║░░░██║░░██║██║░░╚═╝██║░░██║██║░░░░░
██╔══██║██╔══╝░░██╔══██╗██╔══██║██╔══╝░░██║  ██╔═══╝░██╔══██╗██║░░██║░░░██║░░░██║░░██║██║░░██╗██║░░██║██║░░░░░
██║░░██║███████╗██║░░██║██║░░██║██║░░░░░██║  ██║░░░░░██║░░██║╚█████╔╝░░░██║░░░╚█████╔╝╚█████╔╝╚█████╔╝███████╗
╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝  ╚═╝░░░░░╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░░╚════╝░░╚════╝░░╚════╝░╚══════╝


    """
    print(f"{Fore.GREEN}{banner:^80}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}{'═' * BORDER_WIDTH}{Style.RESET_ALL}")
    print_border("HERAFI PROTOCOL TESTNET", Fore.GREEN)
    print(f"{Fore.YELLOW}│ {'Contact'}: {Fore.CYAN}https://t.me/thog099{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}│ {'Replit'}: {Fore.CYAN}Thog{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}│ {'Telegram Channel'}: {Fore.CYAN}https://t.me/thogairdrops{Style.RESET_ALL}")
    print(f"{Fore.GREEN}{'═' * BORDER_WIDTH}{Style.RESET_ALL}")

# Clear screen
def _clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Script functions
async def run_faucet(language: str):
    from scripts.faucet import run_faucet
    await run_faucet(language)

async def run_faucetmax(language: str):
    from scripts.faucetmax import run_faucetmax
    await run_faucetmax(language)

async def run_swap(language: str):
    from scripts.swap import run_swap
    await run_swap(language)

async def run_vault(language: str):
    from scripts.vault import run_vault
    await run_vault(language)

async def run_liquidity(language: str):
    from scripts.liquidity import run_liquidity
    await run_liquidity(language)

async def cmd_exit(language: str):
    messages = {"vi": "Đang thoát...", "en": "Exiting..."}
    print_border(messages[language], Fore.GREEN)
    sys.exit(0)

# Script map
SCRIPT_MAP = {
    "faucet": run_faucet,
    "faucetmax": run_faucetmax,
    "swap": run_swap,
    "vault": run_vault,
    "liquidity": run_liquidity,
    "exit": cmd_exit
}

# Available scripts by language
def get_available_scripts(language):
    scripts = {
        'vi': [
            {"name": "1. Nhận token từ faucet [WETH, CRV, SUSHI, UNI, USDC] │ Optimism Sepolia", "value": "faucet"},
            {"name": "2. Nhận tối đa token từ faucet [WETH, CRV, SUSHI, UNI, USDC, wBTC] │ Optimism Sepolia", "value": "faucetmax"},
            {"name": "3. Swap token [hDEFI ↔ WETH, CRV, SUSHI, UNI, USDC] │ Optimism Sepolia", "value": "swap"},
            {"name": "4. Issue/Redeem token qua Vault │ Optimism Sepolia", "value": "vault"},
            {"name": "5. Cung cấp/Rút thanh khoản │ Optimism Sepolia", "value": "liquidity"},
            {"name": "6. Thoát", "value": "exit"},
        ],
        'en': [
            {"name": "1. Claim faucet tokens [WETH, CRV, SUSHI, UNI, USDC] │ Optimism Sepolia", "value": "faucet"},
            {"name": "2. Claim max faucet tokens [WETH, CRV, SUSHI, UNI, USDC, wBTC] │ Optimism Sepolia", "value": "faucetmax"},
            {"name": "3. Swap tokens [hDEFI ↔ WETH, CRV, SUSHI, UNI, USDC] │ Optimism Sepolia", "value": "swap"},
            {"name": "4. Issue/Redeem tokens via Vault │ Optimism Sepolia", "value": "vault"},
            {"name": "5. Provide/Remove liquidity │ Optimism Sepolia", "value": "liquidity"},
            {"name": "6. Exit", "value": "exit"},
        ]
    }
    return scripts[language]

def run_script(script_func, language):
    if asyncio.iscoroutinefunction(script_func):
        asyncio.run(script_func(language))
    else:
        script_func(language)

def select_language():
    while True:
        _clear()
        _banner()
        print(f"{Fore.GREEN}{'═' * BORDER_WIDTH}{Style.RESET_ALL}")
        print_border("CHỌN NGÔN NGỮ / SELECT LANGUAGE", Fore.YELLOW)
        questions = [
            inquirer.List('language',
                          message=f"{Fore.CYAN}Vui lòng chọn / Please select:{Style.RESET_ALL}",
                          choices=[("1. Tiếng Việt", 'vi'), ("2. English", 'en')],
                          carousel=True)
        ]
        answer = inquirer.prompt(questions)
        if answer and answer['language'] in ['vi', 'en']:
            return answer['language']
        print(f"{Fore.RED}❌ {'Lựa chọn không hợp lệ / Invalid choice':^76}{Style.RESET_ALL}")

def main():
    _clear()
    _banner()
    language = select_language()

    messages = {
        "vi": {
            "running": "Đang thực thi: {}",
            "completed": "Đã hoàn thành: {}",
            "error": "Lỗi: {}",
            "press_enter": "Nhấn Enter để tiếp tục...",
            "menu_title": "MENU CHÍNH",
            "select_script": "Chọn script để chạy"
        },
        "en": {
            "running": "Running: {}",
            "completed": "Completed: {}",
            "error": "Error: {}",
            "press_enter": "Press Enter to continue...",
            "menu_title": "MAIN MENU",
            "select_script": "Select script to run"
        }
    }

    while True:
        _clear()
        _banner()
        print(f"{Fore.YELLOW}{'═' * BORDER_WIDTH}{Style.RESET_ALL}")
        print_border(messages[language]["menu_title"], Fore.YELLOW)
        print(f"{Fore.CYAN}│ {messages[language]['select_script'].center(BORDER_WIDTH - 4)} │{Style.RESET_ALL}")

        available_scripts = get_available_scripts(language)
        questions = [
            inquirer.List('script',
                          message=f"{Fore.CYAN}{messages[language]['select_script']}{Style.RESET_ALL}",
                          choices=[script["name"] for script in available_scripts],
                          carousel=True)
        ]
        answers = inquirer.prompt(questions)
        if not answers:
            continue

        selected_script_name = answers['script']
        selected_script_value = next(script["value"] for script in available_scripts if script["name"] == selected_script_name)

        script_func = SCRIPT_MAP.get(selected_script_value)
        if script_func is None:
            print(f"{Fore.RED}{'═' * BORDER_WIDTH}{Style.RESET_ALL}")
            print_border(f"{'Chưa triển khai / Not implemented'}: {selected_script_name}", Fore.RED)
            input(f"{Fore.YELLOW}⏎ {messages[language]['press_enter']}{Style.RESET_ALL:^76}")
            continue

        try:
            print(f"{Fore.CYAN}{'═' * BORDER_WIDTH}{Style.RESET_ALL}")
            print_border(messages[language]["running"].format(selected_script_name), Fore.CYAN)
            run_script(script_func, language)
            print(f"{Fore.GREEN}{'═' * BORDER_WIDTH}{Style.RESET_ALL}")
            print_border(messages[language]["completed"].format(selected_script_name), Fore.GREEN)
            input(f"{Fore.YELLOW}⏎ {messages[language]['press_enter']}{Style.RESET_ALL:^76}")
        except Exception as e:
            print(f"{Fore.RED}{'═' * BORDER_WIDTH}{Style.RESET_ALL}")
            print_border(messages[language]["error"].format(str(e)), Fore.RED)
            input(f"{Fore.YELLOW}⏎ {messages[language]['press_enter']}{Style.RESET_ALL:^76}")

if __name__ == "__main__":
    main()
