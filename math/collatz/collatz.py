INT_GET = "Enter an integer greater than zero: "
INT_ERROR = "Bad input, try again."
OUTPUT = "Series ended in {} steps.\nMax value: {}"


def collatz(n: int) -> int:
    """Returns next value for n in the Collatz series.

    Note: This function does not use the "shortcut" of 
    (3n + 1) / 2 if n is odd.
    """
    return n // 2 if n % 2 == 0 else 3*n + 1


def collatz_series(n: int) -> tuple[int, int]:
    """Calculates steps and max value for the Collatz series of n.

    Returns a tuple with with the order (steps, max value).
    """
    steps = 0
    max_val = n
    
    while n > 1:
        n = collatz(n)
        if n > max_val:
            max_val = n
        steps += 1

    return (steps, max_val)


def get_integer(msg: str = INT_GET) -> int:
    """Get integer from stdin."""
    while not (integer := input(msg).strip()).isnumeric():
        print(INT_ERROR)
    return int(integer)


def main():
    n = get_integer()
    steps, max_val = collatz_series(n)
    print(OUTPUT.format(steps, max_val))


if __name__ == "__main__":
    main()

