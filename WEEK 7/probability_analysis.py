print("===== PROBABILITY ANALYSIS =====")

successful = int(input("Enter successful outcomes: "))
total = int(input("Enter total outcomes: "))

probability = successful / total

print("\nProbability =", round(probability, 4))
print("Percentage =", round(probability * 100, 2), "%")