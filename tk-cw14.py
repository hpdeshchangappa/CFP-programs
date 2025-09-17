import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("simple Combobox Example")
root.geometry("400x200")

languages=["JAVA","Python","Dart","orange","go","C++","javascript"]
combobox = ttk.Combobox(root, values=languages)
combobox.pack(pady=10)
root.mainloop()