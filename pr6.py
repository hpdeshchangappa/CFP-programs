import tkinter as tk
root = tk.Tk()
root.title("Text Example")
text_area = tk.Text(root, height=5,
width=30)
text_area.pack()
root.mainloop()