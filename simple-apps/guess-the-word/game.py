import random
import ansi


# Game constants.
WORD_LENGTH = 5
MAX_GUESSES = 5
WORDS = ["snake", "quake", "makes"]

# Dialogue constants.
MAKE_GUESS = "Make guess: "
MAKE_GUESS_ERROR = "Guess must be 5 letters, make new guess: "

# Constants for functions.
OK = 2
WRONG_PLACE = 1
WRONG = 0

# UI constants.
WIDTH = 101


def get_hidden_word(words: list[str]) -> str:
    return random.choice(words)


def check_guess(guess: str, word: str) -> list[int]:
    return [
        OK if letter_in_guess == letter_in_word
        else WRONG_PLACE if letter_in_guess in word
        else WRONG
        for letter_in_guess, letter_in_word in zip(guess, word)
    ]


def get_user_input() -> str:
    guess = input(MAKE_GUESS).lower()
    while len(guess) != WORD_LENGTH or not guess.isalpha():
        ansi.clear_rows(2)
        guess = input(MAKE_GUESS_ERROR)
    return guess


def calculate_padding(string: str, width: int) -> int:
    return (width-1)//2 - (len(string)) // 2


def draw_board(header: str, guesses: list[str], hidden_word: str) -> None:
    # Head.
    head = ansi.create_color_code(header, ansi.RED_FG)
    padding = calculate_padding(header, WIDTH)
    print(" " * padding + head)

    # Guesses.
    for guess in guesses:
        row = ""
        guess_result = check_guess(guess, hidden_word)
        for letter, result in zip(guess, guess_result):
            if result == OK:
                row += ansi.create_color_code(
                    letter.upper(),
                    ansi.WHITE_FG,
                    ansi.GREEN_BG,
                )
            elif result == WRONG_PLACE:
                row += ansi.create_color_code(
                    letter.upper(),
                    ansi.WHITE_FG,
                    ansi.YELLOW_BG,
                )
            elif result == WRONG:
                row += letter.upper()
        padding = calculate_padding(guess, WIDTH)
        print(" " * padding + row)

    # Pad wtih blank rows for guesses not yet made.
    if len(guesses) < MAX_GUESSES:
        for _ in range(MAX_GUESSES - len(guesses)):
            print(("_"*5).center(WIDTH))


def main() -> None:
    # Set up game.
    hidden_word = get_hidden_word(WORDS)
    guesses = MAX_GUESSES
    prev_guesses = []
    guess_nr = 1  # Keep track of round.
    draw_board(f'Welcome to guess the word', prev_guesses, hidden_word)
    
    # Game loop.
    while guesses:
        # Take guess from user.
        guess = get_user_input()
        prev_guesses.append(guess)

        # Redraw board and print current state.
        ansi.clear_rows(8)
        guesses -= 1
        if guesses and guess != hidden_word:
            guess_nr += 1  # Only increase round counter if game not ended.
        draw_board(f'Round {guess_nr}', prev_guesses, hidden_word)

        # Check if win.
        if guess == hidden_word:
            print("You win!")
            break
    else:
        print("You lose!")


main()
