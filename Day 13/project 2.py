#guessing game
'''
#this is basic level
secret_word = "Titanic"
guess = ""

while guess != "Titanic":
    guess = input("Enter a guess: ")

print(f"Congrats! You have guessed the word {guess} correctly.")
'''
'''
#Intermediate level
secret_word = "Titanic"
guess = ""
guess_limit = 3
guess_count = 1
out_of_guess = False

while guess != secret_word and not out_of_guess:
    if guess_count <= guess_limit:
        guess = input("Enter a guess: ")
        guess_count += 1
    else:
        out_of_guess = True

if guess == secret_word:
    print(f"Congrats! You have guessed the word {guess} correctly.")
else:
    print("out of guesses")
'''

#Advance level
import random

guess_words = ["Titanic", "Day after tomorrow", "Avatar", "Avengers", "Star wars"]
secret_word = guess_words[0]
guess = ""
guess_limit = 3
guess_count = 1
out_of_guess = False


def guess_game(guess):
    random_guess = random.randint(guess_words)

    while guess != secret_word:
        if guess_count <= guess_limit:
            gues = input("Enter a guess: ")
            guess_count =  guess_count + 1

        else:
            out_of_guess = True

if guess == secret_word:
    print(f"Congrats! You have guessed the word {guess} correctly.")
else:
    print("out of guesses")            

#will complete this later as I need to understand import module first
