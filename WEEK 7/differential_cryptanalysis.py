print("===== DIFFERENTIAL CRYPTANALYSIS =====")

text1 = input("Enter plaintext 1: ")
text2 = input("Enter plaintext 2: ")

length = min(len(text1), len(text2))

differences = []

for i in range(length):
    if text1[i] != text2[i]:
        differences.append(i)

print("\nPositions with differences:", differences)
print("Total Differences:", len(differences))