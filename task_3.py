import random
import string

print("===== PASSWORD GENERATOR =====")

# User input for password length
length = int(input("Enter desired password length: "))

# Character sets
letters = string.ascii_letters     
digits = string.digits             
symbols = string.punctuation        

# Combine all characters
all_characters = letters + digits + symbols

# Generate password
password = ""
for i in range(length):
    password += random.choice(all_characters)

# Display password
print("\nGenerated Password:", password)