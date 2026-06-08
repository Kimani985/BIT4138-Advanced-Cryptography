from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import time

print("===== AES ENCRYPTION SYSTEM =====")

# Generate AES key
key = get_random_bytes(16)

print("\nGenerated AES Key:")
print(key.hex())

# Read file
with open("secret.txt", "rb") as file:
    data = file.read()

# Padding
while len(data) % 16 != 0:
    data += b' '

cipher = AES.new(key, AES.MODE_ECB)

start = time.time()

encrypted_data = cipher.encrypt(data)

with open("encrypted.bin", "wb") as file:
    file.write(encrypted_data)

end = time.time()

print("\nFile Encrypted Successfully")

# Decrypt
decrypted_data = cipher.decrypt(encrypted_data)

with open("decrypted.txt", "wb") as file:
    file.write(decrypted_data)

print("File Decrypted Successfully")

print("\nRecovered Text:")
print(decrypted_data.decode())

print("\n===== PERFORMANCE RESULTS =====")
print("Encryption Time:", end - start, "seconds")