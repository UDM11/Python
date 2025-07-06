number = int(input("Enter the number: "))
fact = 1
i = 1
while(i <= number):
    fact *= i
    i += 1
print("The factorial of", number, "is", fact)