def average(num1, num2, num3):
    sum = (num1 + num2 + num3)
    subtract = (num1 - num2 - num3)
    multiply = (num1 * num2 * num3)
    divide = (num1 / num2 / num3)
    avg = (num1 + num2 + num3) / 3

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))    
num3 = float(input("Enter the third number: "))
sum = num1 + num2 + num3
print("The sum of the three numbers is:", sum)
subtract = num1 - num2 - num3
print("The subtraction of the three numbers is:", subtract)
multiply = num1 * num2 * num3
print("The multiplication of the three numbers is:", multiply)
divide = num1 / num2 / num3
print("The division of the three numbers is:", divide)
avg = (num1 + num2 + num3) / 3
print("The average is:", avg)