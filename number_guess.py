# import math
# from random import random
#
# random_num = math.ceil(random()*10)
# while True:
#     user_guess = int(input("Guess the number between 0 to 10 "))
#     if user_guess>random_num:
#         print("Guess lower")
#         continue
#     elif user_guess< random_num:
#         print("Guess Higher")
#         continue
#     if user_guess==random_num:
#         print(f"Yay!!!, Hooray!!!, you guessed it, the ans is {random_num}")
#         break


import math
from random import random

# Constants for range
MIN_VALUE = 0
MAX_VALUE = 10

# Generate random number
random_num = math.ceil(random() * MAX_VALUE)

# Game loop
while True:
    try:
        user_guess = int(input(f"Guess the number between {MIN_VALUE} and {MAX_VALUE}: "))
        if user_guess > random_num:
            print("Too high! Try guessing a lower number.")
        elif user_guess < random_num:
            print("Too low! Try guessing a higher number.")
        else:
            print(f"Yay!!! Hooray!!! You guessed it! The answer is {random_num}.")
            break
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
