import argparse


def prime(n: int) -> bool:
    """Primality test for n.

    Parameter:
        n : int
            Integer to be tested.

    Returns
        bool 
            True if n is prime otherwise False.
    """
    # Guard clause for n < 4 or if n is divisible by 2 or 3.
    if n < 4:
        return n > 1
    elif n % 2 == 0 or n % 3 == 0:
        return False

    # Prime validation via 6k+/-1 method.
    k = 5
    while k*k <= n:
        if n % k == 0 or n % (k+2) == 0:
            return False
        k += 6
    return True


def prime_factors(n: int) -> list[int]:
    """Return list of all prime factors of n.

    Parameters
        n : int
            Integer to be factorised.
    Return
        factors : list[int]
            List of prime factors of n.

        Edge cases:
            - If n is 1 or 0, list will contain 1 or 0 respectively.
            - If n < 0, list will contain -1.
    """
    # Guard if n is prime.
    if prime(n):
        return [n]

    # Set up list of prime factors, adding -1, 0, and 1 as needed.
    # (Yes I know they are not prime, but it makes the function return
    # a sensible value even for non-prime integers.)
    factors = []
    if n == 1 or n == 0:
        factors.append(n)
    elif n < 0:
        factors.append(-1)
        n = -n  # Make n positive if n was negative.

    # Loop to look for prime factors of n.
    factor = 1
    while factor <= n:
        if prime(factor):
            # Keep adding factor as a factor of n while factor divides n.
            while n % factor == 0:
                factors.append(factor)
                n //= factor  # Remove factor from n.
                if prime(n):
                    # If n is prime, add to list and break.
                    factors.append(n)
                    factor = n+1  # Breaks the outer while loop.
        factor += 1
    return factors


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="prime-factor",
        description="Factorise integer into primes."
    )
    parser.add_argument(
        "integer",
        nargs="*",
        type=int,
        help="integer to factorise"
    )
    args = parser.parse_args()
    for integer in args.integer:
        factors = map(str, prime_factors(integer))
        print(" ".join(factors))


if __name__ == "__main__":
    main()
