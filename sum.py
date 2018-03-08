num1 = int(input("Insert number 1 of 3: "))
num2 = int(input("Insert number 2 of 3: "))
num3 = int(input("Insert number 3 of 3: "))

sum = num1 + num2 + num3

if sum > 10:
    print("The sum of your numbers is > 10, the sum is {}.".format(sum))
else:
    print("The sum of your numbers is < 10, the sum is {}.".format(sum))
