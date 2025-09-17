import tkinter as tk
from tkinter import ttk

# Main function to display the selected data in the same window
def submit_form():
    # Retrieving the entry field data
    name = entry_name.get()
    srn = entry_srn.get()
    address = text_address.get("1.0", tk.END).strip()  # Get all lines from the Text widget
    state = state_combo.get()
    semester = semester_var.get()
    
    # Retrieving the selected subjects
    selected_subjects = [subject for subject, var in subject_vars.items() if var.get() == 1]
    subjects_text = ", ".join(f'"{subject}"' for subject in selected_subjects)
    
    # Displaying each field separately in their respective labels
    output_label_name.config(text=f'Name: "{name}"')
    output_label_srn.config(text=f'SRN: "{srn}"')
    output_label_address.config(text=f'Address: "{address}"')
    output_label_state.config(text=f'State: "{state}"')
    output_label_subjects.config(text=f'Subjects: {subjects_text}')
    output_label_semester.config(text=f'Semester: "{semester}"')

# Creating the main window
root = tk.Tk()
root.title("Student Form")
root.geometry("300x500")
root.config(bg="lightblue")


# Name Field
tk.Label(root, text="Name:").pack(anchor="w")
entry_name = tk.Entry(root)
entry_name.pack(fill="x", padx=5, pady=2)

# SRN Field
tk.Label(root, text="SRN:").pack(anchor="w")
entry_srn = tk.Entry(root)
entry_srn.pack(fill="x", padx=5, pady=2)

# Address Field (Text area)
tk.Label(root, text="Address:").pack(anchor="w")
text_address = tk.Text(root, height=4, wrap="word")
text_address.pack(fill="x", padx=5, pady=2)

# State ComboBox
tk.Label(root, text="State:").pack(anchor="w")
state_combo = ttk.Combobox(root, values=["Karnataka", "Tamil Nadu", "Kerala", "Andhra Pradesh"])
state_combo.pack(fill="x", padx=5, pady=2)
state_combo.set("Select State")  # Default placeholder text

# Semester Radio Buttons
frame_semester = tk.Frame(root)
frame_semester.pack(pady=5, anchor="w")

tk.Label(frame_semester, text="Semester:").pack(side="left")
semester_var = tk.StringVar()
semester_var.set("1st")  # Default selection

tk.Radiobutton(frame_semester, text="1st", variable=semester_var, value="1st").pack(side="left")
tk.Radiobutton(frame_semester, text="2nd", variable=semester_var, value="2nd").pack(side="left")

# Subject Checkboxes
frame_subjects = tk.Frame(root)
frame_subjects.pack(pady=5, anchor="w")

tk.Label(frame_subjects, text="Subjects:").pack(anchor="w")
subject_vars = {
    "CFP": tk.IntVar(),
    "WB": tk.IntVar(),
    "MP": tk.IntVar(),
    "MFCA": tk.IntVar(),
    "DS": tk.IntVar(),
    "DBMS": tk.IntVar()
}

# Create checkboxes for each subject
for subject, var in subject_vars.items():
    tk.Checkbutton(frame_subjects, text=subject, variable=var).pack(anchor="w")

# Submit Button
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.pack(pady=10)

# Output Labels for displaying each field separately in the same window
output_frame = tk.Frame(root)
output_frame.pack(fill="x", pady=10)

output_label_name = tk.Label(output_frame, text="", justify="left", font=("Arial", 10), fg="blue")
output_label_name.pack(anchor="w")

output_label_srn = tk.Label(output_frame, text="", justify="left", font=("Arial", 10), fg="blue")
output_label_srn.pack(anchor="w")

output_label_address = tk.Label(output_frame, text="", justify="left", font=("Arial", 10), fg="blue")
output_label_address.pack(anchor="w")

output_label_state = tk.Label(output_frame, text="", justify="left", font=("Arial", 10), fg="blue")
output_label_state.pack(anchor="w")

output_label_subjects = tk.Label(output_frame, text="", justify="left", font=("Arial", 10), fg="blue")
output_label_subjects.pack(anchor="w")

output_label_semester = tk.Label(output_frame, text="", justify="right", font=("Arial", 10), fg="blue")
output_label_semester.pack(anchor="e")

# Run the application
root.mainloop()
