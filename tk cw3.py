import tkinter as tk
root=tk.Tk()
root.title("pack() example()")
root.geometry("900x400")
label1=tk.Label(root,text="label1" ,bg="lightblue")
label2=tk.Label(root,text="label2" ,bg="lightgreen")
label3=tk.Label(root,text="label3" ,bg="lightyellow")

label1.pack(side="top")
label2.pack(side="left")
label3.pack(side="right")
 
root.mainloop()
