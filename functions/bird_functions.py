from copy import deepcopy
from classes.boardstate import BoardState

powers = {}
power = lambda f: powers.setdefault(f.__name__, f)

@power
def abbots_booby(board_in: BoardState) -> BoardState:
    board_out = deepcopy(board_in)
    return