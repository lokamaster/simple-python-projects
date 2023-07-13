import math
import random
import sys


# Strings used in game
INTRO = (
        "Hi! Welcome to guess the number\n"
        "In this game you try to find the secret number!"
)
CHOICE = "Please choose an upper bound for the number: "
GUESS ="Make a guess: "
GUESS_LOW = "Your guess is too low!"
GUESS_HIGH = "Your guess is too high!"
VICTORY = "You guessed the correct number, you win!"
LOSS = "You have no more guesses remaining, you lose! :("

# Game strings used with .format
START = "Starting game! The secret number is between {} and {}!"
GUESSES_LEFT = "You have {} guesses left.\n"
REVEAL_SECRET = "The hidden number was {}."

# Strings for replay
NEW_GAME = "Starting new game\n"
PLAY_AGAIN = "You want to play again? y/n: "
YES = ["y", "yes"]
NO = ["n", "no"]
EXIT = "Quitting game . . ."

# Error strings
DOMAIN_ERROR = "Choice must be above 1."
NUMERIC_ERROR = "Must be an integer!"
YES_NO_ERROR = "Please answer (y)es or (n)o."

# Other
MIN_LOWER_BOUND = 1
MIN_UPPER_BOUND = 2


def get_input(phrase: str) -> str:
    """Wrapper function to simplify formatting user input."""
    return input(phrase).strip().lower()


def get_integer(phrase: str) -> int:
    """Get integer from user."""
    while not (user_input := get_input(phrase)).isnumeric():
        print(NUMERIC_ERROR)
    return int(user_input)


def game(intro: bool = True) -> None:
    """Run the game. Intro phrase can be switched off."""
    if intro:
        print(INTRO)

    # Get upper bound for secret number, range will be [1, upper bound].
    while (upper_bound := get_integer(CHOICE)) < MIN_UPPER_BOUND:
        print(DOMAIN_ERROR)

    # Initiate secret_number
    secret_number= random.randint(MIN_LOWER_BOUND, upper_bound)

    # Binary search can find number in log_2(n) guesses.
    guesses = math.ceil(math.log2(upper_bound))

    # Game loop
    print(START.format(MIN_LOWER_BOUND, upper_bound))
    while guesses:
        print(GUESSES_LEFT.format(guesses))
        guess = get_integer(GUESS)

        if guess == secret_number:
            print(VICTORY)
            break
        elif guess < secret_number:
            print(GUESS_LOW)
        else:
            print(GUESS_HIGH)
        guesses -= 1
    else:
        # No more guesses.
        print(LOSS)

    # End of game, reveal secret number
    print(REVEAL_SECRET.format(secret_number))


def main() -> None:
    play = True
    intro = True
    while play:
        game(intro)

        # Ask if player want to play again
        while (play_again := get_input(PLAY_AGAIN)) not in YES + NO:
            print(YES_NO_ERROR)

        # If no: break, otherwise player again
        if play_again in NO:
            print(EXIT)
            play = False
        else:
            print(NEW_GAME)
            intro = False  # Disables intro for further rounds.


if __name__ == "__main__":
    main()

