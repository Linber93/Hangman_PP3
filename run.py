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
    return word.upper()


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


def display_dashed_word(word, letters_to_reveal):
    """
    Given a word, print a dashed representation of it.

    Letters that should be shown are provided in the second argument. If a
    a letter in the word is not on that list, it'll be represented by a dash.

    Args:
        word: str - The word to print.
        letters_to_reveal: list of str - List of letters in the word to show.
    """
    dashed_word = ''

    for letter in word:
        if letter in letters_to_reveal:
            dashed_word += f' {letter}'
        else:
            dashed_word += ' _'
    print(dashed_word)
    

def play_again():
    response = input('Would you like to play again? (y/n)\n').strip().lower()
    if response == "y":
        main()
    elif response == "n":
        print("Thanks for playing!")
        return
    else:
        print('Invalid response. Please enter "y" or "n".')
        play_again()


def main():

    word = get_word()
    num_unique_letters_in_word = len(set(word))

    incorrect_tries = 0
    guessed_letters = set()
    correct_guesses = []

    game_won = False

    display_dashed_word(word, correct_guesses)

    while (incorrect_tries <= ALLOWED_INCORRECT_ANSWERS) and not game_won:
        guessed_letter = get_user_guess(guessed_letters)

        if guessed_letter not in word:
            incorrect_tries += 1 

        if guessed_letter in word:
            correct_guesses.append(guessed_letter)

        guessed_letters.add(guessed_letter)

        display_dashed_word(word, guessed_letters)
        print(f'you have guessed: {guessed_letters}')

        if len(correct_guesses) == num_unique_letters_in_word:
            game_won = True

    if game_won:
        print('You made it')

    else: 
        print('You failed')
    play_again()


main()