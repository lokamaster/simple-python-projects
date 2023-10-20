def sieve(n: int) -> list[int]:
    """Sieve of Eratosthenes.

    Will return a list of all prime numbers up to, and including, n.
    """
    numbers = [i for i in range(2, n+1)]
    primes = [True for _ in range(2, n+1)]  # Assume all numbers are prime.

    # Loop to set all numbers that share a factor with any prime
    # less than sqrt(n) to non prime.
    factor = 2  # First prime is 2 (sorry 1).
    while factor*factor <= n:
        # Set all multiples of the current factor to not prime
        # (not including the factor itself).
        for index in range(2*factor - 2, n-1, factor):
            primes[index] = False

        # Set factor to next prime.
        factor = numbers[primes.index(True, factor-1)]

    # Make list of all primes and return.
    return [number for number, prime in zip(numbers, primes) if prime]

