import random

number = random.randint(3, 6)
guess = None

while guess != number:
    guess = int(input("If I have 6 apples and gave Cate 3, how many do I have? "))

    
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("Congratulations! You guessed it.")
