# Week 3 Practical Summary  


## Password Strength Checking

I built a simple password policy checker that evaluates length, character variety, and whether a password is too common. I also calculated approximate entropy to understand how predictable passwords can weaken security.

Finding:
Short or predictable passwords have very low entropy and are highly vulnerable to guessing attacks.

## Hashing with MD5, SHA-256, and bcrypt

I compared three hashing algorithms by hashing the same password and observing their differences.

Finding:

MD5 and SHA-256 are extremely fast and therefore unsuitable for password storage.

bcrypt is intentionally slow and includes a built-in salt, making it far more resistant to brute-force attacks.

## Salts and Peppers

Demonstrated how hashing the same password with and without salts/peppers produces different results.

Finding:

Without salts, identical passwords generate identical hashes. They are vulnerable to rainbow-table attacks.

Adding a salt and pepper makes hashes unique and significantly harder to crack.

## Two-Factor Authentication (TOTP)

Generated a TOTP secret, created a QR code, and verified 6-digit one-time codes from an authenticator app. I also integrated this into my authentication system.

Finding:
Even if a password is compromised, an attacker cannot log in without the one-time code, showing how 2FA provides a strong second layer of defence.

## Dictionary Attack Simulation

Created a simple brute-force script that tries common passwords against hashed values.

Finding:
Weak passwords like password or 123456 were cracked instantly for both MD5 and SHA-256, demonstrating how fast hash functions enable large-scale attacks.

## Final Authentication System

Combined all techniques into a working login system using:

Password strength checks

bcrypt hashing

Per-user TOTP secrets

QR-code-based 2FA

Finding:
Layering defences (strong passwords + slow hashing + salts + 2FA) dramatically increases security and reflects how real-world authentication systems are built.

## What I Learned

Password strength is measurable, and entropy gives a realistic view of "guessability".

Hashing alone is not enough. Algorithm choices and salting are extremely crucial.

bcrypt’s slowness is a feature, not a flaw.

TOTP based 2FA significantly reduces risks from password theft (It adds an extra layer of security).

Brute force experiments make weaknesses visible and reinforce why strong authentication matters.

Combining multiple controls and layers creates a robust, real world authentication pipeline.