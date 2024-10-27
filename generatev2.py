import os
import random
import string
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

def generate_private_key():
    # Generate a random 256-bit number (32 bytes)
    private_key = ''.join(random.choice('0123456789ABCDEF') for _ in range(64))
    return private_key

def save_private_keys_to_file(private_keys, file_name):
    with open(file_name, 'w') as file:
        for key in private_keys:
            file.write(f"{key}\n")

def main():
    simulate_hacking_text("Software Name: Private Key Generator")
    simulate_hacking_text("Software Developed By: Pikai")
    simulate_hacking_text("Software Version: 1.0.0")
    simulate_hacking_text("Description: This software generates random private keys suitable for Bitcoin wallets.")
    
    input(Fore.GREEN + "\nPress Enter to Proceed" + Style.RESET_ALL)
    
    simulate_hacking_text("Warning: Please use these private keys responsibly. Accessing others' wallets without permission is illegal.")
    
    while True:
        try:
            num_keys = int(input(Fore.RED + "\nHow many private keys do you want to generate (1-10000): " + Style.RESET_ALL))
            if 1 <= num_keys <= 10000:
                break
            else:
                print(Fore.RED + "Please enter a number between 1 and 10000." + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + "Please enter a valid number." + Style.RESET_ALL)

    simulate_hacking_text("\nGenerating Random Private Keys...")
    time.sleep(1)

    private_keys = [generate_private_key() for _ in range(num_keys)]

    for key in private_keys:
        simulate_hacking_text(key)
        time.sleep(0.001)

    simulate_hacking_text("\nPrivate keys generated successfully.")
    time.sleep(1)

    while True:
        file_name = input(Fore.RED + "\nEnter a file name with '.txt' to save the private keys: " + Style.RESET_ALL)
        if file_name.endswith('.txt'):
            break
        else:
            print(Fore.RED + "Please enter a valid file name ending with '.txt'." + Style.RESET_ALL)

    save_private_keys_to_file(private_keys, file_name)

    simulate_hacking_text(f"\nPrivate keys have been saved to {file_name}")
    time.sleep(1)

if __name__ == "__main__":
    main()
