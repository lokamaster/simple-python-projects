import random
from typing import Callable


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
    
    def __init__(self,
        computer_ai: Callable[[int, int, int], int],
        target: int = TARGET,
        min_turn: int = MIN_TURN,
        max_turn: int = MAX_TURN,
    ) -> None:
        self.target = target
        self.min_turn = min_turn
        self.max_turn = max_turn
        self.computer_ai = computer_ai
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

    def computer_turn(self):
        """Generate computer turn based on provided logic."""
        return self.computer_ai(self.current, self.target, self.max_turn)

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


# Computer strategies - could be generalized into a class or maybe
# put into separate module.
def pseudo_random(current: int, target: int, max_turn: int) -> int:
    """Generate computer turn somewhat randomly.

    If target is within range, computer adds enough to win, else it
    will add a "random" amount based on the mod of the current value.
    """
    if target - current <= max_turn:
        return target - current
    else:
        return (current % max_turn) + 1


def winning_strat(current: int, target: int, max_turn: int) -> int:
    """Tries to win game, if not possible it will add one.

    Based on the fact that the winning strategy can be recursively
    calculated by the understanding that the player who can put the total
    one more than the max turn away from the target will win the game.

    Example: Target is 23, max turn is 4.
        Player who can put total to 18 will win since next player will
        put total to a value between 19 and 22, all which are within
        reach of the target for player who put total at 18.
        
        This implies that the game can be stated as whoever gets to 18
        first wins the game, which by the same logic means that whoever
        can put the total to 13 will win the game.

        So on and so forth until the winning target becomes 3, which means
        that whoever starts the game is guaranteed to win it.

    The formula for calculating the optimal move is:
        (target - current) % (max_turn + 1).
    since target - current gives the distance away from total and the set
    of winning targets ({23, 18, 13, 8, 3} as per the example above) all lie
    within a multiple of (max_turn + 1) away from the target.

    So if current value is 16, target 23, and max turn 4 the formula gives:
        (23 - 16) % (4 + 1) = 7 % 5
                            = 2
    """
    optimal_to_add = (target-current) % (max_turn + 1)
    return optimal_to_add or 1  # If the optimal turn is 0, return 1.


def main() -> None:
    ai = [
        pseudo_random,
        winning_strat
    ]
    game = GotIt(computer_ai=random.choice(ai))
    game.run()


if __name__ == "__main__":
    main()

