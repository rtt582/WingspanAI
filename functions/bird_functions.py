from copy import deepcopy
import sys
sys.path.append(".\\classes")
from boardstate import BoardState

powers = {}
power = lambda f: powers.setdefault(f.__name__, f)

@power
def abbots_booby(board_in: BoardState) -> BoardState:
    board_out = deepcopy(board_in)
    print("in abbots booby")
    #TODO: finish function
    return board_out

@power
def acorn_woodpecker(board_in: BoardState) -> BoardState:
    board_out = deepcopy(board_in)
    print("in acorn woodpecker")
    #TODO: finish function
    return board_out

print(powers)
powers['abbots_booby'](0)