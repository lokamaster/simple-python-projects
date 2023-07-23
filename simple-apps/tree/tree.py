import argparse
import os


INNER = "|   "
OUTER = "|-- "
HIDDEN = "."


def print_tree(
        cwd: str,
        depth: int = 0,
        max_depth: int = 3,
        hidden: bool = False
) -> None:
    # If first call, print cwd.
    if depth == 0:
        print(cwd)
    
    # Break if max depth is reached.
    if depth >= max_depth:
        return

    # Used to pad tree based on depth.
    # Example:
    # |   |-- Folder-name  -depth 2
    # |   |   |-- File-in-folder  -depth 3
    delimiter = INNER*depth + OUTER
        
    # Get list of content in current directory.
    dir_content = sorted(os.listdir(cwd))

    # Print content of folders recursively.
    for name in dir_content:
        # Ignore if file is hidden and hidden flag is off.
        if name.startswith(HIDDEN) and not hidden:
            continue

        # Check if folder and print content.
        path = os.path.join(cwd, name)
        if os.path.isdir(path):
            print(delimiter + name)
            try:
                print_tree(path, depth + 1, max_depth)
            except PermissionError:
                pass

    # Print files in folder.
    for name in dir_content:
        # Ignore if file is hidden and hidden flag is off.
        if not hidden and name.startswith(HIDDEN):
            continue

        # Check if not folder and print name.
        path = os.path.join(cwd, name)
        if not os.path.isdir(path):
            print(delimiter + name)


def main():
    # Set up parser.
    parser = argparse.ArgumentParser(
            prog="tree",
            description="List content of folder",
    )
    parser.add_argument(
            "path",
            help="path to folder, default cwd",
            nargs="?",
            default=os.getcwd(),
    )
    parser.add_argument(
            "-d", "--depth",
            help="depth of folders to print",
            default=3,
            type=int,
    )
    parser.add_argument(
            "-a", "--all",
            help="flag to show hidden files",
            action="store_true"
    )
            
    # Get arguments and print tree.
    args = parser.parse_args()
    print_tree(
            args.path,
            max_depth=args.depth,
            hidden=args.all,
    )


if __name__ == "__main__":
    main()

