import random

import ansi


# Game constants.
WORD_LENGTH = 5
MAX_GUESSES = 5
WORDS = "words"

# Dialogue constants.
MAKE_GUESS = "Make guess: "
MAKE_GUESS_ERROR = "Guess must be a possible solution, try agian: "
WIN = "You win! Correct word was {}."
LOSE = "No more guesses, you lose! Correct word was {}."

# Constants for functions.
OK = 2
WRONG_PLACE = 1
WRONG = 0

# UI constants.
WIDTH = 101


def read_words(file_name: str) -> list[str]:
    with open(file_name, "r") as file:
        data = [word.lower().strip() for word in file]
    return data


def get_hidden_word(words: list[str]) -> str:
    """Selects a word on random to use as hidden word."""
    return random.choice(words)


def check_guess(guess: str, word: str) -> list[int]:
    """Compares guess to hidden word.

    Status codes returned are:
        OK
            Letter is correct and in correct position.
        WRONG_PLACE
            Letter is correct but in wrong place.
        WRONG
            Letter is wrong.
    """
    letters_in_word = list(word)
    status = []  # Status of letters, OK, WRONG_PLACE or WRONG.

    # Check if letter is in correct spot.
    for letter_in_guess, letter_in_word in zip(guess, word):
        # If letter is in correct slot, mark it as OK and remove it from
        # letters_in_word to not count it again if guess uses the letter
        # two times.
        if letter_in_guess == letter_in_word:
            letters_in_word.remove(letter_in_word)
            status.append(OK)
        else:
            # Else mark it as WRONG for now.
            status.append(WRONG)

    # Check if letter that is not in correct spot is in hidden word.
    for index, (letter_in_guess, letter_status) in enumerate(zip(guess, status)):
        # If letter is not marked as OK, check if it occurs in word at
        # other location, and has not yet been accounted for (either as
        # OK or WRONG_PLACE, i.e. still exists in letters_in_word.).
        if letter_status == WRONG:
            if letter_in_guess in letters_in_word:
                status[index] = WRONG_PLACE
                letters_in_word.remove(letter_in_guess)
    return status


def get_user_input(words: list[str]) -> str:
    """Get guess from user.

    Makes sure guess is any of the possible words.
    """
    guess = input(MAKE_GUESS).lower()
    while guess not in words:
        ansi.clear_rows(2)
        guess = input(MAKE_GUESS_ERROR)
    return guess


def calculate_padding(string_length: int, width: int) -> int:
    """Calculate the padding required to center a string.

    This is used to caluclate the left padding required to center a
    string to a given width.  Function can be used on strings with
    ANSI escape code for example.

    Example:
        String of width 5, total width 10 gives padding of
          (10-1)//2 - (5-1)//2 = 4-2
                               = 2.

        Padding can then be used as follows:

        Input:
            print("-"*10)
            print(" "*2 + "string")
            print("-"*10)

        Output:
            ----------
              string
            ----------
    """
    return (width-1)//2 - (string_length-1) // 2


def draw_board(header: str, guesses: list[str], hidden_word: str) -> None:
    # Head.
    head = ansi.create_color_code(header, ansi.RED_FG)
    heading_padding = calculate_padding(len(header), WIDTH)
    print(" " * heading_padding + head)

    # Guesses.
    padding  = calculate_padding(WORD_LENGTH, WIDTH)
    for guess in guesses:
        row = ""
        guess_result = check_guess(guess, hidden_word)
        for letter, result in zip(guess.upper(), guess_result):
            if result == OK:
                row += ansi.create_color_code(
                    letter,
                    ansi.WHITE_FG,
                    ansi.GREEN_BG,
                )
            elif result == WRONG_PLACE:
                row += ansi.create_color_code(
                    letter,
                    ansi.WHITE_FG,
                    ansi.YELLOW_BG,
                )
            elif result == WRONG:
                row += letter
        print(" " * padding + row)

    # Pad wtih blank rows for guesses not yet made.
    if len(guesses) < MAX_GUESSES:
        for _ in range(MAX_GUESSES - len(guesses)):
            print(("_"*WORD_LENGTH).center(WIDTH))


def main() -> None:
    # Set up game.
    words = read_words(WORDS)
    hidden_word = get_hidden_word(words)
    guesses = MAX_GUESSES
    prev_guesses = []
    guess_nr = 1  # Keep track of round.
    draw_board(f'Welcome to guess the word', prev_guesses, hidden_word)
    
    # Game loop.
    while guesses:
        # Take guess from user.
        guess = get_user_input(words)
        prev_guesses.append(guess)

        # Redraw board and print current state.
        ansi.clear_rows(8)
        guesses -= 1
        if guesses and guess != hidden_word:
            guess_nr += 1  # Only increase round counter if game not ended.
        draw_board(f'Round {guess_nr}', prev_guesses, hidden_word)

        # Check if win.
        if guess == hidden_word:
            print(WIN.format(hidden_word))
            break
    else:
        print(LOSE.format(hidden_word))


if __name__ == "__main__":
    main()
