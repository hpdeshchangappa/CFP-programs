from tkinter import *

root = Tk()
root.geometry("300x200")

# Labels and Input Fields
Label(root, text="Form").pack()

Label(root, text="Name:").place(x=10, y=20)
e1 = Entry(root, width=30)
e1.place(x=70, y=20)

Label(root, text="SRNo:").place(x=10, y=50)
e2 = Entry(root, width=30)
e2.place(x=70, y=50)

# Function to handle button click
def myClick():
    name = e1.get()  # Get name from entry
    srno = e2.get()  # Get SRNo from entry

    # Check credentials and update the result label
    if name == "Desh" and srno == "pes1ug24ca045":
        result.config(text=f"Name: {name}\nSRNo: {srno}", fg="green")
    else:
        result.config(text="Information Incorrect", fg="red")

# Button to trigger the function
Button(root, text="Enter", command=myClick, bg="blue", fg="white").place(x=120, y=75)

# Label to display result
result = Label(root, text="")
result.place(x=70, y=120)

root.mainloop()
