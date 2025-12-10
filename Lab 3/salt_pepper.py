# salt_pepper.py
import hashlib
import secrets

PEPPER = "Secret_PEPPER_for_HASH"

password = input("Enter your password to hash: ")

# 1) No salt, no pepper
no_salt_hash = hashlib.sha256(password.encode()).hexdigest()

# 2) With salt
salt = secrets.token_hex(16)  # random 16-byte salt as hex string
with_salt_hash = hashlib.sha256((salt + password).encode()).hexdigest()

# 3) With salt + pepper
with_salt_pepper_hash = hashlib.sha256((salt + password + PEPPER).encode()).hexdigest()

print("Password:", password)
print("\n1) No salt")
print("   Hash:", no_salt_hash)

print("\n2) With salt")
print("   Salt:", salt)
print("   Hash:", with_salt_hash)

print("\n3) With salt + pepper")
print("   Salt  :", salt)
print("   Pepper:", PEPPER)
print("   Hash  :", with_salt_pepper_hash)
