from tkinter import filedialog
from tkinter import *
from guizero import App, Text, PushButton
from subprocess import call

file_check = False
dir_check = False

def select_file():
    global filename
    filename =  filedialog.askopenfilename(initialdir = "C:\\", title = "Select file")
    curr_file.value = "Current file: " + filename
    global file_check
    file_check = True

def select_dir():
    global directory
    directory =  filedialog.askdirectory()
    curr_dir.value = "Current directory " + directory
    global dir_check
    dir_check = True

def use_rsync():
    if (file_check and dir_check):
        sync_text.value = "File sent to destination"
        args = ["rsync", filename, directory]
        print(args)
        call(args)
    else:
        sync_text.value = "Please select a source file and destination folder"

app = App(title="USB Transfer Device", width=480, height=320) 
#   480x320 should be the resolution of the touch screen)
welcome_message = Text(app, text="Please choose a source file and a destination directory")

file_button = PushButton(app, command=select_file, text="Select a source file", grid=[0,1])
curr_file = Text(app, text="Current file: ", grid=[1,1])

dir_button = PushButton(app, command=select_dir, text="Select a destination directory", grid=[2,1])
curr_dir = Text(app, text="Current directory: ", grid=[3,1])

sync_button = PushButton(app, command=use_rsync, text="Sync Files to Destination", grid=[5,1])
sync_text = Text(app, text="", grid=[6,1])


app.display()

