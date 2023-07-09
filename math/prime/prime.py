WELCOME = "Welcome to prime finder. Enter a number to see if it is prime"
GET_NUMBER = "Enter number: "
PRIME = "The number is prime!"
NOT_PRIME = "The number is not prime :("
NUMERIC_ERROR = "Please enter an integer"


def is_prime(n: int) -> bool:
    """Calculates if the given number n is prime.

    Uses the 6k +/- 1 method wich is based on the fact that every prime
    other than 2 and 3 are one more or less than a multiple of 6 (which
    is just a fancy way of saying that every prime other than 2 and 3 are
    not multiples of 2 or 3).
    """
    # Guard clauses for 2, 3 or multiples of 2 and 3.
    if n < 4:
        return n > 1
    elif n % 2 == 0 or n % 3 == 0:
        return False

    # Main loop
    k = 5
    while k*k < n:
        if n % k == 0 or n % (k+2) == 0:
            return False
        k += 6
    
    # No devisors found - number is prime.
    return True


def main() -> None:
    print(WELCOME)
    while not (n := input(GET_NUMBER)).isnumeric():
        print(NUMERIC_ERROR)
    if is_prime(int(n)):
        print(PRIME)
    else:
        print(NOT_PRIME)


if __name__ == "__main__":
    main()

