import tkinter as tk

def display_message():
    # Create second window
    second_window = tk.Toplevel(root)
    second_window.title("Message Window")
    second_window.geometry("300x100")
    
    # Create label with the message
    message_label = tk.Label(second_window, text="Good Morning My Dear Queen",
                             font=('Comic Sans MS', 16),bg="lightblue")
    message_label.pack(pady=20)

# Create the main window
root = tk.Tk()
root.title("Main Window")
root.geometry("300x150")

# Create the button to trigger the message in the second window
send_button = tk.Button(root, text="Click Me",
command=display_message,
bg="lightblue",
fg="black",
width=10,
height=2)
send_button.pack(pady=20)

root.mainloop()
