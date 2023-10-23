import pyshorteners
from tkinter import *

win = Tk()
win.geometry("400x270")
win.configure(bg="pink")

# Button function
def short():
    url = entry1.get()
    s=pyshorteners.Shortener().tinyurl.short(url)

    entry2.insert(END,s)
       
# Label
Label(win,text="Enter your URL Link",font="impack 17 bold", bg="black", fg="white").pack(fill="x")
# Entry box
entry1= Entry(win,font="10",bd=3,width=30)
entry1.pack(pady=30)
# Button
Button(win, text="submit",font="impact 10 ",bg="blue",fg="white",width="14",command=short).pack()
# Entry
entry2=Entry(win,font="impact 16 bold", bg="pink",width=24,bd=0)
entry2.pack(pady=30)
mainloop()

