import tkinter as tk
from init.boardstate import BoardState


class BoardStateGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.board_state = BoardState()

        self.title("Board State GUI")
        width = self.winfo_screenwidth()
        width = int(width/2)
        height = self.winfo_screenheight()
        height = int(height/2)
        self.geometry(f"{width}x{height}")

        # Labels
        tk.Label(self, text="Action Cubes:").grid(row=0, column=0)
        tk.Label(self, text="Bird Hand:").grid(row=1, column=0)
        tk.Label(self, text="Bonus Hand:").grid(row=2, column=0)
        tk.Label(self, text="Food:").grid(row=3, column=0)
        tk.Label(self, text="Forest:").grid(row=4, column=0)
        tk.Label(self, text="Grassland:").grid(row=5, column=0)
        tk.Label(self, text="Wetland:").grid(row=6, column=0)
        tk.Label(self, text="Goal Tiles:").grid(row=7, column=0)
        tk.Label(self, text="Birdfeeder:").grid(row=8, column=0)
        tk.Label(self, text="Bird Tray:").grid(row=9, column=0)

        # Entry fields
        self.action_cubes_entry = tk.Entry(self)
        self.bird_hand_entry = tk.Entry(self)
        self.bonus_hand_entry = tk.Entry(self)
        self.food_entry = tk.Entry(self)
        self.forest_entry = tk.Entry(self)
        self.grassland_entry = tk.Entry(self)
        self.wetland_entry = tk.Entry(self)
        self.goal_tiles_entry = tk.Entry(self)
        self.birdfeeder_entry = tk.Entry(self)
        self.bird_tray_entry = tk.Entry(self)

        # Place entry fields
        self.action_cubes_entry.grid(row=0, column=1)
        self.bird_hand_entry.grid(row=1, column=1)
        self.bonus_hand_entry.grid(row=2, column=1)
        self.food_entry.grid(row=3, column=1)
        self.forest_entry.grid(row=4, column=1)
        self.grassland_entry.grid(row=5, column=1)
        self.wetland_entry.grid(row=6, column=1)
        self.goal_tiles_entry.grid(row=7, column=1)
        self.birdfeeder_entry.grid(row=8, column=1)
        self.bird_tray_entry.grid(row=9, column=1)

        # Buttons
        tk.Button(self, text="Update", command=self.update_board_state).grid(row=10, column=0, columnspan=2)
        tk.Button(self, text="View", command=self.view_board_state).grid(row=11, column=0, columnspan=2)

    def update_board_state(self):
        # Get the values from entry fields and update the BoardState object
        self.board_state.action_cubes = int(self.action_cubes_entry.get())
        self.board_state.bird_hand = self.bird_hand_entry.get().split(",")
        self.board_state.bonus_hand = self.bonus_hand_entry.get().split(",")
        self.board_state.food = self.food_entry.get().split(",")
        self.board_state.forest = self.forest_entry.get().split(",")
        self.board_state.grassland = self.grassland_entry.get().split(",")
        self.board_state.wetland = self.wetland_entry.get().split(",")
        self.board_state.goal_tiles = self.goal_tiles_entry.get().split(",")
        self.board_state.birdfeeder = self.birdfeeder_entry.get().split(",")
        self.board_state.bird_tray = self.bird_tray_entry.get().split(",")

    def view_board_state(self):
        # Display the current BoardState object in the console
        print(self.board_state.__repr__())

if __name__ == "__main__":
    app = BoardStateGUI()
    app.mainloop()
