def caesar_encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            result += chr((ord(char.upper()) - 65 + shift) % 26 + 65)
        else:
            result += char

    return result


def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


message = input("Enter message: ")

if not message.replace(" ", "").isalpha():
    print("Invalid input! Use letters only.")
else:
    shift = int(input("Enter shift value: "))

    encrypted = caesar_encrypt(message, shift)
    decrypted = caesar_decrypt(encrypted, shift)

    print("\nOriginal:", message)
    print("Encrypted:", encrypted)
    print("Decrypted:", decrypted)