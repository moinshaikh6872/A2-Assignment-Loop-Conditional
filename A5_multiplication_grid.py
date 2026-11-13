size = int(input("Enter the grid size (e.g., 10): "))

for i in range(1, size + 1):
    for j in range(1, size + 1):
        # Format the output for a neat grid
        print(f"{i * j:4}", end="")
    print()
