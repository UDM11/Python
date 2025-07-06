def factorial(n):
    if n == 0 or n == 1:
        # Base case: factorial of 0 or 1 is 1
        return 1
    else:
        return n * factorial(n - 1)
    
number = int(input("Enter the number: "))
fact = factorial(number)
print("The factorial of", number, "is", fact)