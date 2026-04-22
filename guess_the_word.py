# Laury Flowers
# CIS256 Spring 2026
# Exercise Assignment 4

import random

# list of words
words = ["apple", "banana", "grape", "orange"]

# pick random word
def get_word():
    return random.choice(words)

# check if guess is in word
def check_guess(word, guess):
    return guess in word


def play_game():
    word = get_word()
    guessed = []
    attempts = 6

    print("Guess the word!")

    # This part keeps the game running after attemps are done
    while attempts > 0:
        display = ""

        #this part check each letter in the word 
        for letter in word:
            if letter in guessed:
                display += letter
            else:
                display += "_"

        print(display)

        if display == word:
            print("You win!")
            return

        guess = input("Enter a letter: ")

        if guess in guessed:
            print("You already guessed that letter")
            continue

        guessed.append(guess)

        if check_guess(word, guess):
            print("Correct!")
        else:
            print("Wrong!")
            # if guss is wrong,  lose one attempt
            attempts -= 1

    print("You lost! The word was:", word)


if __name__ == "__main__":
    play_game()
