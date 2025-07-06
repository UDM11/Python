def sum_natural_numbers(n):
    if n < 0:
        return 0
    else:
        return n + sum_natural_numbers(n - 1)
    
number = int(input("Enter the number: "))
sum = sum_natural_numbers(number)
print("The sum of natural numbers up to", number, "is", sum)