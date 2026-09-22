import random
import string


def get_yes_no(question):
    while True:
        answer = input(question).lower()

        if answer == "yes" or answer == "no":
            return answer

        print("Please enter yes or no.")


def generate_password():
    # Ask for password length
    while True:
        try:
            length = int(input("Enter password length (minimum 8): "))

            if length < 8:
                print("Password length must be at least 8 characters.")
                continue

            break

        except ValueError:
            print("Please enter a valid number.")

    # Choose character types
    while True:
        uppercase = get_yes_no("Include uppercase letters? yes/no: ")
        lowercase = get_yes_no("Include lowercase letters? yes/no: ")
        numbers = get_yes_no("Include numbers? yes/no: ")
        symbols = get_yes_no("Include symbols? yes/no: ")

        characters = ""
        guaranteed = ""
        count = 0

        if uppercase == "yes":
            characters += string.ascii_uppercase
            guaranteed += random.choice(string.ascii_uppercase)
            count += 1

        if lowercase == "yes":
            characters += string.ascii_lowercase
            guaranteed += random.choice(string.ascii_lowercase)
            count += 1

        if numbers == "yes":
            characters += string.digits
            guaranteed += random.choice(string.digits)
            count += 1

        if symbols == "yes":
            characters += string.punctuation
            guaranteed += random.choice(string.punctuation)
            count += 1

        if count < 2:
            print("At least 2 character types must be selected.")
            continue

        break

    # Generate remaining characters
    password = ""

    remaining = length - count

    for i in range(remaining):
        password += random.choice(characters)

    # Combine guaranteed characters and random characters
    final_password = list(guaranteed + password)

    # Shuffle password
    random.shuffle(final_password)

    print("\nGenerated password:", "".join(final_password))


# Generate passwords without restarting the program
while True:
    restart = get_yes_no("\nDo you want to generate a password? yes/no: ")

    if restart == "no":
        print("Thank you for using the password generator!")
        break

    generate_password()