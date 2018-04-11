import tkinter as tk

LARGE_FONT = ("Verdana", 12)

class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        ## calender here
        label = tk.Label(self, text = "GMail", font = LARGE_FONT)
        label.config(fg='white', bg='black')
        label.pack(pady = 10, padx = 10)

        ## buttons in place of swipe for now
        button1 = tk.Button(self, text = "Time/Weather", 
             command= lambda: controller.show_frame(1))
        button1.pack()

        button2 = tk.Button(self, text = "Calender", 
             command= lambda: controller.show_frame(2))
        button2.pack()
