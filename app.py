import tkinter as tk
from page_1 import PageOne
from page_2 import PageTwo
from page_3 import PageThree


class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand= True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        i = 1
        for F in (PageOne, PageTwo, PageThree):
            key = i
            frame = F(container, self)
            frame.config(background='black')
            self.frames[key] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")
            i += 1

        self.show_frame(1)

    def show_frame(self, key):
        frame = self.frames[key]
        frame.tkraise()
