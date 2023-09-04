import argparse


import hanoi


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="Hanoi solver",
        description="Solves the tower of hanoi"
    )
    parser.add_argument("bricks", type=int)

    args = parser.parse_args()
    moves = hanoi.solve(args.bricks)
    for start, end in moves:
        print(f'Moves {start} to {end}')


if __name__ == "__main__":
    main()
