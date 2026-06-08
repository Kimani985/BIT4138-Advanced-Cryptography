from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

print("===== RSA ENCRYPTION SYSTEM =====")

# Generate RSA key pair
key = RSA.generate(2048)

private_key = key.export_key()
public_key = key.publickey().export_key()

print("\n===== KEY GENERATION =====")
print("Public Key Generated")
print("Private Key Generated")

# Save keys
with open("public.pem", "wb") as pub:
    pub.write(public_key)

with open("private.pem", "wb") as priv:
    priv.write(private_key)

message = "HELLO BIT4138"

print("\nOriginal Message:")
print(message)

# Encrypt using public key
public_key_obj = RSA.import_key(public_key)
cipher_encrypt = PKCS1_OAEP.new(public_key_obj)

encrypted_message = cipher_encrypt.encrypt(message.encode())

print("\n===== PUBLIC KEY ENCRYPTION =====")
print("Encrypted Message:")
print(encrypted_message.hex())

# Decrypt using private key
private_key_obj = RSA.import_key(private_key)
cipher_decrypt = PKCS1_OAEP.new(private_key_obj)

decrypted_message = cipher_decrypt.decrypt(encrypted_message)

print("\n===== PRIVATE KEY DECRYPTION =====")
print("Recovered Message:")
print(decrypted_message.decode())

print("\n===== SECURE MESSAGE TRANSMISSION =====")
print("Alice encrypts with Bob's public key")
print("Bob decrypts with his private key")

print("\n===== RSA VALIDATION =====")

if decrypted_message.decode() == message:
    print("Validation Successful")
else:
    print("Validation Failed")