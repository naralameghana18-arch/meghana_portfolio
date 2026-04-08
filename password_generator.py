import random
import string

print("Password Generator")

# user input
length = int(input("Enter password length: "))

# characters to use
characters = string.ascii_letters + string.digits + string.punctuation

# generate password
password = ''.join(random.choice(characters) for _ in range(length))

print("Generated Password:", password)
