import random
import string

def generate_password(length=12):
    if length < 4:
        raise ValueError("Password length must be at least 4 characters")

    # Define the characters to be used in the password
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    # Ensure that the password contains at least one of each character type
    all_characters = uppercase + lowercase + digits + special_characters
    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(special_characters)
    ]

    # Fill the remaining length with random characters from all categories
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the resulting password list to ensure randomness
    random.shuffle(password)

    return ''.join(password)

# Example usage
password_length = 12
generated_password = generate_password(password_length)
print(f"Generated Password: {generated_password}")
