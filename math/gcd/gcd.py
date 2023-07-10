GET_INTEGER = "Enter your {} number: "
FIRST = "first"
SECOND = "second"
INTEGER_ERROR = "Must be an integer."
RESULT = "The gcd({}, {}) is {} and the lcm({}, {}) is {}."


def gcd(a: int, b: int) -> int:
    """Calculate the greatest common divisor via the Euclidean algorithm.

    The gcd(a, b) can be found by recursively calculating gcd(b, a % b)
    until a is divisible by b (a % b giving a remainder of 0).  At this
    stage the gcd is given by a.

    Example:
        gcd(27, 6) = gcd(6, 27 % 6)
                   = gcd(6, 3)
                   = gcd(3, 6 % 3)
                   = gcd(3, 0)
                   = 3
    """
    while b:
        a, b = (b, a % b)
    return a


def lcm(a: int, b: int) -> int:
    """Calculates the least common multiple of a and b.

    Uses the fact that lcm can be written as the product of a and b
    divided by their gcd.  This is obvious when a and b are written
    as product of primes.

    Example: lcm(18, 12)
    The gcd are all the primes that the two numbers have in common
        18 = 2 * 3 * 3
        12 = 2 * 2 * 3
    Both numbers have a 2 and a 3 in common, so the gcd is 6. This
    implies that the lcm can be written as
        (18 * 12) / 6 = (2*3*3) * (2*2*3) / (2*3)
                    = 2 * 2 * 3 * 3
                    = 4 * 9
                    = 36
    """
    return abs(a*b) // gcd(a, b) if a*b else 0


def main() -> None:
    # Get values from user.
    while not (a := input(GET_INTEGER.format(FIRST))).isnumeric():
        print(INTEGER_ERROR)
    else:
        a = int(a)
    while not (b := input(GET_INTEGER.format(SECOND))).isnumeric():
        print(INTEGER_ERROR)
    else:
        b = int(b)
    
    # Calculate and print result.
    print(RESULT.format(a, b, gcd(a, b), a, b, lcm(a, b)))


if __name__ == "__main__":
    main()

