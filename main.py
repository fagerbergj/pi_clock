import tkinter as tk
from app import App

class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master=master
        self.master.attributes("-fullscreen", True)
        self.master.attributes("-topmost", True)
        self.master.configure(background='black')
        self.master.bind('<Escape>',self.resize)   

    def resize(self,event):
        self.master.attributes("-fullscreen", False)

root=App()
app=FullScreenApp(root)
root.mainloop()