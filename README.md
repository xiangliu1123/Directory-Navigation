# Directory Browser

## Goal of the Project

The primary objective of the Directory Browser project is to provide a user-friendly, intuitive file management system. This application aims to simplify the process of navigating, creating, reading, editing, and deleting files for users, especially focusing on the needs of the elderly who may require a more accessible and straightforward interface.

## Significance of the Project

This project significantly enhances the digital experience for the elderly by offering a simplified interface that minimizes complexity and cognitive load. It addresses common challenges faced by older adults, such as difficulty in navigating complex file systems and performing basic file operations. By providing an easy-to-use tool, it helps bridge the digital divide, empowering the elderly to manage their digital files independently and confidently.

## Installation and Instruction to Use
### Prerequisite
- Make you have Python installed in your current working environment
- Download integrated Development Environments (IDEs) or use CMD or Powershell with a download repository
- Ensure Python and Tkinter are installed on your work system environment. Tkinter usually comes with Python when downloading Python on your local machine.

### Installation
Step 1: Git Clone or download the repository as a zip to your local machine.
The command for git clone in the terminal: 
```bash
Git Clone https://github.com/xiangliu1123/Directory-Navigation
```
Downloading the repository as a zip to your local machine can follow this link: https://github.com/xiangliu1123/Directory-Navigation 

Step 2: Navigate or use the command in the terminal to the directory containing the `directory_browser.py` file.
Terminal Command:
```bash
cd src
```
### Run the script

Run the script in the terminal using Python:

```bash
python directory_browser.py
```

- Use the GUI to navigate directories, create, read, edit, and delete files. Detailed instructions can be accessed via the 'Help' button in the application.

### Structure of the Code
1.	Main Window Initialization: Creation of the Tkinter window, setting its title, geometry, and font.
2.	GUI Components: Listbox for directory contents, scrollbar, and buttons for file operations (create, delete, read, write, back, help).
3.	Event Bindings: Linking GUI elements to their respective functions (e.g., double-click event on the list box).
4.	File Operations Functions: list_dir, create_file, delete_file, read_file, write_file, each performing specific file operations.
5.	Utility Functions: on_double_click, go_back, show_help, handling user interactions like navigation and displaying help.
6.	File Interaction: Reading from and writing to files in the current directory.
7.	Main Loop: The execution point that keeps the GUI running.

### Detailed explanations of each component:

- list_dir(): Handles directory listing and navigation.
on_double_click(): Event handler for opening directories.

- go_back(): Navigates to the previous directory.

- create_file(), read_file(), write_file(), delete_file(): Handle file operations.
show_help(): Displays instructions and help information.

## Functionalities and Test Results

### Functionalities

Directory Navigation
File Creation
File Reading
File Editing
File Deletion
Help Section
### Test Results
The application was tested for various scenarios including directory navigation, file operations, and error handling. It performed reliably, with intuitive responses to user actions.

## Discussion and Conclusions
The project successfully meets its objectives but is not without limitations. It currently lacks advanced features like search functionality and bulk operations, which could be future enhancements. The application of course learnings is evident in the structured programming approach and user-centric design, highlighting the importance of accessibility in software development.

Overall, the Directory Browser stands as a testament to the potential impact of technology in enhancing the lives of the elderly.
