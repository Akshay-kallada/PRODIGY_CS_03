# Password Strength Assessor 🔒

![Password Strength Demo](demo.gif) *(Example GIF showing the tool in action)*

A Python-based tool that evaluates password strength using multiple criteria and provides actionable feedback for improvement.

## Features ✨

- **Comprehensive Strength Analysis**:
  - Length requirements (8+ characters recommended)
  - Presence of uppercase/lowercase letters
  - Number inclusion
  - Special character verification
- **Advanced Security Checks**:
  - Common password detection
  - Sequential pattern recognition (e.g., "123", "abc")
  - Repeated character identification
- **Scientific Measurements**:
  - Entropy calculation (in bits)
  - Estimated time-to-crack
- **User-Friendly Feedback**:
  - Clear error indicators
  - Strength rating with emoji visualization
  - Practical improvement tips
- **Privacy Protection**:
  - Password masking during display
  - No storage or logging of checked passwords

## Installation ⚙️

1. Ensure you have Python 3.6+ installed
2. Clone this repository:
   ```bash
   git clone https://github.com/Akshay-kallada/password-strength-assessor.git

   Navigate to the project directory:
   cd password-strength-assessor

   Usage 🚀
   python password_strength.py

   Then:

1. Enter a password when prompted

2. Receive instant analysis and feedback

3. Type 'quit' to exit the program

Example Output 📊
=== Password Strength Checker ===
(Type 'quit' exit)

Enter your password: Example123!

--- Password Analysis ---
Password: ***********
Length: 11 characters
✓ Contains uppercase letters
✓ Contains lowercase letters
✓ Contains numbers
✓ Contains special characters

--- Strength Assessment ---
Estimated entropy: 65.2 bits
Time to crack: years
✅ Excellent Password (Very Strong) 💪
💡 Tip: Consider using this in a password manager!

Requirements 📦
Python 3.6+

No external dependencies required

Contributing 🤝
Contributions are welcome! Please open an issue or submit a pull request for any:

• Bug fixes

• Additional password checks

• Improved entropy calculations

• UI enhancements

Security Note 🔐
This tool:

• Does not store or log any passwords

• Runs entirely locally on your machine

• Is for educational purposes only
