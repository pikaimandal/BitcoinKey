import hashlib
import ecdsa
import base58
import colorama
from colorama import Fore, Style
import time
import os
import random
import itertools

# Initialize colorama
colorama.init()

def simulate_hacking_text(text, delay=0.03):
    for char in text:
        print(Fore.RED + char, end='', flush=True)
        time.sleep(delay)
    print(Style.RESET_ALL)

def generate_private_key():
    return os.urandom(32).hex()

def private_key_to_public_key(private_key):
    private_key_bytes = bytes.fromhex(private_key)
    sk = ecdsa.SigningKey.from_string(private_key_bytes, curve=ecdsa.SECP256k1)
    vk = sk.verifying_key
    public_key = b'\x04' + vk.to_string()
    return public_key.hex()

def public_key_to_address(public_key):
    public_key_bytes = bytes.fromhex(public_key)
    sha256_bpk = hashlib.sha256(public_key_bytes).digest()
    ripemd160_bpk = hashlib.new('ripemd160', sha256_bpk).digest()
    pre_address = b'\x00' + ripemd160_bpk
    checksum = hashlib.sha256(hashlib.sha256(pre_address).digest()).digest()[:4]
    address = base58.b58encode(pre_address + checksum)
    return address.decode()

def brute_force_address(target_address):
    attempts = 0
    spinner = itertools.cycle(['-', '\\', '|', '/'])
    while True:
        attempts += 1
        private_key = generate_private_key()
        public_key = private_key_to_public_key(private_key)
        address = public_key_to_address(public_key)
        if address == target_address:
            return private_key, attempts
        if attempts % 1000 == 0:  # Update the animation every 1000 attempts
            print(Fore.RED + f"\rAttacking... {next(spinner)}  Attempts: {attempts}", end='', flush=True)

if __name__ == "__main__":
    simulate_hacking_text("Software Name: Bitcoin Private Key Finder")
    simulate_hacking_text("Software Developed By: Pikai")
    simulate_hacking_text("Software Version: 1.0.6")
    simulate_hacking_text("Description: This software attempts to find the private key for a given Bitcoin address with brute force.")
    
    input(Fore.BLUE + "\nPress Enter to Proceed" + Style.RESET_ALL)
    
    target_address = input(Fore.GREEN + "Enter the Bitcoin address to find the private key for: " + Style.RESET_ALL)
    simulate_hacking_text(f"Starting brute force attack for private key on address: {target_address}\n", delay=0.01)

    start_time = time.time()
    private_key, attempts = brute_force_address(target_address)
    end_time = time.time()

    duration = end_time - start_time
    print(Fore.GREEN + f"\nAttack Successful! Private key found: {private_key}" + Style.RESET_ALL)
    print(Fore.GREEN + f"Total Attempts made: {attempts}" + Style.RESET_ALL)
    print(Fore.GREEN + f"Total Time taken: {duration:.2f} seconds" + Style.RESET_ALL)
