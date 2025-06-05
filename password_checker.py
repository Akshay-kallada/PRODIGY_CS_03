import re
import math
from datetime import datetime

# Common passwords list for additional check
COMMON_PASSWORDS = [
    'password', '123456', '12345678', '1234', 'qwerty', '12345', 
    'dragon', 'baseball', 'football', 'letmein', 'monkey', 'abc123'
]

def check_password_strength(password):
    """Enhanced password strength checker with more features"""
    
    # Original checks
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None
    
    # New checks being added
    common_error = password.lower() in COMMON_PASSWORDS
    sequential_error = any(
        str(i)*3 in password or 
        chr(ord('a')+i)*3 in password.lower() 
        for i in range(8)
    )
    repeated_error = re.search(r"(.)\1{2,}", password) is not None
    
    # Calculate entropy for better strength measurement
    pool_size = 0
    if not lowercase_error: pool_size += 26
    if not uppercase_error: pool_size += 26
    if not digit_error: pool_size += 10
    if not symbol_error: pool_size += 32  # approx special chars
    
    entropy = len(password) * math.log2(pool_size) if pool_size else 0
    
    # Original score calculation (0-5)
    base_score = 5 - sum([length_error, digit_error, uppercase_error, lowercase_error, symbol_error])
    
    # Adjust score based on new checks
    final_score = base_score
    if common_error: final_score = max(0, final_score - 2)
    if sequential_error: final_score = max(0, final_score - 1)
    if repeated_error: final_score = max(0, final_score - 1)
    
    # Time to crack estimation (very rough approximation)
    crack_time = "seconds"
    if entropy > 65: crack_time = "centuries"
    elif entropy > 55: crack_time = "years"
    elif entropy > 45: crack_time = "months"
    elif entropy > 35: crack_time = "days"
    elif entropy > 25: crack_time = "hours"
    
    print("\n--- Password Analysis ---")
    print(f"Password: {'*' * len(password)}")  # Hide password for security
    print(f"Length: {len(password)} characters")
    
    # Original feedback
    if length_error:
        print("❌ Should be at least 8 characters long")
    if digit_error:
        print("❌ Add at least one number")
    if uppercase_error:
        print("❌ Add at least one uppercase letter")
    if lowercase_error:
        print("❌ Add at least one lowercase letter")
    if symbol_error:
        print("❌ Add at least one special character")
    
    # New feedback
    if common_error:
        print("❌ This is a very common password")
    if sequential_error:
        print("❌ Contains simple sequences (like 123 or abc)")
    if repeated_error:
        print("❌ Has repeated characters (like aaa or 111)")
    
    print("\n--- Strength Assessment ---")
    print(f"Estimated entropy: {entropy:.1f} bits")
    print(f"Time to crack: {crack_time}")
    
    # Enhanced strength rating with color suggestions
    if final_score >= 4 and entropy > 50 and not common_error:
        print("✅ Excellent Password (Very Strong) 💪")
        print("💡 Tip: Consider using this in a password manager!")
    elif final_score >= 3:
        print("⚠️ Good Password (Could Be Stronger)")
        print("💡 Tip: Add more special characters or length")
    else:
        print("🚫 Weak Password (Needs Significant Improvement)")
        print("💡 Tip: Avoid common words and patterns")

if __name__ == "__main__":
    print("=== Password Strength Checker ===")
    print("(Type 'quit' to exit)")
    
    while True:
        user_input = input("\nEnter your password: ")
        if user_input.lower() == 'quit':
            break
        check_password_strength(user_input)