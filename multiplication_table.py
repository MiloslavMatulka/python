inp = int(input("Insert size of multiplication table: "))

size = inp + 1

for number in range(size):
    for multiple in range(size):
        print("{0:4d}".format(number * multiple), end="")
    print(end="\n")
