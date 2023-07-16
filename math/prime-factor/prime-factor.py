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


def primes_up_to(n: int) -> list[int]:
    """Find all primes less than or equal to n.

    Parameters:
        n : int
            Integer to use as boundry.

    Returns:
        primes : list[int]
            List with all ptimes less than or equal to n.
    """
    primes = []
    k = 1
    while k <= n:
        if prime(k):
            primes.append(k)
        k += 1
    return primes


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
    factors = []
    if n == 1 or n == 0:
        factors.append(n)
    elif n < 0:
        factors.append(-1)
        n = -n
    elif prime(n):
        return list(n)
    potential_factors = primes_up_to(n)
    for factor in potential_factors:
        if n % factor == 0:
            while n % factor == 0:
                factors.append(factor)
                n //= factor 
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
