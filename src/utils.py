# src/utils.py
import hashlib

def hash_password(password: str, algorithm: str = "md5", salt: str = None) -> str:
    """
    Hash a password with optional salt.
    algorithm: 'md5', 'sha1', 'sha256'
    salt: if provided, it's appended to the password before hashing.
    Returns hexadecimal string.
    """
    # Combine password and salt (if any)
    data = password
    if salt:
        data = password + salt   # simple suffix salt; you can change to prefix: salt + password

    # Select hash function
    if algorithm == "md5":
        h = hashlib.md5(data.encode())
    elif algorithm == "sha1":
        h = hashlib.sha1(data.encode())
    elif algorithm == "sha256":
        h = hashlib.sha256(data.encode())
    else:
        raise ValueError(f"Unsupported algorithm: {algorithm}")

    return h.hexdigest()

def load_lines(filename: str) -> list:
    """Read file, strip whitespace, ignore empty lines."""
    with open(filename, "r", encoding="utf-8", errors="ignore") as f:
        return [line.strip() for line in f if line.strip()]

def save_result(filename: str, hash_value: str, password: str):
    """Append a cracked hash:password pair to results file."""
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"{hash_value}:{password}\n")