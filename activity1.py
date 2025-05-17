# import necessary libraries
from tkinter import *

# setting up main window
root = Tk()
root.geometry("400x300")
root.title("main")

# function to open new (Top Level1) window
def topwin():
    # setting up to window
    top = Toplevel()
    top.geometry("180x100")
    top.title("Top Level1")
    # Adding a label widget to top window
    l2 = Label(top, text="This is Toplevel1 window")
    l2.pack()

    top.mainloop()

# adding a lebel and button widget to root (Main) window
l = Label(root, text="This is root window")
btn = Button(root, text = "click here to open another window", command = topwin)

# Arranging widgets
l.pack()
btn.pack()

root.mainloop()
