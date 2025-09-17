from tkinter import *
#creating buttons
root = Tk()#creates a window
root.geometry("400x100")
lbl=Label(root, text= "Enter text")
lbl.pack()

e = Entry(root,font=("Arial",14),bg="lightyellow",fg="black",width=30,
        show="*",#mask input like password
        justify=CENTER,
        selectbackground="lightblue",
        selectforeground="red",
        relief=GROOVE,bd=5,
        highlightcolor="blue",
        highlightthickness=2)
e.pack()
root.mainloop()
