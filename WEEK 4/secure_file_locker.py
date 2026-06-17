from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

print("===== SECURE FILE LOCKER =====")

filename = input("Enter file name to encrypt: ")

key = get_random_bytes(16)

cipher = AES.new(key, AES.MODE_EAX)

with open(filename, "rb") as file:
    data = file.read()

ciphertext, tag = cipher.encrypt_and_digest(data)

with open("encrypted.bin", "wb") as file:
    file.write(cipher.nonce)
    file.write(tag)
    file.write(ciphertext)

print("\nFile encrypted successfully!")

decrypt_choice = input("\nDecrypt file now? (Y/N): ")

if decrypt_choice.upper() == "Y":

    with open("encrypted.bin", "rb") as file:
        nonce = file.read(16)
        tag = file.read(16)
        ciphertext = file.read()

    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)

    decrypted_data = cipher.decrypt_and_verify(ciphertext, tag)

    with open("recovered.txt", "wb") as file:
        file.write(decrypted_data)

    print("\nFile decrypted successfully!")
    print("Recovered file saved as recovered.txt")

else:

    print("\nProgram completed.")