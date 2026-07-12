import random
import string

print("=" * 40)
print("      PASSWORD GENERATOR")
print("=" * 40)

try:
    length = int(input("Enter password length: "))

    if length <= 0:
        print("Please enter a valid positive number.")
    else:
        characters = string.ascii_letters + string.digits + string.punctuation

        password = ""

        for i in range(length):
            password += random.choice(characters)

        print("\nGenerated Password:")
        print(password)

except ValueError:
    print("Invalid input! Please enter numbers only.")