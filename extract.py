for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("bump-bang")
    elif num % 3 == 0:
        print("bump")
    elif num % 5 == 0:
        print("bang")
    else:
        print(num)
    
