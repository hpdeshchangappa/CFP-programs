import tkinter as tk

def send_message():
    message_label.config(text="Message Sent")

def accept_message():
    message_label.config(text="Message Accepted")

root = tk.Tk()
root.title("Message Sender")
root.geometry("350x350")

# Create a label to display messages
message_label = tk.Label(root, text="Click a button", font=('Helvetica', 20),)
message_label.pack(pady=20)

# Create the "Send" button
send_button = tk.Button(root,
text="Send",
command=send_message,
font=('Courier', 10),
bg="lightgreen",
fg="darkgreen",
width=10,
height=3)
send_button.pack(side=tk.LEFT, padx=30, pady=30)

# Create the "Accept" button
accept_button = tk.Button(root,
text="Accept",
command=accept_message,
font=('Courier', 10),
bg="lightblue",
fg="darkblue",
width=10,
height=3)
accept_button.pack(side=tk.RIGHT, padx=30, pady=30)

root.mainloop()