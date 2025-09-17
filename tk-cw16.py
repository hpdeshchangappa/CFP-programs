from tkinter import *
from tkinter import messagebox as mb
root=Tk()
root.geometry("400x200")
def answer():
    if mb.askyesno("Answer", "Is 2020 a leap year?"):
        mb.showinfo('Answer', 'Correct')
        exit()
    else:
         mb.showinfo('Answer', 'Incorrect')
         exit()
         
def callback():
    if mb.askyesno('Verify', 'Really quit?'):
        mb.showinfo('Quit', 'Goodbye')
        exit()
    else:
        mb.showinfo('No', 'Good Choice')
        
label =Label(root, text = "Would you like to answer a Question?").pack()
b1 = Button(root, text='Answer', command=answer).pack(fill=X)
b2 = Button(root, text='Quit', command=callback).pack(fill=X)

root.mainloop()