def compare_integers():
    num1 = int(input("Enter first integer: "))
    num2 = int(input("Enter second integer: "))
    if num1 > num2:
        print(f"{num1} is greater than {num2}.")
    elif num1 < num2:
        print(f"{num1} is less than {num2}.")
    else:
        print(f"{num1} is equal to {num2}.")
compare_integers()
