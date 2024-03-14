import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    print("Welcome to Password Generator")
    while True:
        try:
            length = int(input("\nEnter the length of the password (default is 12): "))
            if length <= 0:
                print("Length should be a positive integer. Using default length of 12.")
                length = 12
        except ValueError:
            print("Invalid input. Using default length of 12.")
            length = 12

        password = generate_password(length)
        print("Generated Password:", password)

        again = input("Do you want to generate another password? (yes/no): ")
        if again.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
