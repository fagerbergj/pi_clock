import tkinter as tk

LARGE_FONT = ("Verdana", 12)

class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        ## time and wether here
        label = tk.Label(self, text = "Time/Weather", font = LARGE_FONT)
        label.config(fg='white', bg='black')
        label.pack(pady = 10, padx = 10)

        ## buttons in place of swipe for now
        button1 = tk.Button(self, text = "Calender", 
            command= lambda: controller.show_frame(2))
        button1.pack()

        button2 = tk.Button(self, text = "Gmail", 
            command= lambda: controller.show_frame(3))
        button2.pack()
