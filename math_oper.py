n = int(input('Insert number "n": '))

# Factorial
fact = 1

for num in range(1, n + 1):
    fact *= num
print('Factorial of your number "n" is: ', fact)

# Prime number
yes = 'Your number "n" is prime number.'
no = 'Your number "n" is not prime number.'
if n == 1:
    print(no)
elif n == 2 or n == 3 or n == 5 or n == 7:
    print(yes)
elif n % 2 != 0 and n % 3 != 0 and n % 5 != 0 and n % 7:
    print(yes)
else:
    print(no)

# Fibonacci
print('Fibonacci for "n" numbers: ', end="")
a, b = 0, 1
for i in range(n):
    print(b, end=", ")
    a, b = b, a + b
print("...")
