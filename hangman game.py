import random
import time
from collections import Counter

words = '''apple banana mango strawberry  
orange grape pineapple apricot lemon coconut watermelon 
cherry papaya berry peach lychee muskmelon'''

words = words.split(' ')

# Program randomly chooses word from the "words" list
word = random.choice(words)

if __name__ == '__main__':
    print('Guess the word! HINT: word is a name of fruit')

    for i in word:
        # Printing the empty spaces of the word for the user to guess
        print('_', end=' ')
    print()

    # Game state
    playing = True
    # List for storing the letters guessed by the player
    letterGuessed = ''
    chances = len(word) + 2
    correct = 0
    flag = 0
    try:
        while (chances != 0) and flag == 0: # Flag gets updated whenever the word is correctly guessed
            print()
            chances -= 1

            try:
                guess = str(input('Enter a letter to guess: '))
            except:
                print('Enter only a letter!')
                continue

            # Validation
            if not guess.isalpha():
                print('Enter only a LETTER')
                continue
            elif len(guess) != 1:
                print('Enter only a SINGLE letter')
                continue
            elif guess in letterGuessed:
                print('You have already guessed that letter')
                continue

            # If letter is guessed correctly
            if guess in word:
                # K is the placeholder for how many iterations the guessed letter occurs
                k = word.count(guess)
                for _ in range(k):
                    letterGuessed += guess

            # Print the word
            for char in word:
                if char in letterGuessed and (Counter(letterGuessed) != Counter(word)):
                    print(char, end=' ')
                    correct += 1
                # If the player guessed all the letters
                # Once the correct word is guessed fully,
                elif (Counter(letterGuessed) == Counter(word)):
                    print("The word is: ", end=' ')
                    print(word)
                    flag = 1
                    print('Congratulations, You won!')
                    break # Break for loop
                    break # Break while loop
                else:
                    print('_', end=' ')

        # If user has used all of their chances
        if chances == 0 and (Counter(letterGuessed) != Counter(word)):
            print()
            print('You lost! Try again..')
            print('The word is {}'.format(word))

    except KeyboardInterrupt:
        print()
        print('Bye! Try Again.')
        exit()