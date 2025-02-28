import random
import time

print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 10")
time.sleep(2)
guess = int(input("What is your guess? "))
time.sleep(1)
correct_number = random.randint(1, 10)
guess_count = 1

while guess != correct_number:
    guess_count += 1
    if guess < correct_number:
        guess = int(input("Nope. Try again. Your guess is too low: "))
    else:
        guess = int(input("Nope. Try again. Your guess is too high: "))

print("You got it!" + " It took you " + str(guess_count) + " tries.")
