import tkinter as tk
from tkinter import ttk
from frames import make_frame

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400

def center_window(root, width, height):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x_coordinate = (screen_width - width) // 2
    y_coordinate = (screen_height - height) // 2

    return f"{width}x{height}+{x_coordinate}+{y_coordinate}"

def init_main_window():
    root = tk.Tk()
    root.title("Wingspan AI")
    window_geometry = center_window(root, WINDOW_WIDTH, WINDOW_HEIGHT)
    root.geometry(window_geometry)
    return root

def init_frame(app):
    frame = make_frame(app)
    frame.grid(row=0, column=0, sticky=tk.NSEW)
        
if __name__ == "__main__":
    app = init_main_window()
    init_frame(app)
    app.mainloop()