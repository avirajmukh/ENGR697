from tkinter import filedialog
from tkinter import *
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

# runs LS command to list files in directories, either specified or current
def use_ls()
	

#This function destroys and exits the program when called
def on_escape(event=None):
    print("Exiting program")
    app.tk.destroy()
# ~~~~~~~~~~~~~~~~~~~~~~~~
# GUI section
# ~~~~~~~~~~~~~~~~~~~~~~~~

master = Tk()
master.geometry("480x320")
master.title("File Transfer Device")

welcome = Label(master, text="Welcome to the usb696!", font=("Helvetica", 25))
welcome.pack()

# ~~~~~~~~~~~~~~~~~~~~~~~~
# different frames
# ~~~~~~~~~~~~~~~~~~~~~~~~

frame1 = Frame(master)
frame1.pack(fill=BOTH, expand=TRUE, side=LEFT)

frame2 = Frame(master)
frame2.pack(fill=BOTH, expand=TRUE, side=RIGHT)

frame3 = Frame(master)
frame3.pack(fill=BOTH, expand=TRUE, side=BOTTOM)

# ~~~~~~~~~~~~~~~~~~~~~~~~
# creating buttons
# ~~~~~~~~~~~~~~~~~~~~~~~~
selFileButton = Button(frame1, text="Select file", command=select_file, relief=FLAT,  font=("Helvetica", 17))
# selFileButtonWindow = background.create_window(10, 10, window = selFileButton)
selFileButton.pack(side=TOP, pady=1)

selDirButton = Button(frame2, text="Select directory", command=select_dir, relief=FLAT,  font=("Helvetica", 17))
selDirButton.pack(side=TOP, pady=1)

selSyncButton = Button(frame3, text="Synchronize files", command=use_rsync, relief=FLAT, font=("Helvetica", 17))
selSyncButton.pack(side=BOTTOM) 
# ending button portion

# ~~~~~~~~~~~~~~~~~~~~~~~~
# menu section 
# ~~~~~~~~~~~~~~~~~~~~~~~~

menu = Menu(master)
master.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="directory", command=select_dir)
filemenu.add_command(label="synchronize", command=use_rsync)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=master.quit)


mainloop()
