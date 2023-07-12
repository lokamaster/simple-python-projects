import argparse
import os


HIDDEN_PREFIX = "."


def list_files(path: str, show_hidden=False) -> None:
    # Only get and print content of folder if it exists.
    if os.path.exists(path):
        for file in os.listdir(path):
            if not file.startswith(HIDDEN_PREFIX) or show_hidden:
                # Hidden files start with a certain prefix, usually ".",
                # this means that the show_hidden flag need to be set in
                # order to print the hidden files to console.
                print(file)


def main() -> None:
    # Create parser
    parser = argparse.ArgumentParser(
            prog="ls",
            description=(
                "List all files in path."
                "If no path is given, the files in cwd will be listed"
            )
    )
    parser.add_argument(
            "path",
            nargs="*",
            default=[os.getcwd()],
            help="path to folders whose files to be listed",
    )
    parser.add_argument(
            "-a", "--all",
            action="store_true",
            help="list hidden files",
    )

    # Get passed paths and print files
    args = parser.parse_args()
    for path in args.path:
        list_files(path, args.all)


if __name__ == "__main__":
    main()

