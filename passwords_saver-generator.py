# Import the os module to work with file paths
import os
import random
import string

# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Prompt the user for their choice
choice = input("Do you want to save an existing password (enter 'existing') or generate a random one (enter 'random')? ").lower()

if choice == 'existing':
    # Prompt the user for the domain
    domain = input("Enter the domain: ")

    # Prompt the user for a username
    username = input("Enter your username: ")

    # Prompt the user for an existing password
    password = input("Enter your existing password: ")
elif choice == 'random':
    # Prompt the user for the domain
    domain = input("Enter the domain: ")

    # Prompt the user for a username
    username = input("Enter your username: ")

    # Prompt the user for the desired length of the random password
    password_length = int(input("Enter the desired length of the random password: "))

    # Ask the user if they want to include special characters in the password
    include_special_characters = input("Include special characters in the password? (yes/no): ").lower()

    special_characters = ""
    if include_special_characters == "yes":
        special_characters = "!@"

    # Generate a random password with or without special characters
    characters = string.ascii_letters + string.digits + special_characters
    password = ''.join(random.choice(characters) for _ in range(password_length))
else:
    print("Invalid choice. Please enter 'existing' or 'random'.")
    exit(1)

# Define the path to the passwords file
passwords_file = os.path.join(script_dir, "myPasswords.txt")

# Open the file in append mode and write the domain, username, and password with line breaks and hyphens for separation
with open(passwords_file, "a") as file:
    file.write(f"Domain: {domain}\nUsername: {username}\nPassword: {password}\n{'-' * 35}\n")

print(f"Data saved to '{passwords_file}'.")
