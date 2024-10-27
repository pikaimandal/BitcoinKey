import os
import random
import string
import time
import colorama
from colorama import Fore, Style

# Initialize colorama
colorama.init()

def simulate_hacking_text(text):
    print(Fore.RED + text + Style.RESET_ALL)

def generate_private_key():
    # Generate a random 256-bit number (32 bytes)
    private_key = ''.join(random.choices('0123456789ABCDEF', k=64))
    return private_key

def save_private_keys_to_file(private_keys, file_name):
    with open(file_name, 'w') as file:
        file.write("\n".join(private_keys))

def main():
    simulate_hacking_text("Software Name: Private Key Generator")
    simulate_hacking_text("Software Developed By: Pikai")
    simulate_hacking_text("Software Version: 1.0.0")
    simulate_hacking_text("Description: This software generates random private keys suitable for Bitcoin wallets.")
    
    input(Fore.GREEN + "\nPress Enter to Proceed" + Style.RESET_ALL)
    
    simulate_hacking_text("Warning: Please use these private keys responsibly. Accessing others' wallets without permission is illegal.")
    
    while True:
        try:
            num_keys = int(input(Fore.GREEN + "\nHow many private keys do you want to generate (1-10000): " + Style.RESET_ALL))
            if 1 <= num_keys <= 10000:
                break
            else:
                print(Fore.GREEN + "Please enter a number between 1 and 10000." + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + "Please enter a valid number." + Style.RESET_ALL)

    simulate_hacking_text("\nGenerating Random Private Keys...")
    time.sleep(1)

    private_keys = [generate_private_key() for _ in range(num_keys)]

    simulate_hacking_text("Private keys successfully generated in the background.")
    time.sleep(1)

    while True:
        file_name = input(Fore.GREEN + "\nEnter a file name with '.txt' to save the generated private keys: " + Style.RESET_ALL)
        if file_name.endswith('.txt'):
            break
        else:
            print(Fore.GREEN + "Please enter a valid file name ending with '.txt'." + Style.RESET_ALL)

    save_private_keys_to_file(private_keys, file_name)

    simulate_hacking_text(f"\nPrivate keys have been saved to you folder as {file_name}")
    time.sleep(1)

if __name__ == "__main__":
    main()
