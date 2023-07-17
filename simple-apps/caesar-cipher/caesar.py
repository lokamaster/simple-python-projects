import argparse
import string


LOWER = string.ascii_lowercase
UPPER = string.ascii_uppercase
NUM_OF_LETTERS = 26


def get_translation(rot: int) -> dict[str, str]:
    """Creates a translation table with certain rotation of the alphabet.

    See cipher for details.
    """
    lower = {
        l: LOWER[(LOWER.index(l) + rot) % NUM_OF_LETTERS]
        for l in LOWER
    }
    upper = {
        l: UPPER[(UPPER.index(l) + rot) % NUM_OF_LETTERS]
        for l in UPPER
    }
    return str.maketrans(dict(**lower, **upper))


def cipher(message: str, rot: int) -> str:
    """Caesar cipher of message.

    Casear cipher method replaces all letter by the one that is n places
    further down in the alphabet.  If alphabet reaches the end you start
    counting from A again.  n is given by rot.

    Example: "Zero" with rotation of 3
        Z -> A B C
        e -> f g h
        r -> s t u
        o -> p q r
    "Zero" therefore becomes "Chur" after a rotation of 3.

    Decipher can be made by giving a negative integer to rot.
    """ 
    translation = get_translation(rot)
    new_message = [string.translate(translation) for string in message]
    return "".join(new_message)


def decipher(message: str, rot: int) -> str:
    """Wrapper function for deciphering, see cipher for details."""
    return cipher(message, -rot)

    
def main() -> None:
    # Create parser.
    parser = argparse.ArgumentParser(
        prog="cipher",
        description="Cipher a message using Casesar cipher algorithm."
    )
    parser.add_argument(
        "message",
        nargs="+",
        help="message to be ciphered",
    )
    parser.add_argument(
        "rot",
        nargs=1,
        help="rotation to use",
        type=int,
    )
    parser.add_argument(
        "-d", "--decipher",
        action="store_const",
        dest="operator",
        const=decipher,
        default=cipher,
        help="decipher message",
    )
    
    # Get arguments.
    args = parser.parse_args()
    rot = args.rot[0]
    message = []
    for m in args.message:
        message.append(args.operator(m, rot))
    print(" ".join(message))

if __name__ == "__main__":
    main()

