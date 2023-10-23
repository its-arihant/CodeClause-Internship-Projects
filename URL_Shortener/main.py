import pyshorteners
from tkinter import *

win = Tk()
win.geometry("400x270")
win.configure(bg="pink")
#label
Label(win,text="Enter your URL Link",font="impack 17 bold", bg="black", fg="white").pack(fill="x")
#Entry box
entry1= Entry(win,font="10",bd=3,width=30)
entry1.pack(pady=30)
#Button
Button(win, text="submit",font="impact 10 ",bg="blue",fg="white",width="14").pack()
mainloop()

