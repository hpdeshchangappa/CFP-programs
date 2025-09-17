import tkinter as tk

root=tk.Tk()
root.title("Tkinter RadioButton Example")
root.geometry("500x500")

var=tk.StringVar(value="Python")

languages=[("Python","Python"),
           ("Java","Java"),
           ("C++","C++"),
           ("JavaScript","JavaScript")]
for text, value in languages:
    tk.Radiobutton(root,
                   text=text,
                   variable=var,
                   value=value
                   ).pack()
root.mainloop()