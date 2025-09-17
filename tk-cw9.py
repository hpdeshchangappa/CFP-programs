import tkinter as tk
root=tk.Tk()
root.title("Text Example")
root.geometry("600x600")
text_area=tk.Text(root,height=5,width=10)
text_area.pack()
root.mainloop()