# Simple SPN Cipher

sbox = {
    "0": "E",
    "1": "4",
    "2": "D",
    "3": "1",
    "4": "2",
    "5": "F",
    "6": "B",
    "7": "8",
    "8": "3",
    "9": "A"
}

plaintext = input("Enter plaintext digits: ")

# Substitution
substituted = ""

for char in plaintext:
    if char in sbox:
        substituted += sbox[char]
    else:
        substituted += char

# Permutation (reverse string)
ciphertext = substituted[::-1]

print("\nSubstituted Text:", substituted)
print("Ciphertext:", ciphertext)