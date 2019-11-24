# Author: Davide Pollicino
# Date: 10/09/2019

import random as rand

random_number =  rand.randint(1, 10)
print(random_number)
user_number = 0

while user_number != random_number:
    print("Guess a number between 1 and 10")
    user_number = int(input("Your number:"))

    if user_number < random_number:
        print("To low")
    elif user_number > random_number:
        print("TO high")
    else:
        print("You got it")
        print("See you next time")
