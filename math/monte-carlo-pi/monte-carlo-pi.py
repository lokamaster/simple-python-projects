import random

# Game constants.
RADIUS = 1

# Shell dialogue.
INTRO = (
    "This app will calculate the value of pi by randomly thowing darts "
    "at a square board with side length 2.\n"
    "Pi can be estimated by comparing the ratio of darts landing within "
    "a unit circle to the area of the board.\n"
)
GET_THROWS = "Enter the number of darts to throw: "
NUMERIC_ERROR = "Please anter an integer."
THROWS_INSIDE_CIRCLE = "{} out of {} throws landed in the circle."
RESULT = "The ratio of throws inside circle is {0:.4f} and pi estimate is {1:.4f}."


def get_throws(n: int) -> list[tuple[float, float]]:
    return [
            (random.uniform(-RADIUS, RADIUS), random.uniform(-RADIUS, RADIUS))
            for throw in range(n)
    ]


def distance(x: float, y: float) -> float:
    return (x**2 + y**2)**0.5


def main() -> None:
    print(INTRO)

    # Get throws from user.
    while not (n_throws := input(GET_THROWS).strip()).isnumeric():
        print(NUMERIC_ERROR)
    else:
        n_throws = int(n_throws)

    # Estimate pi.
    throws = get_throws(n_throws)
    throws_in_circle = sum([distance(*throw) <= RADIUS for throw in throws])
    ratio = throws_in_circle / n_throws
    pi = (2*RADIUS)**2 * ratio  # Square area times ratio of throws in circle.

    # Print results.
    print(THROWS_INSIDE_CIRCLE.format(throws_in_circle, n_throws))
    print(RESULT.format(ratio, pi))


if __name__ == "__main__":
    main()

