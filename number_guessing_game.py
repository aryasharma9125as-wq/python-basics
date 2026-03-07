import random
number = random.randrange(1,20)
guess = 0

print ("i am thinking of a number from1 to 20.")

while guess != number:
    guess = int(input("take a guess:"))
    if guess>number:
            print("guess",guess)
            print("too high!")
    elif number>guess:
            print("Guess",guess)
            print("too low!")
    else:
            print("correct! you guessed it!")
