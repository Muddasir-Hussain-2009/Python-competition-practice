rows = 5
cols = 5

for i in range(rows):

    # Print P
    for j in range(cols):
        if j == 0 or (i == 0 and j < cols - 1) or (i == rows // 2 and j < cols - 1) or (j == cols - 1 and i < rows // 2):
            print("*", end="")
        else:
            print(" ", end="")

    print("  ", end="")

    # Print G
    for j in range(cols):
        if (i == 0 or i == rows - 1) and j > 0 or j == 0 and i > 0 and i < rows - 1 or (j == cols - 1 and i >= rows // 2) or (i == rows // 2 and j >= cols // 2):
            print("*", end="")
        else:
            print(" ", end="")

    print("  ", end="")

    # Print C
    for j in range(cols):
        if (i == 0 or i == rows - 1) and j > 0 or j == 0 and i > 0 and i < rows - 1:
            print("*", end="")
        else:
            print(" ", end="")

    print()
