import tkinter as tk

root1=tk.Tk()


root1.title("place() example()")
root1.geometry("900x400")
label1=tk.Label(root1,text="Bold Text" ,weight="bold",size=12)
label2=tk.Label(root1,text="Italics" ,slant="italic")
label3=tk.Label(root1,text="Underline" ,underline=1)
label4=tk.Label(root1, text="Custom Color", bg="yellow", fg="blue")
label5=tk.Label(root, text="Right Aligned", anchor="e")
label6=tk.Label(root1,text="With Border", relief="solid", bd=2, padx=10, pady=5)
label7=tk.Label(root1,text="Padded Text", padx=20, pady=10)
label1.place(x=100,y=100)
label2.place(x=100,y=100)
label3.place(x=100,y=100)
label4.place(x=100,y=100)
label5.place(x=100,y=100)
label6.place(x=100,y=100)
label7.place(x=100,y=100)

root1.mainloop()


# import tkinter as tk
# root=tk.Tk()
# root.title("pack() example()")
# root.geometry("900x400")
# label1=tk.Label(root,text="labe1" ,bg="lightblue")
# label2=tk.Label(root,text="labe2" ,bg="lightgreen")
# label3=tk.Label(root,text="labe3" ,bg="lightyellow")
# 
# label1.pack(side="top")
# label2.pack(side="left")
# label3.pack(side="right")
# 
# root.mainloop()
