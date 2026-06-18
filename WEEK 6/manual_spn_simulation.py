print("===== MANUAL SPN SIMULATION =====")

sbox = {
    "0000": "1110",
    "0001": "0100",
    "0010": "1101",
    "0011": "0001"
}

binary = input("Enter a 4-bit binary number: ")

# Round 1 - Substitution
substituted = sbox.get(binary, binary)

# Round 1 - Permutation
permuted = substituted[2] + substituted[3] + substituted[0] + substituted[1]

# Round 2 - Substitution
substituted2 = sbox.get(permuted, permuted)

# Round 2 - Permutation
permuted2 = substituted2[2] + substituted2[3] + substituted2[0] + substituted2[1]

print("\nRound 1 Substitution:", substituted)
print("Round 1 Permutation :", permuted)

print("\nRound 2 Substitution:", substituted2)
print("Round 2 Permutation :", permuted2)

print("\nFinal Output:", permuted2)