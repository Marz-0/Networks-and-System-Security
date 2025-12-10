# brute_force.py
import hashlib
import time

COMMON_PASSWORDS = [
    "password", 
    "admin",
    "123",
    "wasd",
    "123456", 
    "123456789",
    "qwerty", 
    "abc123", 
    "letmein",
    "admin", 
    "iloveyou", 
    "monkey", 
    "football"
]

def hash_md5(pwd):
    return hashlib.md5(pwd.encode()).hexdigest()

def hash_sha256(pwd):
    return hashlib.sha256(pwd.encode()).hexdigest()

def dictionary_attack(target_hash, algo):
    if algo == "md5":
        hasher = hash_md5
    else:
        hasher = hash_sha256

    start = time.perf_counter()
    for p in COMMON_PASSWORDS:
        if hasher(p) == target_hash:
            elapsed = time.perf_counter() - start
            print(f"✅ Found password: {p!r} in {elapsed:.6f} seconds")
            return
    elapsed = time.perf_counter() - start
    print(f"Password not in list (checked in {elapsed:.6f} seconds)")

password = input("Enter your password: ")


for algo in ["md5", "sha256"]:
    print(f"\n--- {algo.upper()} ---")
    if algo == "md5":
        target = hash_md5(password)
    else:
        target = hash_sha256(password)
    print("Target hash:", target)
    dictionary_attack(target, algo)


