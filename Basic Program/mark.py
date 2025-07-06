mark=int(input("Enter your marks:"))
name = input("Enter your name: ")

if(mark>=90 and mark<100):
    grade = "A"

elif(mark>=80 and mark<90):
    grade = "B"

elif(mark>=70 and mark<80):
    grade = "C"

elif(mark>=60 and mark<70):
    grade = "D"

elif(mark>=0 and mark<60):
    grade = "You Fail"

else:
    grade = "You entered a invalid numbers"


print("Your name is", name , "Your final grade is",grade,)