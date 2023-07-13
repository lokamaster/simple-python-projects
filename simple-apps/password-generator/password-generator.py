import secrets 
import string

# Shell text.
GET_LENGTH = "Enter length of password: "
SPACE = "Shall password contain a space? y/n: "
RESULT = "\nYour generated password is:"

# Errors.
LENGHT_ERROR = "Error: Min length of password is {}."
NUMERIC_ERROR = "Must be an integer."

# Character constants.
WHITESPACE = " "
LOWER = string.ascii_lowercase
UPPER = string.ascii_uppercase
DIGIT = string.digits
PUNCTUATION = string.punctuation
ALL = LOWER + UPPER + DIGIT + PUNCTUATION

# Other constants.
MIN_LENGTH = 4
RNG = secrets.SystemRandom()  # rng-generator.
YES = "y"


def generate_password(
        length: int,
        space: bool = False,
        rng:secrets.SystemRandom = RNG
)-> str:
    """Generate password of given length.

    Password will consist of at least one of each from the following:
        - Uppercase letter
        - Lowercase letter
        - Digit
        - Special characet (#, !, ?, etc.)
        - Whitespace (" ") if flag is set

    Password will then be padded out with random characters to reach the
    given length.

    Parameters:
        length : int
            Lenght of password.
        space : bool
            Flag to control if password shall contain space or not.
        rng : secrets.SystemRandom
            RNG-class to control rng.

    Returns:
        password : str 
            A string of the generated passowrd

    Raises:
        ValueError
            If lenght is shorter than 4, or 5 with space.
    """
    if length < MIN_LENGTH + space:
        raise ValueError(LENGHT_ERROR.format(MIN_LENGTH + space))

    # Generate password
    password = (
            [rng.choice(LOWER),
             rng.choice(UPPER),
             rng.choice(DIGIT),
             rng.choice(PUNCTUATION)]
            + ([WHITESPACE] if space else [])
            + rng.choices(ALL, k=length - (MIN_LENGTH + space))
    )
    
    # Shuffle password and make sure whitespace is not last.
    rng.shuffle(password)
    while password[-1] == WHITESPACE:
        rng.shuffle(password)

    # Make string and return.
    return "".join(password)


def main() -> None:
    # Get password length from user.
    while not (length := input(GET_LENGTH).strip()).isnumeric():
        print(NUMERIC_ERROR)
    else:
        length = int(length)
    
    # Ask if password shall contain space.
    space = True if input(SPACE).lower().strip() == YES else False
    
    # Generate password.
    try:
        password = generate_password(length, space)
    except ValueError as error:
        print(error)
    else:
        print(RESULT)
        print(password)


if __name__ == "__main__":
    main()

