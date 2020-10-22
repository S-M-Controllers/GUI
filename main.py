import tkinter as tk
import time

# TODO update State

consoleState = "Connected"

class Gui:
    def __init__(self):
        self.root = tk.Tk()
        self.statusLabel = tk.Label(text="State: " + consoleState)
        self.statusLabel.grid(row=0, column=0)
        self.timeLabel = tk.Label(text="")
        self.timeLabel.grid(row=0, column=1, padx=1000)
        self.update_clock()
        self.root.mainloop()

    def update_clock(self):
        now = time.strftime("%H:%M:%S")
        self.timeLabel.configure(text="Time: " + now)
        self.timeLabel.after(1000, self.update_clock)


app = Gui()
