class BoardState:
    def __new__ (cls, *args, **kwargs):
        print("1. Creating BoardState class")
        return super(BoardState, cls).__new__(cls)
        
    def __init__(self):
        print("2. Initializing BoardState class")
        self.action_cubes = 0
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
        return f"{type(self).__name__}()"

    def draw_bonus(self, bonus_card: str) -> None:
        self.bonus_hand.append(bonus_card)
        
    def discard_bonus(self, bonus_card: str) -> None:
        self.bonus_hand.remove(bonus_card)