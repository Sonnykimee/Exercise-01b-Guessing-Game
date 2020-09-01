'''
Now you get 3 chances, the program will tell you whether your guess is low or high.
But also the range of has extended.
'''

import sys, random
assert sys.version_info >= (3,8), "This script requires at least Python 3.8"

life = 3
number = random.randrange(1, 20)

print("[Your Life: " + str(life) + "]")

run = True
while run:
    try:
        guess = int(input("Guess a number from 1 to 20: "))

        if guess >= 1 and guess <= 20:
            if guess == number:
                print("\nGreat job! You got it!")
                run = False
            else:
                life -= 1

                if life > 0:
                    if (guess > number):
                        print("Your guess is too big. Try a smaller number!\n")
                        print("[Your Life: " + str(life) + "]")
                    else:
                        print("Your guess is too small. Try a bigger number!\n")
                        print("[Your Life: " + str(life) + "]")
                else:
                    print("\n[Your Life: " + str(life) + "]")
                    print("Sorry, better luck next time.")
                    print("The number was " + str(number))
                    run = False
        else:
            print("Please enter a number in the boundary of 1 to 20! Try again!\n")
    except ValueError:
        print("Please enter an integer! Try again!\n")

print("Game End.")