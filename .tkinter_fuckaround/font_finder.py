import tkinter as tk
from tkinter import font

root = tk.Tk()

# Get a list of all available font families
available_fonts = font.families()
for font_family in available_fonts:
    print(font_family)

root.mainloop()