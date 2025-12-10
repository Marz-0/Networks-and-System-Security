import string
import math


def analyze_password_strength(password):
    """
    Analyzes password strength based on multiple criteria:
    - Length (8+ and 12+ character thresholds)
    - Character variety (uppercase, lowercase, numbers, special characters)
    - Common password check
    - Entropy calculation
    
    Returns a dictionary with score, strength rating, and detailed feedback.
    """
    score = 0
    feedback = []
    
    # Common weak passwords list
    common_passwords = [
        'password', '123456', '12345678', 'qwerty', 'abc123',
        'monkey', '1234567', 'letmein', 'trustno1', 'dragon',
        'baseball', 'iloveyou', 'master', 'sunshine', 'ashley',
        'bailey', 'passw0rd', 'shadow', '123123', '654321',
        'superman', 'qazwsx', 'michael', 'football', 'password1'
    ]
    
    # 1. Length Check
    length = len(password)
    
    if length >= 8:
        score += 1
        feedback.append("✓ Length meets 8-character minimum")
    else:
        feedback.append("✗ Password should be at least 8 characters")
    
    if length >= 12:
        score += 1
        feedback.append("✓ Length meets 12-character minimum (strong)")
    else:
        feedback.append("✗ Consider using 12+ characters for better security")
    
    # 2. Character Variety Checks
    has_uppercase = any(c.isupper() for c in password)
    has_lowercase = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)
    
    if has_uppercase:
        score += 1
        feedback.append("✓ Contains uppercase letters")
    else:
        feedback.append("✗ Add uppercase letters (A-Z)")
    
    if has_lowercase:
        score += 1
        feedback.append("✓ Contains lowercase letters")
    else:
        feedback.append("✗ Add lowercase letters (a-z)")
    
    if has_digit:
        score += 1
        feedback.append("✓ Contains numbers")
    else:
        feedback.append("✗ Add numbers (0-9)")
    
    if has_special:
        score += 1
        feedback.append("✓ Contains special characters")
    else:
        feedback.append("✗ Add special characters (!@#$%^&*)")
    
    # 3. Common Password Check
    if password.lower() in common_passwords:
        score -= 2  # Penalty for common passwords
        feedback.append("✗ WARNING: This is a commonly used password!")
    else:
        score += 1
        feedback.append("✓ Not in common password list")
    
    # 4. Entropy Calculation
    pool_size = 0
    if has_lowercase:
        pool_size += 26
    if has_uppercase:
        pool_size += 26
    if has_digit:
        pool_size += 10
    if has_special:
        pool_size += len(string.punctuation)
    
    entropy = 0
    if pool_size > 0:
        entropy = length * math.log2(pool_size)
    
    feedback.append(f"→ Entropy: {entropy:.2f} bits")
    
    # Entropy-based scoring
    if entropy >= 60:
        score += 2
        feedback.append("✓ Excellent entropy (60+ bits)")
    elif entropy >= 40:
        score += 1
        feedback.append("✓ Good entropy (40+ bits)")
    else:
        feedback.append("✗ Low entropy - password is predictable")
    
    # Determine strength rating
    max_score = 9  # Maximum possible score
    if score < 0:
        score = 0
    
    if score >= 8:
        strength = "Very Strong"
        color = "🟢"
    elif score >= 6:
        strength = "Strong"
        color = "🟡"
    elif score >= 4:
        strength = "Moderate"
        color = "🟠"
    else:
        strength = "Weak"
        color = "🔴"
    
    return {
        'score': score,
        'max_score': max_score,
        'strength': strength,
        'color': color,
        'entropy': entropy,
        'feedback': feedback,
        'pool_size': pool_size
    }


def display_password_analysis(password):
    """
    Displays a formatted analysis of the password strength.
    """
    print(f"\n{'='*60}")
    print(f"PASSWORD STRENGTH ANALYSIS")
    print(f"{'='*60}")
    print(f"Password: {'*' * len(password)} (length: {len(password)})")
    print()
    
    result = analyze_password_strength(password)
    
    print(f"{result['color']} Strength: {result['strength']}")
    print(f"Score: {result['score']}/{result['max_score']}")
    print(f"Character Pool Size: {result['pool_size']}")
    print(f"Entropy: {result['entropy']:.2f} bits")
    print()
    
    print("Detailed Feedback:")
    print("-" * 60)
    for item in result['feedback']:
        print(f"  {item}")
    print(f"{'='*60}\n")
    
    return result


# Test the password strength analyzer
if __name__ == "__main__":
    # Test passwords with varying strengths
    test_passwords = [
        "password",                      # Very weak
        "Password1",                     # Weak
        "P@ssw0rd",                      # Moderate
        "MyP@ssw0rd123",                 # Strong
        "Tr0ub4dor&3",                   # Strong
        "correct horse battery staple",  # Moderate (no special chars/numbers)
        "X9#mK2$pL5@qR8*nT1"            # Very Strong
    ]
    
    for pwd in test_passwords:
        display_password_analysis(pwd)
        input("Press Enter to continue...")  # Pause between each analysis
