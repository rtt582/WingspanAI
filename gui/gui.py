import tkinter as tk
from tkinter import ttk
from tabs import ai, overview

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 530

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
    
    tab_control = ttk.Notebook(root)
    
    
    overview_tab = ttk.Frame(tab_control, height=500, width=600)
    ai_tab = ttk.Frame(tab_control, height=500, width=600)
    
    
    tab_control.add(overview_tab, text="Overview")
    tab_control.add(ai_tab, text="AI")
    
    overview.init_tab(overview_tab)
    ai.init_tab(ai_tab)
    
    tab_control.place(relx=0, rely=0)
    
    return root
 
if __name__ == "__main__":
    app = init_main_window()
    app.mainloop()