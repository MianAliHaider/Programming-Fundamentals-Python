rows = int(input('Enter Rows: '))
for i in range(rows):
    for j in range(rows):
        if j == 0 or j == rows - 1:
            print("*", end=" ")
        elif i == j and i >= rows // 2:
            print("*", end=" ")
        elif i + j == rows - 1 and i >= rows // 2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
