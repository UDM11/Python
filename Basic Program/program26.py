def sum(n):
    if (n==0):
        return 0
    return sum(n-1)+n
    
n = int(input("The Number is: "))
sum = sum(n)
print(sum)