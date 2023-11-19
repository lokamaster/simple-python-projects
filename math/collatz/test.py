from collatz import collatz, collatz_series


def test() -> bool:
    assert collatz(1) == 4
    assert collatz(2) == 1
    assert collatz(3) == 10
    assert collatz(4) == 2
    assert collatz(5) == 16

    assert collatz_series(1) == (0, 1)
    assert collatz_series(27) == (111, 9232)
    assert collatz_series(871)[0] == 178

    return True


if __name__ == "__main__":
    if test():
        print("All tests passed")

