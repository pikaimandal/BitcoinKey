import requests
import time
import colorama
from colorama import Fore, Style

# Initialize colorama
colorama.init()

def simulate_hacking_text(text, delay=0.03):
    for char in text:
        print(Fore.RED + char, end='', flush=True)
        time.sleep(delay)
    print(Style.RESET_ALL)

def check_balance(address):
    try:
        url = f"https://blockchain.info/balance?active={address}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            balance = data[address]['final_balance'] / 100000000  # Convert from satoshi to BTC
            return balance
        else:
            return None
    except Exception as e:
        print(Fore.RED + f"Error checking balance for address {address}: {str(e)}" + Style.RESET_ALL)
        return None

def check_wallet_balances(file_path):
    with open(file_path, 'r') as file:
        addresses = [line.strip() for line in file.readlines()]
    
    simulate_hacking_text("Checking Wallet Balances...\n", delay=0.01)
    time.sleep(1)
    
    valid_balances = []
    for line_number, address in enumerate(addresses, start=1):
        balance = check_balance(address)
        if balance is not None:
            if balance > 0:
                print(Fore.RED + f"{address} ({balance} BTC)" + Style.RESET_ALL)
                valid_balances.append(f"{address} ({balance} BTC)")
            else:
                print(Fore.GREEN + f"{address} (0 BTC)" + Style.RESET_ALL)
        else:
            print(Fore.RED + f"Invalid address at line {line_number}: {address}" + Style.RESET_ALL)
        
        time.sleep(0.2)  # Rate limit sleep

    simulate_hacking_text("Balance check complete.", delay=0.01)

    if valid_balances:
        file_name = input(Fore.GREEN + "\nEnter a file name with '.txt' to save the addresses and balances: " + Style.RESET_ALL)
        if not file_name.endswith('.txt'):
            file_name += '.txt'
        
        with open(file_name, 'w') as file:
            file.write("\n".join(valid_balances))
        
        simulate_hacking_text(f"\nAddresses and balances have been saved to {file_name}", delay=0.01)

if __name__ == "__main__":
    simulate_hacking_text("Software Name: Wallet Balance Checker")
    simulate_hacking_text("Software Developed By: Pikai")
    simulate_hacking_text("Software Version: 1.0.0")
    simulate_hacking_text("Description: This software checks the balances of Bitcoin addresses via Blockchain.info API.")
    
    input(Fore.GREEN + "\nPress Enter to Proceed" + Style.RESET_ALL)
    
    file_path = input(Fore.RED + "Enter the path to the TXT file containing Bitcoin addresses: " + Style.RESET_ALL)
    check_wallet_balances(file_path)
