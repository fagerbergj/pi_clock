import tkinter as tk

LARGE_FONT = ("Verdana", 12)

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        ## calender here
        label = tk.Label(self, text = "Calender", font = LARGE_FONT)
        label.pack(pady = 10, padx = 10)

        ## buttons in place of swipe for now
        button1 = tk.Button(self, text = "Gmail", 
             command= lambda: controller.show_frame("Page 3"))
        button1.pack()

        button2 = tk.Button(self, text = "Time/Weather", 
             command= lambda: controller.show_frame("Page 1"))
        button2.pack()
