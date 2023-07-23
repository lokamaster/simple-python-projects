import argparse
import re


def read_file(file_name: str) -> list[str]:
    """Read a file and return a list of strings.

    All rows are stripped of newline character.
    """
    with open(file_name, "r") as file:
        data = [row.strip() for row in file]
    return data


def word_count(text: str, word: str) -> int:
    """Count the occurence of given word in list.
    
    Will match exact matches, ignoring case and punctuation.  E.g. with
    word "hi" will match "Hi", "hi." and "HI!" but not "his".
    """
    regex = rf'\b{re.escape(word)}\b'
    count = len(re.findall(regex, text, re.IGNORECASE))
    return count


def word_count_in_file(file: str, word: str) -> int:
    """Wrapper to count occurance of word in file."""
    data = read_file(file)
    count = sum(word_count(row, word) for row in data)
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
        count = word_count_in_file(arguments.filename, arguments.word)
    except FileNotFoundError:
        print("ERROR: File not found.")
    else:
        print(count)


if __name__ == "__main__":
    main()

