import tkinter as tk
from app import App

class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master=master
        self._geom='200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth(), master.winfo_screenheight()))
        master.bind('<Escape>',self.resize)   

    def resize(self,event):
        geom=self.master.winfo_geometry()
        print(geom,self._geom)
        self.master.geometry(self._geom)
        self._geom=geom

root=App()
app=FullScreenApp(root)
root.mainloop()