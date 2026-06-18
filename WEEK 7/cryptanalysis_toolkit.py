while True:

    print("\n===== CRYPTANALYSIS TOOLKIT =====")
    print("1. Difference Analysis")
    print("2. Frequency Analysis")
    print("3. Probability Analysis")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        a = input("First text: ")
        b = input("Second text: ")

        diff = 0

        for i in range(min(len(a), len(b))):
            if a[i] != b[i]:
                diff += 1

        print("Differences:", diff)

    elif choice == "2":

        text = input("Enter text: ").upper()

        frequency = {}

        for char in text:
            if char.isalpha():
                frequency[char] = frequency.get(char, 0) + 1

        print(frequency)

    elif choice == "3":

        success = int(input("Successful outcomes: "))
        total = int(input("Total outcomes: "))

        print("Probability:", success / total)

    elif choice == "4":
        print("Exiting Toolkit...")
        break

    else:
        print("Invalid choice.")