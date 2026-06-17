def caesar_encrypt(text, shift):
    encrypted = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                encrypted += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                encrypted += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            encrypted += char

    return encrypted


def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


def vigenere_encrypt(text, key):
    encrypted = ""
    key = key.upper()
    key_index = 0

    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')

            if char.isupper():
                encrypted += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                encrypted += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))

            key_index += 1
        else:
            encrypted += char

    return encrypted


while True:

    print("\n===== CRYPTOGRAPHY TOOLKIT =====")
    print("1. Caesar Encrypt")
    print("2. Caesar Decrypt")
    print("3. Vigenère Encrypt")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        message = input("Enter message: ")
        shift = int(input("Enter shift value: "))

        result = caesar_encrypt(message, shift)

        print("\nEncrypted Message:", result)

    elif choice == "2":

        message = input("Enter encrypted message: ")
        shift = int(input("Enter shift value: "))

        result = caesar_decrypt(message, shift)

        print("\nDecrypted Message:", result)

    elif choice == "3":

        message = input("Enter message: ")
        key = input("Enter keyword: ")

        result = vigenere_encrypt(message, key)

        print("\nEncrypted Message:", result)

    elif choice == "4":

        print("\nThank you for using the Cryptography Toolkit.")
        break

    else:

        print("\nInvalid choice. Please try again.")