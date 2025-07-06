number = [1, 2, 3, 2, 1, 3]
number.copy()
number.reverse()
if (number == number.reverse()):
    print("The list is palindrome")
else:
    print("The list is not palindrome")