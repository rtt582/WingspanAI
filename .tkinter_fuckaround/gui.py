import tkinter as tk
from tkinter import ttk
from frames import get_frames

WINDOW_SCALING_FACTOR = 2

def init_main_window(scaling_factor: float):
    root = tk.Tk()
    root.title("Wingspan AI")
    width = root.winfo_screenwidth()
    width = int(width/scaling_factor)
    height = root.winfo_screenheight()
    height = int(height/scaling_factor)
    root.geometry(f"{width}x{height}")
    return root

def init_frames(root):
    frames = []
    for frame in get_frames():
        frames.append(frame(root, width=root.winfo_width(), height=root.winfo_height()))
    print(frames)
    return frames

def show_frame(frame):
    frame.tkraise()
        
if __name__ == "__main__":
    app = init_main_window(WINDOW_SCALING_FACTOR)
    print(type(app))
    frames = init_frames(app)
    
    # Organize frames using grid geometry manager
    for frame in frames:
        frame.grid(row=0, column=0, sticky=tk.NSEW)
        app.grid_rowconfigure(0, weight=1)
        app.grid_columnconfigure(0, weight=1)

    # Create a button to switch between frames
    btn_switch_frame = ttk.Button(app, text="Switch Frame")
    btn_switch_frame.grid(row=1, column=0, pady=10)

    current_frame_idx = 1

    def on_switch_frame():
        global current_frame_idx
        current_frame = frames[current_frame_idx]
        current_frame.grid_forget()  # Hide the current frame
        current_frame_idx = (current_frame_idx + 1) % len(frames)  # Move to the next frame
        next_frame = frames[current_frame_idx]
        next_frame.grid(row=0, column=0, sticky=tk.NSEW)  # Show the next frame
        app.grid_rowconfigure(0, weight=1)
        app.grid_columnconfigure(0, weight=1)

    btn_switch_frame.config(command=on_switch_frame)
    
    app.mainloop()