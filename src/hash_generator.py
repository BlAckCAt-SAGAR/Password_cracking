# src/hash_generator.py
"""
Generate hashes from a wordlist and save them as targets.
You can optionally use a salt file (data/salt.txt).
"""
import os
from utils import hash_password, load_lines

# ---------- CONFIGURATION (change these as needed) ----------
ALGORITHM = "md5"               # try 'sha1' or 'sha256' later
USE_SALT = False                # set True to use salt
WORDLIST_PATH = "../data/common_passwords.txt"
TARGET_HASHES_PATH = "../data/target_hashes.txt"
SALT_FILE = "../data/salt.txt"
# -----------------------------------------------------------

def main():
    # Load salt if enabled
    salt = None
    if USE_SALT:
        if not os.path.exists(SALT_FILE):
            print(f"Error: Salt file not found at {SALT_FILE}")
            return
        salt = load_lines(SALT_FILE)[0]  # use first line as salt
        print(f"Using salt: '{salt}'")

    # Load passwords
    if not os.path.exists(WORDLIST_PATH):
        print(f"Error: Wordlist not found at {WORDLIST_PATH}")
        return
    passwords = load_lines(WORDLIST_PATH)
    print(f"Loaded {len(passwords)} passwords from {WORDLIST_PATH}")

    # Generate hashes and write to file
    with open(TARGET_HASHES_PATH, "w", encoding="utf-8") as out:
        for pwd in passwords:
            h = hash_password(pwd, ALGORITHM, salt)
            out.write(h + "\n")

    print(f"Generated {len(passwords)} {ALGORITHM.upper()} hashes -> {TARGET_HASHES_PATH}")
    if USE_SALT:
        print("Remember: The salt is NOT stored in the hash file (cracker must know it).")

if __name__ == "__main__":
    main()