import tkinter as tk

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Changing Window with Buttons")
        self.geometry("400x300")

        # Create the frames for different views
        self.frame1 = tk.Frame(self, bg="red")
        self.frame2 = tk.Frame(self, bg="green")
        self.frame3 = tk.Frame(self, bg="blue")

        # Pack all frames to fill the entire window
        self.frame1.pack(fill=tk.BOTH, expand=True)
        self.frame2.pack(fill=tk.BOTH, expand=True)
        self.frame3.pack(fill=tk.BOTH, expand=True)
        
        # Create buttons to switch between views
        button1 = tk.Button(self.frame1, text="Go to Green View", command=self.show_green_view)
        button2 = tk.Button(self.frame2, text="Go to Blue View", command=self.show_blue_view)
        button3 = tk.Button(self.frame3, text="Go to Red View", command=self.show_red_view)

        # Pack buttons in their respective frames
        button1.pack(pady=10)
        button2.pack(pady=10)
        button3.pack(pady=10)

        # Initialize current view to frame1
        self.current_view = self.frame1

        

        # Initially show frame1
        self.show_frame(self.frame1)

    def show_frame(self, frame):
        # Hide the current view and show the new frame
        self.current_view.pack_forget()
        frame.pack(fill=tk.BOTH, expand=True)
        print(frame)
        self.current_view = frame

    def show_green_view(self):
        self.show_frame(self.frame2)

    def show_blue_view(self):
        self.show_frame(self.frame3)

    def show_red_view(self):
        self.show_frame(self.frame1)

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
