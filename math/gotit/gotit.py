# Game variables
TARGET = 23
MIN_TURN = 1
MAX_TURN = 4

# Game messages
WELCOME = (
        "Welcome to Got It!\n"
        "The goal of the game is to reach the target value of {}\n"
        "Each player get to add a value between {} and {} each turn\n"
        "The player who adds a value that makes the total reach or "
        "surpass the target win the game!"
)
NEW_TURN = "\nTurn {}!"
GET_VALUE = "Enter value between {} and {} to add to total: "
CURRENT_VALUE = "The current value is {}."
COMPUTER_STEP = "Computer added {} to value."
GAME_END = "\nGame over, target of {} reached!"

# Error messages
INTEGER_ERROR = "Please enter an integer."
VALUE_ERROR = "Step not in the allowed range [{}, {}]"


def get_numeric(msg: str) -> int:
    while not (user_input := input(msg).strip()).isnumeric():
        print(INTEGER_ERROR)
    else:
        user_input = int(user_input)
    return user_input


class GotIt:
    
    def __init__(
            self,
            target: int = TARGET,
            min_turn: int = MIN_TURN,
            max_turn: int = MAX_TURN,
    ) -> None:
        self.target = target
        self.min_turn = min_turn
        self.max_turn = max_turn
        self.current = 0

    def take_turn(self, step: int) -> None:
        self.current += step

    def get_step(self) -> int:
        msg = GET_VALUE.format(self.min_turn, self.max_turn)
        value = get_numeric(msg)
        while self.min_turn > value or self.max_turn < value:
            print(VALUE_ERROR.format(self.min_turn, self.max_turn))
            value = get_numeric(msg)
        return value

    def computer_turn(self) -> int:
        """Generate computer turn.

        If target is within range, computer adds enough to win, else it
        will add a "random" amount based on the mod of the current value.
        """
        if self.target - self.current <= self.max_turn:
            return self.target - self.current
        else:
            return (self.current % self.max_turn) + 1

    def run(self) -> None:
        print(WELCOME.format(self.target, self.min_turn, self.max_turn))
        turn = 1
        while self.current < self.target:
            print(NEW_TURN.format(turn))
            print(CURRENT_VALUE.format(self.current))
            if turn % 2 == 1:
                step = self.get_step()
                self.take_turn(step)
            else:
                step = self.computer_turn()
                print(COMPUTER_STEP.format(step))
                self.take_turn(step)
            turn += 1
        print(GAME_END.format(self.target))


def main() -> None:
    game = GotIt()
    game.run()


if __name__ == "__main__":
    main()

