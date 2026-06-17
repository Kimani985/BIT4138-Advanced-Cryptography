import random

print("===== RANDOMNESS CHALLENGE GAME =====")

# Ask user for sequence length
length = int(input("Enter sequence length: "))

# Generate random binary sequence
sequence = [random.randint(0, 1) for _ in range(length)]

print("\nSequence Generated Successfully!")

# User guess
guess = int(input("Guess how many 1's are in the sequence: "))

# Count ones and zeros
ones = sequence.count(1)
zeros = sequence.count(0)

print("\n===== RESULTS =====")
print("Generated Sequence:")
print(sequence)

print("\nNumber of Ones :", ones)
print("Number of Zeros:", zeros)

if guess == ones:
    print("\n🎉 Congratulations! Your guess was correct.")
else:
    print("\n❌ Wrong guess.")
    print("Difference:", abs(guess - ones))

# Calculate percentages
ones_percent = (ones / length) * 100
zeros_percent = (zeros / length) * 100

print("\n===== RANDOMNESS ANALYSIS =====")
print(f"Percentage of Ones : {ones_percent:.2f}%")
print(f"Percentage of Zeros: {zeros_percent:.2f}%")

print("\nProgram Completed Successfully.")