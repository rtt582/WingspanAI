import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog


def make_frame(root, bg_color="white", width=None, height=None):
    # ================================== #
    # functions used by frame generator
    def create_tab(tab_parent, tab_text):
        frame = ttk.Frame(tab_parent)
        tab_parent.add(frame, text=tab_text)
        return frame

    def create_tab_content(tab_frame, content_text):
        label = ttk.Label(tab_frame, text=content_text)
        label.pack(padx=10, pady=10)
        
    def create_overview_tab(notebook):
        frame = create_tab(notebook, "Overview")
                # Labels
        tk.Label(frame, text="Action Cubes:").grid(row=0, column=0, sticky='w')
        tk.Label(frame, text="Bird Hand:").grid(row=1, column=0, sticky='w')
        tk.Label(frame, text="Bonus Hand:").grid(row=2, column=0, sticky='w')
        tk.Label(frame, text="Food:").grid(row=3, column=0, sticky='w')
        tk.Label(frame, text="Forest:").grid(row=4, column=0, sticky='w')
        tk.Label(frame, text="Grassland:").grid(row=5, column=0, sticky='w')
        tk.Label(frame, text="Wetland:").grid(row=6, column=0, sticky='w')
        tk.Label(frame, text="Goal Tiles:").grid(row=7, column=0, sticky='w')
        tk.Label(frame, text="Birdfeeder:").grid(row=8, column=0, sticky='w')
        tk.Label(frame, text="Bird Tray:").grid(row=9, column=0, sticky='w')
        
        
        # Create a frame inside the "Overview" tab
        tab_frame = ttk.Frame(frame, width=200, height=200)
        tab_frame.grid(row=0, column=1, rowspan=10, padx=10, pady=10)
        
        # Add widgets inside the tab_frame
        tk.Label(tab_frame, text="This is a frame inside the tab!").pack()

        # Create a custom ttk.Style for the tab_frame to set the background color
        style = ttk.Style()
        style.configure("TabFrame.TFrame", background="red")
        tab_frame.configure(style="TabFrame.TFrame")
    
    def create_ai_parameter_tab(notebook):
        frame = create_tab(notebook, "AI Parameters")
        pass
    # ================================== #
    frame = tk.Frame(root, bg=bg_color, width=width, height=height)
    notebook = ttk.Notebook(frame)
    create_overview_tab(notebook)
    create_ai_parameter_tab(notebook)
    notebook.pack(fill=tk.BOTH, expand=True)
    return frame