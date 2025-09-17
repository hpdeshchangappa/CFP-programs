import tkinter as tk
def on_click():
    print("button clicked")

root=tk.Tk()
root.geometry("200x200")

btn1=tk.Button(root,text="click me",command=on_click,
               height=2,width=8,
               bg="lightblue",state="normal",
               relief="raised",
               activebackground="pink",bd=2)
btn1.pack(pady=40)

root.mainloop()