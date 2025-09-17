import tkinter as tk
def on_click():
    print("botton clicked")
root=tk.Tk()
root.title("button widget example")
#creating a button with multiple parameters
button = tk.Button(root,
text="Click Me",
command=on_click,
width=15,
height=2,
bg="lightblue",
fg="black",
font=("Arial", 14, "bold"),
relief=tk.RAISED,
padx=10, pady=10,
activebackground="green",
activeforeground="white",
bd=5)
button.pack(pady=20)
root.mainloop()


