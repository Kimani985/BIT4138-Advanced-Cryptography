print("===== DIFFERENCE ANALYSIS =====")

text1 = input("Enter first plaintext: ")
text2 = input("Enter second plaintext: ")

length = min(len(text1), len(text2))

differences = 0

for i in range(length):
    if text1[i] != text2[i]:
        differences += 1

print("\nDifferences Found:", differences)