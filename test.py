import os
import tkinter as tk
from tkinter import simpledialog, messagebox
from tkinter import scrolledtext
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
            if content == "":
              
                messagebox.showinfo(title= file_name, message="File is empty")
            else:
                # Create a new top-level window
                top = tk.Toplevel()
                top.geometry("1000x600")
                top.title(file_name)

                # Create a scrollable text widget
                text = tk.Text(top)
                text.insert(tk.END, content)
                text.config(state=tk.DISABLED)  # Make the text widget read-only

                # Create a scrollbar
                scrollbar = tk.Scrollbar(top)
                scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
                scrollbar.pack(side=tk.BOTTOM, fill=tk.X)

                # Attach scrollbar to text widget
                text.config(yscrollcommand=scrollbar.set)
                scrollbar.config(command=text.yview)
                text.config(xscrollcommand=scrollbar.set)
                scrollbar.config(command=text.xview)

                # Pack the text widget
                text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
                text.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
                

def delete_file():
    selected = listbox.curselection()
    if selected:
        file_name = listbox.get(selected[0])
        if messagebox.askyesno("Delete", f"Delete {file_name}?"):
            os.remove(file_name)
            list_dir(os.getcwd())

def write_file():
    selected = listbox.curselection()
    content = ''
    if selected:
        file_name = listbox.get(selected[0])
        if os.path.isfile(file_name):
            
            # Create a new top-level window
            top = tk.Toplevel()
            top.geometry("1000x600")
            top.title(f"Edit {file_name}")

            # Create a text widget for typing
            text = tk.Text(top)
            text.pack(expand=True, fill=tk.BOTH)

            # Create a scrollbar
            scrollbar = tk.Scrollbar(top)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
            scrollbar.pack(side=tk.BOTTOM, fill=tk.X)

            # Attach scrollbar to text widget
            text.config(yscrollcommand=scrollbar.set)
            scrollbar.config(command=text.yview)
            text.config(xscrollcommand=scrollbar.set)
            scrollbar.config(command=text.xview)


            # Load the content of the file into the text widget
            with open(file_name, 'r') as f:
                content = f.read()
            text.insert(tk.END, content)


            # Function to handle save action
            def save_content():
                content = text.get("1.0", tk.END)
                with open(file_name, 'a') as f:
                    f.write(content)
                messagebox.showinfo("Write File", f"Saved to {file_name}")
                top.destroy()

            # Add a save button
            save_button = tk.Button(top, text="Save", command=save_content)
            save_button.pack()

            # Add a cancel button
            cancel_button = tk.Button(top, text="Cancel", command=top.destroy)
            cancel_button.pack()

# Initialize the main window
window = tk.Tk()
window.title("Directory Browser")
window.geometry("700x500")

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