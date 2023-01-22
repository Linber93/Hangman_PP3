"""
Hangman

1 When use starts game, computer chooses a random word from a list

2 computer will display dasches representing the word

3 User will get a chanse to guess 1 letter at the time.
    - If they enter something thatäs not a letter, print an error
      and prompt the user to try again
    - If they've guessed the letter earlier, tell them that the
      letter has already been guessed and give them another chance
    - If they guess a letter the haven't guessed before, check whether it's
      in the word. and reveal it.

    show the list of words they have guessed previously

4 Repeat 3 until the game is over. Game is over whne:
    - Word is guessed -- tell them they've won
    -They've reached a preset number of failures
"""

import random

WORD_LIBRARY = ['computer', 'windows', 'skynet', 'monitor', 'elevator']

ALLOWED_INCORRECT_ANSWERS = 8


def get_word():
    """
    Get a Random word from the Word library and returns it
    """
    word = random.choice(WORD_LIBRARY)
    return word


def get_user_guess(guessed_letters):
    """
    Prompt the user to guess a letter and validate it.

    Validation rules:
      - Input should be a single letter from the Roman alphabet.
      - Input should not have been guessed previously.

    Cleanup:
      - Input is converted to uppercase.
      - Input is stripped from whitespace.

    Args:
      guessed_letters: set of str - leters that the user has guessed already.
    """

    while True:
        user_guess = input('\nGuess a letter.\n').strip().upper()

        if len(user_guess) > 1 or not user_guess.isalpha():
            print('Please enter a single letter.')
            continue

        if user_guess in guessed_letters:
            print('You\'ve guessed that already')
            continue

        break

    return user_guess


guessed_letters = []

get_word()
get_user_guess(guessed_letters)
