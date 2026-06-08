def caesar_encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            result += chr((ord(char.upper()) - 65 + shift) % 26 + 65)
        else:
            result += char

    return result


def vigenere_encrypt(text, key):
    result = ""
    key = key.upper()

    key_index = 0

    for char in text.upper():
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 65
            result += chr((ord(char) - 65 + shift) % 26 + 65)
            key_index += 1
        else:
            result += char

    return result


message = input("Enter message: ")

if not message.replace(" ", "").isalpha():
    print("Invalid input!")
else:
    caesar = caesar_encrypt(message, 3)

    print("\nCaesar Cipher:", caesar)

    key = input("Enter Vigenere key: ")

    vig = vigenere_encrypt(message, key)

    print("Vigenere Cipher:", vig)