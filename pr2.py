import tkinter as tk
root = tk.Tk()
root.title("Label Widget Example")
label = tk.Label(root,
 text="Hello, Tkinter!",
 font=("Arial", 16, "italic"),
 bg="lightblue", fg="darkblue",
 padx=10, pady=10,
 relief=tk.RIDGE,
 borderwidth=5,
 anchor=tk.CENTER,
 wraplength=150)
label.pack(pady=20)
root.mainloop()