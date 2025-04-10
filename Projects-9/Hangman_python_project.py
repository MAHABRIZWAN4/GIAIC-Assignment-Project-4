import random
stages = ['''
    --------
    |       |
    |
    |
    |
    |
    --------
''',
'''
    --------
    |       |
    |       O
    |
    |
    |
    --------
''',
'''
    --------
    |       |
    |       O
    |       |
    |
    |
    --------
''',
'''
    --------
    |       |
    |       O
    |      /|
    |
    |
    --------
''',
'''
    --------
    |       |
    |       O
    |      /|\\
    |      
    |
    --------
''',
'''
    --------
    |       |
    |       O
    |      /|\\
    |      /
    |
    --------
''',
'''
    --------
    |       |
    |       O
    |      /|\\
    |      / \\
    |
    --------
'''
]



words = ["apple","banana","grapes","orange","pinapple","strawberry","mango","kiwi","peach","watermelon","pear"]


choose_words = random.choice(words)

word_display = ['_'for _ in choose_words]
guess_letters = []
lives = len(stages)-1


print("WELCOME TO HANGMAN!!")
print("GUESS THE FRUITS WORD!!")

while True:
    print(" ".join(word_display))
    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a valid letter.")
        continue


    if guess in guess_letters:
        print("You already guessed that letter.Try Again.\n")
        continue

    guess_letters.append(guess)

    if guess in choose_words:
        print(f"Good guess! '{guess}' is in the word.")
        for index, letter in enumerate(choose_words):
            if letter == guess:
                word_display[index] = guess
    else:
        print(f"Sorry, '{guess}' is not in the word.")
        print(stages[len(stages) - lives -1])
        lives -= 1
        print(f"You have {lives} lives left🎃")


        if lives == 0:
            print(stages[lives])
            print(f"You Lose! The word was '{choose_words}'")
            break


