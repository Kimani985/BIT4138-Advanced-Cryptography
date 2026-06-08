import random
import time

print("===== LFSR SIMULATION =====")

state = [1, 0, 1, 1]

sequence = []

for i in range(100):
    new_bit = state[0] ^ state[2]
    sequence.append(state[-1])
    state = [new_bit] + state[:-1]

print("Generated Sequence Length:", len(sequence))

print("\nGenerated Sequence:")
print(sequence)

print("\n===== RANDOMNESS TEST =====")

ones = sequence.count(1)
zeros = sequence.count(0)

print("Number of Ones :", ones)
print("Number of Zeros:", zeros)

ones_percent = (ones / len(sequence)) * 100
zeros_percent = (zeros / len(sequence)) * 100

print(f"Percentage of Ones : {ones_percent:.2f}%")
print(f"Percentage of Zeros: {zeros_percent:.2f}%")

if abs(ones - zeros) <= 10:
    print("Result: Fairly Balanced")
else:
    print("Result: Weak Randomness")

print("\n===== RC4 STYLE SIMULATION =====")

message = "HELLO"

key_stream = [random.randint(1, 255) for _ in message]

encrypted = []

start = time.time()

for i in range(len(message)):
    encrypted.append(ord(message[i]) ^ key_stream[i])

end = time.time()

print("Message:", message)
print("Key Stream:", key_stream)
print("Encrypted:", encrypted)

print("\n===== PERFORMANCE RESULTS =====")
print("Execution Time:", end - start, "seconds")