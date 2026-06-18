print("===== FREQUENCY ANALYSIS =====")

text = input("Enter text: ").upper()

frequency = {}

for char in text:
    if char.isalpha():
        frequency[char] = frequency.get(char, 0) + 1

print("\nLetter Frequencies:")

for letter, count in sorted(frequency.items()):
    print(letter, ":", count)
