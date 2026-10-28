
size = int(input("Enter the size of the pattern: "))

for i in range(size):
    for j in range(size):
        if i + j == size or i == j:
            print("*", end="")
        else:
            print(" ", end="")
    print()


