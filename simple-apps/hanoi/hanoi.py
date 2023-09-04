def solve(
        n: int,
        start: int = 1,
        middle: int = 2,
        end: int = 3,
        moves: None | list = None
) -> list[tuple[int, int]]:
    # If first call to function.
    if moves is None:
        moves = []

    # Solve the tower recursively.
    if n < 1:
        # Base case.
        return
    else:
        # Solve the tower in two steps, first solve tower with n-1
        # bricks to middle pin, then move the free large pin to goal
        # then solve the n-1 tower from middle to goal.
        solve(n-1, start, end, middle, moves)
        moves.append((start, end))
        solve(n-1, middle, start, end, moves)
    return moves
