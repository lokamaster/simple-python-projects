import argparse
import os
import re


URL = "http://www.duckduckgo.com/"
QUERY = "?q="


def create_url(base: str, query: str = "") -> str:
    return base + (QUERY + query) if query else base


def parse_query(query: list[str]) -> str:
    """Create query from list of strings.

    Function will join individual multi-word queries into single word
    query with words separated with plus signs.

    Example input:
        ["Hello there", "you", "are", "very cool"]
    Output:
        "Hello+there+you+are+very+cool"
    """
    regex = "\s+"  # Pattern match for whitespace.
    return "+".join(re.split(regex, "+".join(query)))


def open_url(url: str) -> None:
    os.system(f'open {url}')


def main() -> None:
    # Create parser.
    parser = argparse.ArgumentParser(
        prog="ddg",
        description="Search DuckDuckGo with query."
    )
    parser.add_argument(
            "query",
            nargs="*",
            help="term to use as query"
    )

    # Get args and open ddg.
    args = parser.parse_args()
    query = parse_query(args.query)
    url = create_url(URL, query)
    open_url(url)


if __name__ == "__main__":
    main()

