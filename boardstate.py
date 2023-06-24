class BoardState:
    def __new__ (cls, *args, **kwargs):
        print("1. Creating BoardState class")
        return super().__new__(cls)
        
    def __init__(self, action_cubes, bird_hand, bonus_hand, food, forest, grassland, wetland, goal_tiles, birdfeeder, bird_tray):
        print("2. Initializing BoardState class")

    def __repr__(self) -> str:
        return f"{type(self).__name__}()"
    pass