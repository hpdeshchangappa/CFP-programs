import tkinter as tk
root=tk.Tk()
root.title("Text Example")
root.geometry("600x600")
text=tk.Text(root,font=("Arial",14),
             bg="lightyellow",
             fg="black",
             width=50,
             height=15,
             wrap=tk.WORD,
             selectbackground="lightblue",
             selectforeground="red",
             insertbackground="blue",
             relief=tk.SUNKEN,
             bd=5,
             undo=True)
text.pack()
root.mainloop()