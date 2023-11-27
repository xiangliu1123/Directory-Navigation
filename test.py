import os
import tkinter as tk
from tkinter import simpledialog, messagebox

def list_dir(path):
    try:
        # Clear the current list
        listbox.delete(0, tk.END)
        for item in os.listdir(path):
            listbox.insert(tk.END, item)
        os.chdir(path)
        window.title(f"Directory Browser - {os.getcwd()}")
    except PermissionError:
        # In case of permission error, show an alert
        alert_label.config(text="Access Denied!")

def on_double_click(event):
    widget = event.widget
    selection = widget.curselection()
    if selection:
        item = widget.get(selection[0])
        new_path = os.path.join(os.getcwd(), item)
        if os.path.isdir(new_path):
            list_dir(new_path)

def go_back():
    os.chdir('..')
    list_dir(os.getcwd())

def create_file():
    file_name = simpledialog.askstring("Input", "Enter filename:", parent=window)
    if file_name:
        with open(file_name, 'w') as f:
            pass
        list_dir(os.getcwd())

def read_file():
    selected = listbox.curselection()
    if selected:
        file_name = listbox.get(selected[0])
        if os.path.isfile(file_name):
            with open(file_name, 'r') as f:
                content = f.read()
            messagebox.showinfo("Read File", content)

def delete_file():
    selected = listbox.curselection()
    if selected:
        file_name = listbox.get(selected[0])
        if messagebox.askyesno("Delete", f"Delete {file_name}?"):
            os.remove(file_name)
            list_dir(os.getcwd())

def write_file():
    selected = listbox.curselection()
    if selected:
        file_name = listbox.get(selected[0])
        if os.path.isfile(file_name):
            content = simpledialog.askstring("Input", "Enter content to write:", parent=window)
            with open(file_name, 'w') as f:
                f.write(content)
            messagebox.showinfo("Write File", f"Written to {file_name}")

# Initialize the main window
window = tk.Tk()
window.title("Directory Browser")
window.geometry("600x400")

# Listbox to show directory contents
listbox = tk.Listbox(window, width=100, height=20)
listbox.bind('<Double-1>', on_double_click)
listbox.pack()

# Buttons for file operations
create_button = tk.Button(window, text="Create File", command=create_file)
create_button.pack()
delete_button = tk.Button(window, text="Delete File", command=delete_file)
delete_button.pack()
read_button = tk.Button(window, text="Read File", command=read_file)
read_button.pack()
write_button = tk.Button(window, text="Write File", command=write_file)
write_button.pack()

# Back button
back_button = tk.Button(window, text="Back", command=go_back)
back_button.pack()

# Alert label
alert_label = tk.Label(window, text="", fg="red")
alert_label.pack()

# Start in the current directory
list_dir(os.getcwd())

# Start the GUI event loop
window.mainloop()