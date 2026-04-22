# Laury Flowers
# CIS256 Spring 2026
# Exercise Assignment 4

# importing from main file
from guess_the_word import get_word, check_guess, words


# test if word comes from list
def test_word_from_list():
    word = get_word()
    assert word in words


# test correct guess
def test_correct_guess():
    word = "apple"
    assert check_guess(word, "a") == True


# test wrong guess
def test_wrong_guess():
    word = "apple"
    assert check_guess(word, "z") == False
