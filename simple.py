from tkinter import *

root = Tk()

root.title("my paint application")
root.geometry('500x350')

def paint(event):
    x1, y1 = (event.x-3), (event.y-3) 
    x2, y2 = (event.x+3), (event.y+3)
    color = "black"
    a.create_oval(x1, y1, x2, y2, fill=color, outline=color)

a = Canvas(root, width=500,height=350,bg="white")
a.bind('<B1-Motion>', paint)
a.pack()
root.mainloop()