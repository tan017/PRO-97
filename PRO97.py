import random 
number=random.randint(1,9)
chances=0
print("Guess a number between 1 and 9")
while chances <5:
    guess=int (input("enter your guess:"))
    if guess==number:
        print("Congratulation! That is the right number.")
        break
    elif guess<number:
        print("Uh oh!The number you guessed is lower than the correct number.")
    else:
        print("No, the number you chose is greater than the actual number.")
    chances=chances+1
if chances>5:
    print("You Lose, the correct number is ", number )