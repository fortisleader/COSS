from tkinter import *

window = Tk()
window.title("Canvas")

canvas = Canvas(window,height=500,width=500)
#canvas.create_arc(0,0,500,500,fill="red",extent=180,width=10)
#canvas.create_arc(0,0,500,500,fill="white",start=180,extent=180,width=10)
#canvas.create_oval(190,190,310,310,fill="white",width=10)
#canvas.create_arc(0,0,450,450,extent=90,fill="black")

canvas.create_rectangle(50,50,250,250,fill="red",width=15)


canvas.pack()


window.mainloop()