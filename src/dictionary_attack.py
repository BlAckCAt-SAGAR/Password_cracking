# src/dictionary_attack.py
"""
Dictionary attack against a list of target hashes.
Supports salted/unsalted hashes and multiple algorithms.
"""
import os
import time
from utils import hash_password, load_lines, save_result

# ---------- CONFIGURATION ----------
ALGORITHM = "md5"                 # must match what you used to generate hashes
USE_SALT = False                  # set True if the target hashes were generated with salt
WORDLIST_PATH = "../data/common_passwords.txt"
TARGET_HASHES_PATH = "../data/target_hashes.txt"
RESULTS_PATH = "../results/cracked_passwords.txt"
SALT_FILE = "../data/salt.txt"
# -----------------------------------

def main():
    # Load salt if used
    salt = None
    if USE_SALT:
        if not os.path.exists(SALT_FILE):
            print(f"Error: Salt file not found at {SALT_FILE}")
            return
        salt = load_lines(SALT_FILE)[0]
        print(f"Using salt: '{salt}'")

    # Load wordlist
    if not os.path.exists(WORDLIST_PATH):
        print(f"Error: Wordlist not found at {WORDLIST_PATH}")
        return
    passwords = load_lines(WORDLIST_PATH)
    print(f"Loaded {len(passwords)} passwords from wordlist")

    # Load target hashes
    if not os.path.exists(TARGET_HASHES_PATH):
        print(f"Error: Target hash file not found at {TARGET_HASHES_PATH}")
        return
    target_hashes = set(load_lines(TARGET_HASHES_PATH))   # set for fast lookup
    print(f"Loaded {len(target_hashes)} target hashes")

    # Clear previous results
    if os.path.exists(RESULTS_PATH):
        os.remove(RESULTS_PATH)

    # Begin attack
    start = time.time()
    cracked = 0
    for pwd in passwords:
        computed_hash = hash_password(pwd, ALGORITHM, salt)
        if computed_hash in target_hashes:
            print(f"[+] Cracked: {computed_hash} -> '{pwd}'")
            save_result(RESULTS_PATH, computed_hash, pwd)
            cracked += 1

    elapsed = time.time() - start
    print(f"\nDone. Cracked {cracked}/{len(target_hashes)} hashes in {elapsed:.2f} seconds.")
    print(f"Results saved to {RESULTS_PATH}")

if __name__ == "__main__":
    main()