import argparse
import re


def read_file(file_name: str) -> list[str]:
    """Read a file and return a list of strings.

    All rows are stripped of newline character.
    """
    with open(file_name, "r") as file:
        data = [row.strip() for row in file]
    return data


def word_count(data: list[str], word: str) -> int:
    """Count the occurence of given word in list.
    
    Will match exact matches, ignoring case and punctuation.  E.g. with
    word "hi" will match "Hi", "hi." and "HI!" but not "his".
    """
    regex = rf'\b{re.escape(word)}\b'
    count = 0
    for row in data:
        word_in_row = len(re.findall(regex, row, re.IGNORECASE))
        count +=  word_in_row
    return count


def main() -> None:
    # Set up parser.
    parser = argparse.ArgumentParser(
        prog="wc",
        description="Count the occurence of word in document"
    )
    parser.add_argument("filename", help="path to file")
    parser.add_argument("word", help="word to count")
    arguments = parser.parse_args()

    # Try to read file and count words.
    try:
        file = read_file(arguments.filename)
    except FileNotFoundError:
        print("ERROR: File not found.")
    else:
        print(word_count(file, arguments.word))


if __name__ == "__main__":
    main()

