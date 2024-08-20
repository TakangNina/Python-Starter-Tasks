import string
import random

def generate_password(length):
    """
    Generates a random password of the specified length.
    
    Args:
        length (int): The desired length of the password.
    
    Returns:
        str: The generated password.
    """
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

if __name__ == "__main__":
    password_length = int(input("Enter the desired length of the password: "))
    password = generate_password(password_length)
    print(f"Your generated password is: {password}")
