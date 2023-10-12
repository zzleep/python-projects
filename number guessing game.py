import math
import random

lower = int(input("Enter Lower Bound:- "))

upper = int(input("Enter Upper Bound:- "))

# Generation of random numbers between lower and upper bounds

x = random.randint(lower, upper)
print("\n\tYou've only got ",
      round(math.log(upper - lower + 1, 2)),
      " chances to guess the right number!\n")

# Placeholder for guesses
count = 0

# Calculation of minimum number of guesses depends upon range

while count < math.log(upper - lower + 1, 2):
    count += 1

    # Guess inout
    guess = int(input("Guess a number:- "))

    if x == guess:
        print("Congratulations you did it in ",
              count, " try")
        # Once the guess is correct, the loop will break
        break
    elif x > guess:
        print("You guessed too small!")
    elif x < guess:
        print("You guessed too high!")

# If Guessing is more than repaired guesses, it will show this output
if count >= math.log(upper - lower + 1, 2):
    print("\nThe number is %d " % x)
    print("\tBetter Luck Next Time!")