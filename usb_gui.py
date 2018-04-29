from tkinter import filedialog
from tkinter import *
from guizero import App, Text, PushButton
from subprocess import call

# Setting initial boolean values to check for the file and directory selection
file_check = False
dir_check = False

# Opens a file dialog to select a file in the filesystem
def select_file():
    global filename
    filename =  filedialog.askopenfilename(initialdir = "C:\\", title = "Select file")
    curr_file.value = "Current file: " + filename
    global file_check
    file_check = True

# Opens a file dialog to select a directory in the filesystem
def select_dir():
    global directory
    directory =  filedialog.askdirectory()
    curr_dir.value = "Current directory " + directory
    global dir_check
    dir_check = True

# runs the rsync linux command to sync files to destination directories
def use_rsync():
    if (file_check and dir_check):
        sync_text.value = "File sent to destination"
        args = ["rsync", filename, directory]
        print(args)
        call(args)
    else:
        sync_text.value = "Please select a source file and destination folder"

#This function destroys and exits the program when called
def on_escape(event=None):
    print("Exiting program")
    app.tk.destroy()

app = App(title="USB Transfer Device", width=480, height=320) 
#   480x320 should be the resolution of the touch screen)
welcome_message = Text(app, text="Please choose a source file and a destination directory")

#   Establishes buttons for file / directory selection and sync
file_button = PushButton(app, command=select_file, text="Select a source file", grid=[0,1])
curr_file = Text(app, text="Current file: ", grid=[1,1])

dir_button = PushButton(app, command=select_dir, text="Select a destination directory", grid=[2,1])
curr_dir = Text(app, text="Current directory: ", grid=[3,1])

sync_button = PushButton(app, command=use_rsync, text="Sync Files to Destination", grid=[5,1])
sync_text = Text(app, text="", grid=[6,1])

app.tk.attributes("-fullscreen", True)  #force the app to run in fullscreen
app.tk.bind("<Escape>", on_escape)      #Binds the escape key on a keyboard to the on_escape function
app.display()

