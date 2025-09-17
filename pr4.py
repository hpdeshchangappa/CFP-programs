from tkinter import *

root = Tk()
root.geometry("300x200")

hlb = Label(root, text = "Form")
hlb.pack()

lb1 = Label(root, text = "Name :")
lb1.place(y=20)

e1 = Entry(root, width = 40)
e1.place(x=50,y=20)

lb2 = Label(root, text = "SRNo :")
lb2.place(y=50)

e2 = Entry(root, width = 40)
e2.place(x=50,y=50)

e1.insert(0, "") #Default text to be displayed as a prompt
def myClick():
    if e1=="Desh" and e2=="pes1ug24ca045":
        result.config(text=f"Name: {name}\nSRNo: {srno}", fg="green")
    else:
        result.config(text="Incorrect Information", fg="red")

Button(root, text="Enter", command=myClick, bg="blue", fg="white").place(x=120, y=75)

# Label to display result
result = Label(root, text="")
result.place(x=70, y=120)

root.mainloop()

        
