message = "HELLO"
shift = 3

encrypted = ""

for char in message:
    encrypted += chr(ord(char) + shift)

print("Original:", message)
print("Encrypted:", encrypted)