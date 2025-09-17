from tkinter import *
#creating buttons
root = Tk()#creates a window
root.geometry("400x100")
lbl=Label(root, text= "Enter text")
lbl.pack()
#text box
e=Entry(root, width = 50)
e.pack()

e.insert(0,"Enter your name")
def myClick():
    message="hello " + e.get()
    lb4=Label(root, text = message)
    lb4.pack()
    
bt1=Button(root, text="click me!",command=myClick, bg="blue", fg="green")
bt1.pack()

root.mainloop()