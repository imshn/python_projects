# import random as rn
# words = ["python", "java", "javascript", "c", "golang", "erlang", "html", "css"]
#
# random_word = rn.choice(words)
# print("Guess the language")
# while True:
#     try:
#         user_choice = input(f"(Hint: It has the length of {len(random_word)} char) ")
#         if user_choice != random_word:
#             print("Opp! Nope you guessed it wrong, try one more time!")
#         else:
#             print(f"Yes, it was correct, the answer is {random_word}")
#             break
#     except ValueError:
#         print("Please enter valid Character")

import random

target_word = random.choice(["python", "java", "javascript", "c", "golang", "erlang", "html", "css"])
print("Guess the language")
print(f"(Hint: It has the length of {len(target_word)} characters)")

max_attempts = 5
attempts = 0

while attempts < max_attempts:
    guess = input("Enter your guess: ")

    if guess == target_word:
        print(f"Correct! The answer is {target_word}")
        break
    else:
        attempts += 1
        print("Incorrect. Try again.")

        if attempts < max_attempts:
            # Provide a hint, e.g., reveal a letter
            hint = target_word[random.randint(0, len(target_word) - 1)]
            print(f"Hint: The word contains the letter '{hint}'")

if attempts == max_attempts:
    print(f"You've reached the maximum number of attempts. The answer was {target_word}")