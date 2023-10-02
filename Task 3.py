import random
import string

def generate_password(length):
    # Define the character sets for password complexity
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = '!@#$%^&*()_+=-[]{}|:;<>,.?/'

    # Combine character sets based on complexity
    if length < 8:
        charset = lowercase_letters + digits
    else:
        charset = lowercase_letters + uppercase_letters + digits + special_characters

    # Generate the password
    password = ''.join(random.choice(charset) for _ in range(length))
    return password

# Prompt the user for the desired password length
while True:
    try:
        length = int(input("Enter the desired password length: "))
        if length <= 0:
            print("Please enter a positive integer.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Generate and display the password
password = generate_password(length)
print("Generated Password:", password)