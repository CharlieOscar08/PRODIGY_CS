import re

def assess_password_strength(password):
    """
    Assess the strength of a password based on length, presence of uppercase and lowercase letters, numbers, and special characters.
    
    Parameters:
    password (str): The password to assess.
    
    Returns:
    str: A message indicating the strength of the password.
    """
    # Check for minimum length
    if len(password) < 8:
        return "Password is too short. It should be at least 8 characters long."
    
    # Check for uppercase letter
    if not re.search(r'[A-Z]', password):
        return "Password should contain at least one uppercase letter."
    
    # Check for lowercase letter
    if not re.search(r'[a-z]', password):
        return "Password should contain at least one lowercase letter."
    
    # Check for number
    if not re.search(r'\d', password):
        return "Password should contain at least one number."
    
    # Check for special character
    if not re.search(r'\W', password):
        return "Password should contain at least one special character."
    
    # If all criteria are met
    return "Password is strong!"

def main():
    """
    Main function to interact with the user and assess the password strength.
    """
    # Get the password from the user
    password = input("Enter your password: ")
    
    # Assess the password strength
    strength = assess_password_strength(password)
    
    # Display the assessment result
    print(strength)

if __name__ == "__main__":
    main()
