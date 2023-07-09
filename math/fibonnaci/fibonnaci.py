from typing import Any, Callable


GET_NUMBER = "Enter how many numbers of the Fibonnaci squence you want to see: "
NUMERIC_ERROR = "Please enter an integer"


def memo(fun: Callable[[int], Any]) -> Callable[[int], Any]:
    cache = {}
    def inner(n: int):
        if n not in cache:
            cache[n] = fun(n)
        return cache[n]
    return inner


@memo
def fib(n: int) -> int:
    """Gets nth number of the Fibonnaci sequence.

    Calculates the value recursively.  Given the structuce of the
    recursive call the use of memoization is needed, the function
    would otherwise not be able to calculate values above 30 or so
    within reasonable time.
    """
    return 1 if n < 2 else fib(n-1) + fib(n-2)


def main() -> None:
    # Get length of sequence.
    while not (n := input(GET_NUMBER)).isnumeric():
        print(NUMERIC_ERROR)

    # Print sequence.
    for i in range(int(n)):
        print(fib(i))


if __name__ == "__main__":
    main()
