import tkinter as tk
import time


class Gui:
    def __init__(self):
        self.root = tk.Tk()
        self.label = tk.Label(text="")
        self.label.grid(column=0, row=0)
        self.label.pack()
        self.update_clock()
        self.root.mainloop()

    def update_clock(self):
        now = time.strftime("%H:%M:%S")
        self.label.configure(text=now)
        self.root.after(1000, self.update_clock)


app = Gui()
