import tkinter as tk
from tkinter import messagebox

def submit():
    name_value = entries["name"].get()
    srno_value = entries["srno"].get()
    address_value = entries["address"].get("1.0", tk.END).strip()  # Get text from Text widget

    if not (name_value and srno_value and address_value):
        messagebox.showerror("Error", "All fields are required")
    else:
        messagebox.showinfo("Submitted", f"Name: {name_value}\nSrNo: {srno_value}\nAddress: {address_value}")

root = tk.Tk()
root.title("Registration Form")

# Create a frame for label-entry pairs
form_frame = tk.Frame(root)
form_frame.pack(padx=10, pady=10)

# Dictionary to hold references to entry fields
entries = {}

# Function to create label and entry in horizontal layout
def add_field(label_text, field_key, is_text_area=False):
    frame = tk.Frame(form_frame)
    frame.pack(fill='x', pady=5)

    tk.Label(frame, text=label_text, width=10, anchor='w').pack(side='left')

    if is_text_area:
        entry = tk.Text(frame, height=4, width=30)  # Create Text widget for multiline input
        entry.pack(side='right', fill='x', expand=True)
    else:
        entry = tk.Entry(frame)  # Create Entry widget for single-line input
        entry.pack(side='right', fill='x', expand=True)

    entries[field_key] = entry  # Store widget in dictionary

# Add form fields
add_field("Name", "name")
add_field("SrNo", "srno")
add_field("Address", "address", is_text_area=True)  # Make Address a Text area

# Add submit button
tk.Button(root, text="Submit", command=submit).pack(pady=20)

root.mainloop()
