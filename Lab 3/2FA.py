# 2FA.py
import pyotp
import qrcode

# Generate secret for a user
secret = pyotp.random_base32()
print("TOTP secret:", secret)

# Create provisioning URI (for authenticator apps)
account_name = "student@example.com"
issuer = "NSSecWeek03"
totp = pyotp.TOTP(secret)
uri = totp.provisioning_uri(name=account_name, issuer_name=issuer)
print("\nProvisioning URI:")
print(uri)

# Save QR code
img = qrcode.make(uri)
img.save("totp_qr.png")
print("\nQR code saved as totp_qr.png (scan with Google Authenticator / Authy).")

# Verify codes from app
while True:
    code = input("\nEnter 6-digit code from app (or 'exit'): ")
    if code.lower() == "exit":
        break

    if totp.verify(code, valid_window=1):
        print("✅ Code is valid")
    else:
        print("❌ Code is invalid or expired")
