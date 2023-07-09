import math
import random
import sys


PHRASES = {
        "intro": (
            "Hi! Welcome to guess the number\n"
            "In this game you try to find the secret number!"
        ),
        "choice": "Please choose an upper bound for the number: ",
        "guess": "Make a guess: ",
        "guess_low": "Your guess is too low!",
        "guess_high": "Your guess is too high!",
        "domain_error": "Choice must be above 0.",
        "numeric_error": "Must be an integer!",
        "victory": "You guessed the correct number, you win!",
        "loss": "You have no more guesses remaining, you lose! :(",
}


def get_integer(phrase: str) -> int:
    """Get integer from user."""
    while not (user_input := input(phrase).strip()).isnumeric():
        print(PHRASES["numeric_error"])
    return int(user_input)


def game(intro: bool = True) -> None:
    """Run the game. Intro phrase can be switched off."""
    if intro:
        print(PHRASES["intro"])

    # Get upper bound for secret number, range will be [0, upper bound].
    while (upper_bound := get_integer(PHRASES["choice"])) < 1:
        print(PHRASES["domain_error"])

    # Initiate secret_number
    secret_number= random.randint(0, upper_bound)

    # Binary search can find number in log_2(n) guesses.
    guesses = math.ceil(math.log2(upper_bound))

    # Game loop
    print(f'Starting game! The secret number is between 0 and {upper_bound}!')
    while guesses:
        print(f'You have {guesses} guesses left.\n')
        guess = get_integer(PHRASES["guess"])
        if guess == secret_number:
            print(PHRASES["victory"])
            break
        elif guess < secret_number:
            print(PHRASES["guess_low"])
        else:
            print(PHRASES["guess_high"])
        guesses -= 1
    else:
        # No more guesses.
        print(PHRASES["loss"])
    # Reveal the hidden number.
    print(f'The hidden number was {secret_number}.')


def main() -> None:
    play = True
    intro = True
    while play:
        game(intro)
        play_again = input("Want to play again? y/n: ")
        if play_again.lower().strip() == "n":
            play = False
        print()
        intro = False  # Disables intro for further rounds.


if __name__ == "__main__":
    main()

