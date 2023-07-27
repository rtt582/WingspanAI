class BoardState:
    def __new__ (cls, *args, **kwargs):
        print("1. Creating BoardState class")
        return super(BoardState, cls).__new__(cls)
        
    def __init__(self):
        print("2. Initializing BoardState class")
        self.action_cubes = 8
        self.bird_hand = []
        self.bonus_hand = []
        self.food = []
        self.forest = []
        self.grassland = []
        self.wetland = []
        self.goal_tiles = []
        self.birdfeeder = []
        self.bird_tray = []

    def __repr__(self) -> str:
        repr_str = f"{type(self).__name__}(\n"
        repr_str += f"    action_cubes={self.action_cubes},\n"
        repr_str += f"    bird_hand={self.bird_hand},\n"
        repr_str += f"    bonus_hand={self.bonus_hand},\n"
        repr_str += f"    food={self.food},\n"
        repr_str += f"    forest={self.forest},\n"
        repr_str += f"    grassland={self.grassland},\n"
        repr_str += f"    wetland={self.wetland},\n"
        repr_str += f"    goal_tiles={self.goal_tiles},\n"
        repr_str += f"    birdfeeder={self.birdfeeder},\n"
        repr_str += f"    bird_tray={self.bird_tray}\n"
        repr_str += ")"

        return repr_str


    def draw_bonus(self, bonus_card: str) -> None:
        self.bonus_hand.append(bonus_card)
        
    def discard_bonus(self, bonus_card: str) -> None:
        self.bonus_hand.remove(bonus_card)