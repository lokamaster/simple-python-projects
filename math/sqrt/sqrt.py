import sys


TOLERANCE = 0.001  # Precision of the sqrt
MIN_ARG = 2  # Smallest amount of arguments for sys.argv
ERROR = "Please enter a numeric value"
RESULT = "{0:.2f}"


def sqrt(n: float) -> float:
    guess = n / 2
    while abs(guess * guess - n) > TOLERANCE:
        # Improve guess via Newtons method.
        new_guess = guess - (guess*guess - n) / (2*guess)

        # Check if value converge to some limit, if not break.
        if abs(guess*guess - n) < abs(new_guess*new_guess - n):
            guess = float("nan")
            break
        else:
            guess = new_guess
    return guess


def main() -> None:
    if len(sys.argv) >= MIN_ARG:
        n = sys.argv[1]
        try:
            n = float(n)
        except ValueError:
            print(ERROR)
        else:
            print(RESULT.format(sqrt(n)))


if __name__ == "__main__":
    main()
