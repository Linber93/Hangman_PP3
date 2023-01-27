"""
Hangman

1 When use starts game, computer chooses a random
 word from a list within a google sheet

2 computer show dashes that represents letters in the word

3 User will get a chanse to guess 1 letter at the time.
    - If they enter something thats not a letter, print an error
      and prompt the user to try again

    - If they've guessed the letter before, tell them that the
      letter has already been guessed and give them another chance


    - If they guess a letter the haven't guessed before, check whether it's
      in the word. and reveal it.

    show the list of words they have guessed previously

4 Repeat 3 until the game is over. Game is over whne:
    - Word is guessed -- tell them they've won
    -They've reached a preset number of failures
"""
import sys
import random
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
WORD_LIBRARY = GSPREAD_CLIENT.open('word_library')

worksheet = WORD_LIBRARY.worksheet('words')
# WORD_LIBRARY = ['computer', 'windows', 'skynet', 'monitor', 'elevator']

all_words = worksheet.get_all_values()


ALLOWED_INCORRECT_ANSWERS = 8


def get_word():
    """
    Get a Random word from the Word library and returns it
    """
    word = random.choice(all_words)[0]
    return word.upper()


def get_user_input(message):
    """
    """

    user_input = input(message + "\n").strip()

    if user_input == "quit":
        sys.exit()

    return user_input


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
        user_guess = get_user_input('\nGuess a letter.')

        if len(user_guess) > 1 or not user_guess.isalpha():
            print('Please enter a single letter.')
            continue

        if user_guess in guessed_letters:
            print('You\'ve guessed that already')
            continue

        break

    return user_guess


def main_menu():
    """
    Display a welcome message to allow the user to first see instructions
    or skip to start the game
    """
    print('Welcome to a friendly game of Hangman!\n')
    while True:
        instructions = get_user_input('would you want to see the instructions '
                                      'before we start?(y/n)').lower()
        if instructions == 'y':
            display_instructions()
            while True:
                continue_to_game = get_user_input('would you like to start '
                                                  'the game?(y/n)').lower()
                if continue_to_game == 'y':
                    play_game()
                    break
                elif continue_to_game == 'n':
                    print('See you later!')
                    exit()
                else:
                    print("Invalid innput, please enter 'y' or 'n'")
        elif instructions == 'n':
            while True:
                continue_to_game = get_user_input('would you like to start '
                                                  'the game?(y/n)').lower()
                if continue_to_game == 'y':
                    play_game()
                    break
                elif continue_to_game == 'n':
                    print('See you later!')
                    exit()
                else:
                    print("Invalid input, please enter 'y' or 'n'")


def display_instructions():
    """
    Displays rules and instructions on how the game is played
    """
    print('\nWelcome to the game of Hangman!\n')
    print('The aim of the game is to guess the word chosen by the computer.\n')
    print('You will be prompted to guess a letter one at a time.\n')
    print('If the letter is in the word, it will be revealed.\n')
    print('If the letter is not in the word, you will lose a chance.\n')
    print('You have a total of 8 chances to guess the word.\n')
    print('After each guess, a list will show your previously'
          'guessed letters.\n')
    print('The game ends when you either successfully guess the word'
          'or when you run out of tries\n')
    print('Good luck!\n')


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


def play_game():
    """
    This function is responsible for running the game logic of the Hangman
    game. It does the following:

    1. Selects a random word from a predefined list of words.

    2. Displays the word in a dashed format, with letters that have
       been guessed correctly revealed.

    3. Prompts the user to guess a letter, validates the input,
       and keeps track of the guessed letters.

    4. If the letter is in the word, it is revealed, otherwise
       the user loses a chance.

    5. The game ends when the user either successfully guesses
       the word or runs out of chances.

    6. If the user wins, it displays a message of congratulations,
       otherwise a message of failure.

    7. Prompts the user to play again.
    """

    word = get_word()
    num_unique_letters_in_word = len(set(word))

    incorrect_tries = 0
    guessed_letters = []
    correct_guesses = set()

    game_won = False

    display_dashed_word(word, correct_guesses)

    while (incorrect_tries < ALLOWED_INCORRECT_ANSWERS) and not game_won:
        guessed_letter = get_user_guess(guessed_letters)

        if guessed_letter not in word:
            incorrect_tries += 1
            tries_left = ALLOWED_INCORRECT_ANSWERS - incorrect_tries
            print(f'\n\n Incorrect, you have {tries_left} tries left. ' +
                  'try again.')

        if guessed_letter in word:
            correct_guesses.add(guessed_letter)

        guessed_letters.append(guessed_letter)

        display_dashed_word(word, guessed_letters)
        print(f'\nyou have guessed: {guessed_letters}')

        if len(correct_guesses) == num_unique_letters_in_word:
            game_won = True

    if game_won:
        print('You made it')

    else:
        print('You failed')
    play_again()


def play_again():
    """
    once the game has reached the end. the user gets asked if they
    would like to play again
    """
    response = get_user_input('Would you like to play again? (y/n)').lower()
    if response == "y":
        main()
    elif response == "n":
        print("Thanks for playing!")
        exit()
    else:
        print('Invalid response. Please enter "y" or "n".')


def main():

    main_menu()
    """
    word = get_word()
    num_unique_letters_in_word = len(set(word))

    incorrect_tries = 0
    guessed_letters = []
    correct_guesses = set()

    game_won = False

    display_dashed_word(word, correct_guesses)

    while (incorrect_tries < ALLOWED_INCORRECT_ANSWERS) and not game_won:
        guessed_letter = get_user_guess(guessed_letters)

        if guessed_letter not in word:
            incorrect_tries += 1
            tries_left = ALLOWED_INCORRECT_ANSWERS - incorrect_tries
            print(f'\n\n Incorrect, you have {tries_left} tries left. ' +
                  'try again.')

        if guessed_letter in word:
            correct_guesses.add(guessed_letter)

        guessed_letters.append(guessed_letter)

        display_dashed_word(word, guessed_letters)
        print(f'\nyou have guessed: {guessed_letters}')

        if len(correct_guesses) == num_unique_letters_in_word:
            game_won = True

    if game_won:
        print('You made it')

    else:
        print('You failed')
    play_again()
    """


main()
