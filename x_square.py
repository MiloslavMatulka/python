size = int(input("Insert size of square: "))

for row in range(size):
    if row != 0 and row != size - 1:
        print("X " + "  " * (size - 2) + "X ")
    else:
        print("X " * size)
