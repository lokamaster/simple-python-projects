import os
import sys


FILE_ERROR = "{}: No such file."
NO_ARGUEMTN = "Please enter path to file."
MIN_ARG = 2


def read_file(file_name: str) -> list[str]:
    with open(file_name, "r") as file:
        data = [line for line in file]
    return data


def print_file(file_name: str) -> None:
    if os.path.isfile(file_name):
        for row in read_file(file_name):
                print(row, end="")
    else:
        print(FILE_ERROR.format(file_name))


def main() -> None:
    if len(sys.argv) < MIN_ARG:
        print(NO_ARGUMENT)
    else:
        for file in sys.argv[1:]:
            print_file(file)


if __name__ == "__main__":
    main()

