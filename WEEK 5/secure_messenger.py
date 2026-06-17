from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

print("===== SECURE RSA MESSENGER =====")

# Generate RSA Keys
key = RSA.generate(2048)

private_key = key
public_key = key.publickey()

# Alice writes a message
message = input("Alice's Message: ")

# Encrypt using Bob's public key
cipher_encrypt = PKCS1_OAEP.new(public_key)

ciphertext = cipher_encrypt.encrypt(message.encode())

print("\nEncrypted Message:")
print(ciphertext.hex())

# Bob decrypts
cipher_decrypt = PKCS1_OAEP.new(private_key)

recovered_message = cipher_decrypt.decrypt(ciphertext)

print("\nBob Received:")
print(recovered_message.decode())

print("\nSecure transmission completed successfully.")