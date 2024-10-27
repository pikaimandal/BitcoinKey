import hashlib
import base58
import time
import colorama
from ecdsa import SigningKey, SECP256k1, BadSignatureError
from colorama import Fore, Style

# Initialize colorama
colorama.init()

def simulate_hacking_text(text, delay=0.03):
    for char in text:
        print(Fore.RED + char, end='', flush=True)
        time.sleep(delay)
    print(Style.RESET_ALL)

def private_key_to_public_key(private_key_hex, compressed=True):
    try:
        private_key_bytes = bytes.fromhex(private_key_hex)
        sk = SigningKey.from_string(private_key_bytes, curve=SECP256k1)
        vk = sk.verifying_key
    except ValueError:
        return None  # Invalid private key format

    if compressed:
        public_key = b'\x02' + vk.to_string()[:32] if vk.pubkey.point.y() % 2 == 0 else b'\x03' + vk.to_string()[:32]
    else:
        public_key = b'\x04' + vk.to_string()
    
    return public_key.hex()

def public_key_to_address(public_key_hex):
    public_key_bytes = bytes.fromhex(public_key_hex)
    
    # SHA-256
    sha256 = hashlib.sha256(public_key_bytes).digest()
    
    # RIPEMD-160
    ripemd160 = hashlib.new('ripemd160')
    ripemd160.update(sha256)
    pk_hash = ripemd160.digest()
    
    # Add network byte (0x00 for mainnet)
    extended_pk_hash = b'\x00' + pk_hash
    
    # Calculate checksum
    sha256_1 = hashlib.sha256(extended_pk_hash).digest()
    sha256_2 = hashlib.sha256(sha256_1).digest()
    checksum = sha256_2[:4]
    
    # Append checksum
    final_pk_hash = extended_pk_hash + checksum
    
    # Encode in Base58
    address = base58.b58encode(final_pk_hash)
    return address.decode('utf-8')

def validate_private_keys(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    simulate_hacking_text("Validating Private Keys...\n", delay=0.01)
    time.sleep(1)
    
    valid_addresses = []
    for line_number, private_key in enumerate(lines, start=1):
        private_key = private_key.strip()
        if len(private_key) not in [64, 66]:  # Check for typical hex lengths (64 or 66 if compressed)
            print(Fore.RED + f"Invalid private key format at line {line_number}: {private_key}" + Style.RESET_ALL)
            continue
        
        public_key_hex = private_key_to_public_key(private_key)
        if public_key_hex is None:
            print(Fore.RED + f"Invalid private key at line {line_number}: {private_key}" + Style.RESET_ALL)
            continue
        
        bitcoin_address = public_key_to_address(public_key_hex)
        valid_addresses.append(bitcoin_address)
        print(Fore.GREEN + f"Line {line_number}: Bitcoin Address: {bitcoin_address}" + Style.RESET_ALL)

    simulate_hacking_text("Validation complete.", delay=0.01)

    if valid_addresses:
        file_name = input(Fore.GREEN + "\nEnter a file name with '.txt' to save the Bitcoin addresses: " + Style.RESET_ALL)
        if not file_name.endswith('.txt'):
            file_name += '.txt'
        
        with open(file_name, 'w') as file:
            file.write("\n".join(valid_addresses))
        
        simulate_hacking_text(f"\nBitcoin addresses have been saved to {file_name}", delay=0.01)

if __name__ == "__main__":
    simulate_hacking_text("Software Name: Private Key Validator")
    simulate_hacking_text("Software Developed By: Pikai")
    simulate_hacking_text("Software Version: 1.0.0")
    simulate_hacking_text("Description: This software validates Bitcoin private keys and extracts the associated addresses.")
    
    input(Fore.GREEN + "\nPress Enter to Proceed" + Style.RESET_ALL)
    
    file_path = input(Fore.RED + "Enter the path to the TXT file containing private keys: " + Style.RESET_ALL)
    validate_private_keys(file_path)
