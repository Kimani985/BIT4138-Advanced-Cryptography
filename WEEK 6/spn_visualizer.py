# SPN Visualizer

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

print("===== SPN VISUALIZER =====")

plaintext = input("Enter plaintext digits: ")

print("\nSTEP 1: PLAINTEXT")
print(plaintext)

substituted = ""

for char in plaintext:
    if char in sbox:
        substituted += sbox[char]
    else:
        substituted += char

print("\nSTEP 2: SUBSTITUTION")
print(substituted)

ciphertext = substituted[::-1]

print("\nSTEP 3: PERMUTATION")
print(ciphertext)

print("\nFINAL CIPHERTEXT")
print(ciphertext)