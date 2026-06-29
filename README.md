# 🔐 Password Cracking & Hashing Algorithms

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-success?style=for-the-badge)
![Built With](https://img.shields.io/badge/Built%20With-Standard%20Library-orange?style=for-the-badge)

**A hands-on cybersecurity project demonstrating password hashing, salting, dictionary attacks, and brute-force techniques.**

</div>

---

## 📖 Table of Contents

- [Overview](#-overview)
- [Project Structure](#-project-structure)
- [How It Works](#-how-it-works)
- [Algorithms Implemented](#-algorithms-implemented)
- [Installation & Usage](#-installation--usage)
- [Demo Results](#-demo-results)
- [Security Concepts Learned](#-security-concepts-learned)
- [Tools & Technologies](#-tools--technologies)
- [Future Enhancements](#-future-enhancements)
- [License](#-license)
- [Author](#-author)

---

## 🎯 Overview

This project was developed as part of a **1-Month Cyber Security Internship** to understand how passwords are stored, hashed, and cracked. It implements:

- **Hashing algorithms** (MD5, SHA-1, SHA-256) using Python's `hashlib`
- **Salted hashing** to defeat rainbow table attacks
- **Dictionary attacks** using common password wordlists
- **Brute-force attacks** to demonstrate computational complexity

The goal is **educational** — to understand the weaknesses of weak hashing algorithms and the importance of strong password policies.

---

## 📁 Project Structure

```
password-cracking-project/
│
├── .gitignore
├── .gitattributes
├── LICENSE
├── README.md
├── requirements.txt
│
├── src/
│   ├── utils.py
│   ├── hash_generator.py
│   ├── dictionary_attack.py
│   └── brute_force.py
│
├── data/
│   ├── common_passwords.txt
│   ├── salt.txt
│   └── target_hashes.txt
│
├── results/
│   └── cracked_passwords.txt
│
└── demo_screenshots/
    ├── hash_generation.png
    ├── dictionary_crack.png
    └── brute_force.png
```

---

## ⚙️ How It Works

### Flow Diagram

```
┌─────────────────┐     ┌──────────────────┐     ┌──────────────────┐
│  Wordlist       │────▶│  Hash Generator  │────▶│  Target Hashes   │
│  (plaintext)    │     │  (+ optional salt)│     │  (MD5/SHA1/256)  │
└─────────────────┘     └──────────────────┘     └────────┬─────────┘
                                                          │
                                                          ▼
┌─────────────────┐     ┌──────────────────┐     ┌──────────────────┐
│  Cracked        │◀────│  Dictionary /    │◀────│  Attack Script   │
│  Passwords      │     │  Brute Force     │     │  (compares hashes)│
└─────────────────┘     └──────────────────┘     └──────────────────┘
```

### Step-by-Step Process

| Step | Script | Action |
|:----:|:-------|:-------|
| 1 | `hash_generator.py` | Reads `common_passwords.txt`, computes hashes (with optional salt), writes to `target_hashes.txt` |
| 2 | `dictionary_attack.py` | Reads wordlist and target hashes, computes hash of each word, compares — if match found, password is cracked |
| 3 | `brute_force.py` | Tries every possible character combination (a-z) up to a given length against a single hash |

---

## 🔬 Algorithms Implemented

| Algorithm | Type | Output Size | Security Level | Usage in Project |
|:----------|:-----|:-----------:|:--------------:|:-----------------|
| **MD5** | Hash | 128-bit | ❌ Broken | Default hashing algorithm |
| **SHA-1** | Hash | 160-bit | ❌ Weak | Alternative algorithm option |
| **SHA-256** | Hash | 256-bit | ✅ Secure | Recommended for real use |
| **Salt** | Protection | Variable | ✅ Adds entropy | Optional suffix/prefix to passwords |

### Why Salt Matters

**Without Salt:**
```
password → MD5 → 5f4dcc3b5aa765d61d8327deb882cf99
```
Same password always = same hash → vulnerable to rainbow tables.

**With Salt ("mysalt123"):**
```
password → password+mysalt123 → MD5 → a3f7b2c9d1e4f5a6b7c8d9e0f1a2b3c4
```
Rainbow tables useless without knowing the salt.

---

## 🚀 Installation & Usage

### Prerequisites

- **Python 3.8+** installed on your system
- No external libraries required (uses only Python Standard Library)

### Setup

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/password-cracking-project.git
cd password-cracking-project
```

Verify Python version:

```bash
python --version
```

### Running the Project

#### 1. Generate Target Hashes

```bash
cd src
python hash_generator.py
```

Expected output:
```
Loaded 18 passwords from wordlist
Generated 18 MD5 hashes -> ../data/target_hashes.txt
```

#### 2. Run Dictionary Attack

```bash
python dictionary_attack.py
```

Expected output:
```
Loaded 18 passwords from wordlist
Loaded 18 target hashes
[+] Cracked: 5f4dcc3b5aa765d61d8327deb882cf99 -> 'password'
[+] Cracked: 7c6a180b36896a0a8c02787eeafb0e4c -> 'password1'
...
Done. Cracked 18/18 hashes in 0.02 seconds.
```

#### 3. Run Brute-Force Demo

```bash
python brute_force.py
```

Expected output:
```
Starting brute-force up to length 3 against hash 900150983cd24fb0d6963f7d28e17f72...
[+] CRACKED: 'abc' in 18278 attempts, 0.18 seconds
```

### Testing with Salt

1. Set `USE_SALT = True` in **both** `hash_generator.py` and `dictionary_attack.py`
2. Ensure `data/salt.txt` contains your salt value
3. Run generator, then attack — it still cracks because the cracker knows the salt
4. Try cracking without the salt → **fails** (demonstrates salt's protective effect)

### Testing with SHA-256

1. Change `ALGORITHM = "sha256"` in **both** scripts
2. Run generator and attack again — works identically but with stronger hashes

---

## 📸 Demo Results

### Hash Generation
![Hash Generation](demo_screenshots/hash_generation.png)

### Dictionary Attack - All 18 Passwords Cracked
![Dictionary Attack](demo_screenshots/dictionary_crack.png)

### Brute-Force on 3-Character Password
![Brute Force](demo_screenshots/brute_force.png)

---

## 🧠 Security Concepts Learned

| Concept | What I Learned |
|:--------|:---------------|
| **Hashing** | One-way functions that convert plaintext to fixed-size digests. Cannot be reversed — only compared. |
| **Salting** | Adding random data to passwords before hashing. Defeats pre-computed rainbow tables. |
| **Dictionary Attack** | Using a pre-compiled list of common passwords to crack hashes. Fast and effective against weak passwords. |
| **Brute-Force Attack** | Trying every possible character combination. Guaranteed to succeed but exponentially slow. |
| **MD5 Weakness** | MD5 is cryptographically broken. Should never be used for password storage in production. |
| **Defence Strategies** | Use bcrypt/scrypt/Argon2 for password storage, enforce minimum password length, implement account lockout. |

### Time Complexity Comparison

```
Password: "abc" (3 chars, lowercase only)
  Dictionary Attack:     < 0.001 seconds  (if in wordlist)
  Brute Force:           ~ 0.18 seconds   (26³ = 17,576 attempts)

Password: "abcd" (4 chars, lowercase only)
  Brute Force:           ~ 4.5 seconds    (26⁴ = 456,976 attempts)

Password: "abcde" (5 chars, lowercase only)
  Brute Force:           ~ 118 seconds    (26⁵ = 11,881,376 attempts)
```

---

## 🛠️ Tools & Technologies

| Category | Technology |
|:---------|:-----------|
| **Language** | Python 3.8+ |
| **Libraries** | `hashlib`, `argparse`, `itertools`, `time` (all built-in) |
| **Hashing Algorithms** | MD5, SHA-1, SHA-256 |
| **Development** | VS Code, Git |
| **Version Control** | Git, GitHub |
| **Reference Tools** | Hashcat, John the Ripper (conceptual understanding) |

---

## 🔮 Future Enhancements

- [ ] Implement bcrypt/Argon2 hashing for production-grade demonstration
- [ ] Add multi-threaded brute-force for performance comparison
- [ ] Integrate rainbow table generation and lookup
- [ ] Create a simple GUI using Tkinter
- [ ] Add password strength checker module
- [ ] Compare cracking speed with Hashcat benchmarks
- [ ] Implement hybrid attack (dictionary words + mutations)

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Sagar Unhale**

[GitHub](https://github.com/BlAckCAt-SAGAR) | [LinkedIn](https://linkedin.com/in/sagar-unhale)

---

<div align="center">

**If you found this project helpful, please star the repository!** ⭐

</div>