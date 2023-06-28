class BoardState:
    def __new__ (cls, *args, **kwargs):
        print("1. Creating BoardState class")
        return super().__new__(cls)
        
    def __init__(self, action_cubes, bird_hand, bonus_hand, food, forest, grassland, wetland, goal_tiles, birdfeeder, bird_tray):
        print("2. Initializing BoardState class")
        self.action_cubes = action_cubes
        self.bird_hand = bird_hand
        self.bonus_hand = bonus_hand
        self. food = food
        self.forest = forest
        self.grassland = grassland
        self.wetland = wetland
        self. goal_tiles = goal_tiles
        self.birdfeeder = birdfeeder

    def __repr__(self) -> str:
        return f"{type(self).__name__}()"
    pass