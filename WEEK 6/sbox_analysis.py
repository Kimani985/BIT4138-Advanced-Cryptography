print("===== S-BOX ANALYSIS =====")

sbox = {
    0: 14,
    1: 4,
    2: 13,
    3: 1,
    4: 2,
    5: 15,
    6: 11,
    7: 8
}

print("\nS-Box Mappings")

for key, value in sbox.items():
    print(key, "->", value)

outputs = list(sbox.values())

if len(outputs) == len(set(outputs)):
    print("\nNo repeated outputs detected.")
    print("S-Box appears secure.")
else:
    print("\nRepeated outputs detected.")
    print("S-Box may be weak.")