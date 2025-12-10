# auth_system_simple.py
import bcrypt
import pyotp
import qrcode
import string

# In-memory "database":
# username -> {"hash": ..., "totp_secret": ...}
users = {}


def password_is_strong(pwd):
    """Very simple policy: length >= 8, and has upper, lower, digit, special."""
    if len(pwd) < 8:
        return False, "Password must be at least 8 characters."
    if not any(c.islower() for c in pwd):
        return False, "Password must contain a lowercase letter."
    if not any(c.isupper() for c in pwd):
        return False, "Password must contain an uppercase letter."
    if not any(c.isdigit() for c in pwd):
        return False, "Password must contain a digit."
    if not any(c in string.punctuation for c in pwd):
        return False, "Password must contain a special character."
    return True, "OK"


def create_totp_qr(username, secret):
    """
    Create a TOTP object, get the provisioning URI and save a QR code image.

    Returns:
        (uri, filename)
    """
    issuer = "NSSecWeek03"  
    totp = pyotp.TOTP(secret)

    # Provisioning URI for authenticator apps
    uri = totp.provisioning_uri(name=username, issuer_name=issuer)

    # Save QR code as PNG
    filename = f"totp_qr_{username}.png"
    img = qrcode.make(uri)
    img.save(filename)

    return uri, filename


def register_user():
    username = input("Choose a username: ").strip()
    if username in users:
        print("That username is already taken.")
        return

    password = input("Choose a password: ")
    ok, msg = password_is_strong(password)
    if not ok:
        print("Password rejected:", msg)
        return

    # bcrypt hash. includes salt 
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    # TOTP secret per user
    secret = pyotp.random_base32()

    # Generate QR code and provisioning URI
    uri, filename = create_totp_qr(username, secret)

    # Store user data
    users[username] = {
        "hash": pw_hash,
        "totp_secret": secret
    }

    print("\n✅ User registered.")
    print("TOTP secret (for debugging only – don't show this in real systems!):")
    print(secret)
    print("\nScan this QR code with your authenticator app:")
    print(f"    File: {filename}")
    print("\nOr use this provisioning URI directly:")
    print(uri)


def authenticate_user():
    username = input("Username: ").strip()
    if username not in users:
        print("Unknown user.")
        return

    password = input("Password: ")
    stored_hash = users[username]["hash"]

    if not bcrypt.checkpw(password.encode(), stored_hash):
        print("❌ Incorrect password.")
        return

    # Check TOTP
    secret = users[username]["totp_secret"]
    totp = pyotp.TOTP(secret)
    code = input("Enter TOTP code from your app: ")

    if totp.verify(code, valid_window=1):
        print("✅ Login successful.")
    else:
        print("❌ Invalid TOTP code.")


def main():
    while True:
        print("\n=== Auth System Demo ===")
        print("1) Register")
        print("2) Login")
        print("3) Quit")
        choice = input("Choice: ")

        if choice == "1":
            register_user()
        elif choice == "2":
            authenticate_user()
        elif choice == "3":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
