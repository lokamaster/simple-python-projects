# Color constants
BLACK_FG = "30"
BLACK_BG = "40"
RED_FG = "31"
RED_BG = "41"
GREEN_FG = "32"
GREEN_BG = "42"
YELLOW_FG = "33"
YELLOW_BG = "43"
BLUE_FG = "34"
BLUE_BG = "44"
MEGANTA_FG = "35"
MEGENTA_BG = "45"
CYAN_FG = "36"
CYAN_BG = "46"
WHITE_FG = "37"
WHITE_BG = "38"
DEFAULT_FG = "39"
DEFAULT_BG = "49"

# Special characters
ESC = "\033["
DELIMITER = ";"
END = "m"
CLEAR_LINE = "K"
PREV_LINE = "F"


def create_clear_string(n: int) -> str:
    """Create string to clear n lines in console."""
    return f'{ESC}{PREV_LINE}'.join(f'{ESC}{CLEAR_LINE}' for _ in range(n))


def create_color_code(
        string: str,
        color_fg: str = DEFAULT_FG,
        color_bg: str = DEFAULT_BG
) -> str:
    return f'{ESC}{color_fg}{DELIMITER}{color_bg}{END}{string}{ESC}{END}'


def clear_rows(n: int) -> None:
    """Wrapper for clearing row."""
    print(create_clear_string(n), end="")

