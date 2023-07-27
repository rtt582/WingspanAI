import tkinter as tk
from tkinter import ttk

def create_tab(tab_parent, tab_text):
    frame = ttk.Frame(tab_parent)
    tab_parent.add(frame, text=tab_text)
    return frame

def create_tab_content(tab_frame, content_text):
    label = ttk.Label(tab_frame, text=content_text)
    label.pack(padx=10, pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Multiple Tabs Example")
    root.geometry("600x400")

    notebook = ttk.Notebook(root)
    notebook.pack(fill=tk.BOTH, expand=True)

    # Create three tabs
    tab1 = create_tab(notebook, "Tab 1")
    tab2 = create_tab(notebook, "Tab 2")
    tab3 = create_tab(notebook, "Tab 3")

    # Add content to each tab
    create_tab_content(tab1, "This is content for Tab 1.")
    create_tab_content(tab2, "Welcome to Tab 2.")
    create_tab_content(tab3, "Content of Tab 3 goes here.")

    root.mainloop()
