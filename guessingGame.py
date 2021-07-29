import random

number = random.randint(1,9)
chances = 0
while chances < 5:
    guess = int(input("enter your guess"))

    if guess == number:
        print("you won")
        break
    chances = chances + 1
    if not chances > 5:
        print("you lose the number is ",number )