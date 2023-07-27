import tkinter as tk
from tkinter import ttk

def get_frames():

    # ================================== #
    # functions used by frame generators
    def create_tab(tab_parent, tab_text):
        frame = ttk.Frame(tab_parent)
        tab_parent.add(frame, text=tab_text)
        return frame

    def create_tab_content(tab_frame, content_text):
        label = ttk.Label(tab_frame, text=content_text)
        label.pack(padx=10, pady=10)
    # ================================== #
        
    frames = []
    frame = lambda f: frames.append(f)
    
    @frame
    def get_gameboard_frame(root, bg_color="white", width=None, height=None):
        frame = tk.Frame(root, bg=bg_color, width=width, height=height)
        notebook = ttk.Notebook(frame)
        action_cube_tab = create_tab(notebook, "Gameboard Overview")
        create_tab_content(action_cube_tab, "This is the gameboard overview tab.")
        action_cube_tab = create_tab(notebook, "AI Parameters")
        create_tab_content(action_cube_tab, "This is the AI parameters tab.")
        notebook.pack(fill=tk.BOTH, expand=True)
        return frame

    @frame
    def get_ai_frame(root, bg_color="red", width=None, height=None):
        frame = tk.Frame(root, bg=bg_color, width=width, height=height)
        return frame
    
    return frames