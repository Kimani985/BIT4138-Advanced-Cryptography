print("===== AVALANCHE EFFECT ANALYZER =====")

text1 = input("Enter first text: ")
text2 = input("Enter second text: ")

length = min(len(text1), len(text2))

differences = 0

for i in range(length):
    if text1[i] != text2[i]:
        differences += 1

percentage = (differences / length) * 100

print("\nRESULTS")
print("Differences:", differences)
print("Percentage Changed:", round(percentage, 2), "%")