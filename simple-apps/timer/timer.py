import argparse
import time


# Constants
MAX_WIDTH = 20
TIME_MSG = "Time left: {}"
EXIT_MSG = "Time's up!"


def convert(n: int) -> str:
    """Convert seconds to hour:minutes:seconds."""
    hours = n // 3600
    minutes = (n % 3600) // 60
    seconds = n % 60
    
    if hours:
        value = f'{hours}:{minutes:02}:{seconds:02}'
    elif minutes:
        value = f'{minutes:02}:{seconds:02}'
    else:
        value = f'{seconds:02}'

    return value


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="Timer",
        description="Simple count down timer",
    )
    parser.add_argument(
        "seconds",
        metavar="n",
        type=int,
        help="time in seconds",
    )

    args = parser.parse_args()
    n = args.seconds
    while n:
        print(TIME_MSG.format(convert(n)), end="\r")
        time.sleep(1)
        print(" "*MAX_WIDTH, end="\r")
        n -= 1
    else:
        print(EXIT_MSG)


if __name__ == "__main__":
    main()

