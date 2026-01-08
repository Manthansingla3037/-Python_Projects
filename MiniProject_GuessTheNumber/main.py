import random

n = random.randint(1,100)
guess = 0
a = -1

while(a!=n):
    guess += 1
    a = int(input("Guess the number...\n"))

    if(a>n):
        print("Please enter the smaller number...")
    else:
        print("Please enter the greater number...")

print(f"Congratulation!,You guessed the correct number in {guess} attempt")