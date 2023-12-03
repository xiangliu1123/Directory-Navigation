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
      * The application will automatically show in the message box if file is empty.
      * The application shows the current directory path in the window title.
      * In case of access restrictions, an 'Access Denied!' message will be displayed.

    For further assistance, please refer to the application documentation or contact support cwb5722@psu.edu, xbl5229@psu.edu.
    """
    top = tk.Toplevel()
    top.geometry("1000x600")
    top.title(f"Help")
    # Create a text widget for typing
    text = tk.Text(top)
    text.pack(expand=True, fill=tk.BOTH) \
    # Load the content 
    text.insert(tk.END, help_text)