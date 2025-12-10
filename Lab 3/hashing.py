# hashing.py
import hashlib
import bcrypt

password = input("Enter a password to hash: ")

# MD5
md5_hash = hashlib.md5(password.encode()).hexdigest()

# SHA-256
sha256_hash = hashlib.sha256(password.encode()).hexdigest()

# bcrypt. salt handled here as well
bcrypt_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

print("\n--- Hashes ---")
print("MD5     :", md5_hash)
print("SHA-256 :", sha256_hash)
print("bcrypt  :", bcrypt_hash.decode())

# verifying with bcrypt
attempt = input("\nRe-enter password to verify with bcrypt: ")
if bcrypt.checkpw(attempt.encode(), bcrypt_hash):
    print("✅ bcrypt check passed")
else:
    print("bcrypt check failed")
