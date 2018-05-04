from tkinter import filedialog
from tkinter import *
from subprocess import call
from tkinter import ttk
import platform
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
#def use_ls()
	

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

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# tab menu section start
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

notebook = ttk.Notebook(master, width = 480, height = 320)
page1 = Frame(notebook)
page2 = Frame(notebook)
page3 = Frame(notebook)
page4 = Frame(notebook)
notebook.add(page1, text="Sync")
notebook.add(page2, text="LS")
notebook.add(page3, text="Tree")
notebook.add(page4, text="Quit")
notebook.pack()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~
# define frames
# ~~~~~~~~~~~~~~~~~~~~~~~~~~

frame4 = Frame(page1)
frame4.config(bg="white")
frame4.pack(fill=BOTH, expand=TRUE, side=TOP)

frame1 = Frame(page1)
frame1.config(bg="white")
frame1.pack(fill=BOTH, expand=TRUE, side=LEFT)

frame2 = Frame(page1)
frame2.config(bg="white")
frame2.pack(fill=BOTH, expand=TRUE, side=RIGHT)

frame3 = Frame(page1)
frame3.config(bg="white")
frame3.pack(fill=BOTH, expand=TRUE, side=BOTTOM)

frame5 = Frame(page1)
frame5.config(bg="white")
frame5.pack(fill=BOTH, expand=TRUE, side=TOP)

frame6 = Frame(page2)
frame6.config(bg="white")
frame6.pack(fill=BOTH, expand=TRUE, side=TOP)

# ~~~~~~~~~~~~~~~~~~~~~~~~
# creating buttons
# ~~~~~~~~~~~~~~~~~~~~~~~~

welcome = Label(frame4, text="Welcome to the usb696!", font=("Helvetica", 25), bg="white")
welcome.pack()

selFileButton = Button(frame1, text="Select file", command=select_file, relief=FLAT, font=("Helvetica", 17), bg="white")
selFileButton.pack()

selDirButton = Button(frame2, text="Select directory", command=select_dir, relief=FLAT, font=("Helvetica", 17), bg="white")
selDirButton.pack()

selSyncButton = Button(frame3, text="Synchronize files", command=use_rsync, relief=FLAT, font=("Helvetica", 17), bg="white")
selSyncButton.pack() 

welcome2 = Label(frame6, text = "List contents of directory", font = ("Helvetica", 25), bg="white")
welcome2.pack()

testButt = Button(frame6, text="Butt stuff", font=("Helvetica", 25), relief = FLAT, bg="white")
testButt.pack()
# ~~~~~~~~~~~~~~~~~~~~~~~~
# background image
# ~~~~~~~~~~~~~~~~~~~~~~~~

backgroundImage = PhotoImage(file="background6.png")
backgroundLabel = Label(page1, image=backgroundImage)
backgroundLabel.place(x = 0, y = 0, relwidth = 1, relheight = 1)
backgroundLabel.pack(fill=BOTH, expand=TRUE, side=LEFT)
mainloop()
