import tkinter as tk

root = tk.Tk()
root.title("place() example")
root.geometry("300x400")

labell=tk.Label(root, text="Label 1", bg="lightblue")
label2=tk.Label (root, text="Label 2", bg="lightgreen")

labell.place(x=50, y=50)
label2.place(x=150, y=100)

root.mainloop()