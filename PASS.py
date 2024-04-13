import re

def password_strength(password):
    # Initialize strength score
    score = 0
    
    # Criteria: Length
    if len(password) >= 8:
        score += 1
    
    # Criteria: Uppercase and lowercase letters
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    
    # Criteria: Numbers
    if re.search(r"\d", password):
        score += 1
    
    # Criteria: Special characters
    if re.search(r"[!@#$%^&*()_+{}\[\]:;<>,.?/~`]", password):
        score += 1
    
    # Feedback based on score
    if score == 0:
        return "Very Weak"
    elif score == 1:
        return "Weak"
    elif score == 2:
        return "Moderate"
    elif score == 3:
        return "Strong"
    elif score == 4:
        return "Very Strong"

# Example usage:
password = input("Enter your password: ")
strength = password_strength(password)
print("Password strength:", strength)