# src/brute_force.py
"""
Basic brute-force on a single hash (demonstration only).
Character set: lowercase letters a-z.
You set max length (keep it small!).
"""
import itertools
import string
import time
from utils import hash_password

# ---- CONFIGURE ----
ALGORITHM = "md5"
TARGET_HASH = "900150983cd24fb0d6963f7d28e17f72"   # hash of "abc" (no salt)
MAX_LENGTH = 3   # try 1,2,3 letter passwords
# -------------------

def brute_force():
    chars = string.ascii_lowercase   # 'abcdefghijklmnopqrstuvwxyz'
    print(f"Starting brute-force up to length {MAX_LENGTH} against hash {TARGET_HASH}...")
    start = time.time()
    attempts = 0

    for length in range(1, MAX_LENGTH + 1):
        for combo in itertools.product(chars, repeat=length):
            attempt = ''.join(combo)
            attempts += 1
            if hash_password(attempt, ALGORITHM) == TARGET_HASH:
                elapsed = time.time() - start
                print(f"[+] CRACKED: '{attempt}' in {attempts} attempts, {elapsed:.2f} seconds")
                return
    print("Not found. Increase MAX_LENGTH or change character set.")

if __name__ == "__main__":
    brute_force()