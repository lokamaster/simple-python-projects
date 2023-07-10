ROW_QUESTION = "Enter how many rows to show: "
NUMERIC_ERROR = "Please enter an integer."


def factorial(n: int) -> int:
    product = 1
    while n:
        product *= n
        n -= 1
    return product


def choose(n: int, k: int) -> int:
    if k >= n:
        return 1
    else:
        return factorial(n) // (factorial(k) * factorial(n-k))


def pascal_row(n: int) -> list[int]:
    return [choose(n, k) for k in range(n+1)]


def pascal_triangle(n: int) -> list[list[int]]:
    return [pascal_row(k) for k in range(n)]


def longest_int(lst: list[list[int]]) -> int:
    """Calculates the longest value in a matrix."""

    # Potential one-line (unreadable).
    # return max([max([len(str(val)) for val in row]) for row in lst])
    longest = float("-inf")
    for row in lst:
        for val in row:
            if len(str(val)) > longest:
                longest = len(str(val))
    return longest


def main() -> None:
    # Get number for rows to print from user.
    while not (n := input(ROW_QUESTION)).isnumeric():
        print(NUMERIC_ERROR)
    else:
        n = int(n)
    
    # Create triangle.
    triangle = pascal_triangle(n)

    # Calculate padding (longest int + 1).
    padding = longest_int(triangle) + 1
    padding += padding % 2  # More even triangle with uneven padding.
    
    # Print out the rows of the triangle.
    for row in triangle:
        values = ""
        for value in row:
            values += str(value).center(padding)
        print(values.center(padding*n))


if __name__ == "__main__":
    main()
 
