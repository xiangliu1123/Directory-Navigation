import os
import tkinter as tk
from tkinter import simpledialog, messagebox, font as tkfont
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

def show_help():
    help_text = """
Help for Directory Browser:

    - Navigating Directories:
      * The main window displays a list of files and folders.
      * Double-click on a directory name to open it and view its contents.
      * Use the 'Back' button to return to the previous directory.

    - File Operations:
      * 'Create File': Click this button and enter a file name to create a new file in the current directory.
      * 'Read File': Select a file from the list and click this button to view its contents in a new window.
      * 'Write File': Select a file and click this button to open it for editing. You can modify the file and save the changes.
      * 'Delete File': Select a file and click this button to delete it. A confirmation dialog will appear before deletion.

    - Additional Features:
      * The application shows the current directory path in the window title.
      * In case of access restrictions, an 'Access Denied!' message will be displayed.

    For further assistance, please refer to the application documentation or contact support cwb5722@psu.edu
    """
    messagebox.showinfo("Help", help_text)

# Initialize the main window
window = tk.Tk()
window.title("Directory Browser")
window.geometry("800x600")
window.resizable(False, False)
app_font = tkfont.Font(family="Arial", size=12)

# Frame for the listbox and scrollbar
frame = tk.Frame(window)
frame.pack(pady=10)

# Listbox to show directory contents
listbox = tk.Listbox(frame, width=80, height=25, font=app_font)
listbox.bind('<Double-1>', on_double_click)
listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Scrollbar for the listbox
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# Frame for the buttons
button_frame = tk.Frame(window)
button_frame.pack(pady=10)

# Buttons for file operations
create_button = tk.Button(button_frame, text="Create File", command=create_file, font=app_font)
delete_button = tk.Button(button_frame, text="Delete File", command=delete_file, font=app_font)
read_button = tk.Button(button_frame, text="Read File", command=read_file, font=app_font)
write_button = tk.Button(button_frame, text="Write File", command=write_file, font=app_font)
back_button = tk.Button(button_frame, text="Back", command=go_back, font=app_font)
help_button = tk.Button(button_frame, text="Help", command=show_help, font=app_font)

# Organize buttons in a grid
create_button.grid(row=0, column=0, padx=5)
delete_button.grid(row=0, column=1, padx=5)
read_button.grid(row=0, column=2, padx=5)
write_button.grid(row=0, column=3, padx=5)
back_button.grid(row=0, column=4, padx=5)
help_button.grid(row=0, column=5, padx=5)

# Alert label
alert_label = tk.Label(window, text="", fg="red", font=app_font)
alert_label.pack()

# Start in the current directory
list_dir(os.getcwd())

# Start the GUI event loop
window.mainloop()