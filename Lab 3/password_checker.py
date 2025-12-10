
# Password strength checker

from math import log2
import string

while True:
    points = 0
    
    password = input("Enter your password (or type 'exit' to quit): ")

    pool_size = 94 # Total number of possible characters (26 lowercase + 26 uppercase + 10 digits + 32 special characters etc.)

    approx_entropy = len(password) * log2(pool_size) 
    
    # Check if user wants to exit the program using the "exit" command
    if password.lower() == 'exit':
        print("Exiting password checker. Goodbye!")
        break

    if len(password) < 8: # Minimum length requirement of 8 characters
        print("Password is too short, please enter at least 8 characters.")
    elif not any(char.isdigit() for char in password): # At least one digit
        print("Password must contain at least one digit.")
    elif not any(char.isupper() for char in password): # At least one uppercase letter
        print("Password must contain at least one uppercase letter.")
    elif not any(char.islower() for char in password): # At least one lowercase letter
        print("Password must contain at least one lowercase letter.")
    elif not any(char in string.punctuation for char in password):
        print("Password must contain at least one special character.")
    else:
        print("Password is acceptable.") 


    for char in password:
        if char.islower():
            points += 1
        if char.isupper():
            points += 2
        if char.isdigit():
            points += 2
        if char in string.punctuation:
            points += 2
        if len(password) >= 8:
            points += 1


    common_passwords = ['password', '123456', '123456789', 'qwerty', 'abc123', 'password1', '111111', '12345678', 'iloveyou', 'admin']
    if password in common_passwords:
        print("Password is too common, please choose a more unique password.")

    print("Password strength points:", points)
    print("Estimated password strength (in bits):", approx_entropy)
    print()  