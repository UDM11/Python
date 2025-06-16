import random

target = random.randint(1, 100)

while True:
    guess = int(input("Guess the number (between 1 and 100): "))
    
    if guess < target:
        print("Too low! Try again.")
    elif guess > target:
        print("Too high! Try again.")
    else:
        print("Congratulations! You've guessed the number.")
        break

print("---------Game Over!---------")
print("Thanks for playing!")