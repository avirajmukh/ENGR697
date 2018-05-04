from tkinter import filedialog
from tkinter import *
from subprocess import call
from tkinter import ttk
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





# ~~~~~~~~~~~~~~~~~~~~~~~~
# different frames
# ~~~~~~~~~~~~~~~~~~~~~~~~


# ending button portion

# ~~~~~~~~~~~~~~~~~~~~~~~~
# top menu section start
# ~~~~~~~~~~~~~~~~~~~~~~~~

# menu = Menu(master)
# master.config(menu=menu)
# filemenu = Menu(menu)
# menu.add_cascade(label="File", menu=filemenu)
# filemenu.add_command(label="directory", command=select_dir)
# filemenu.add_command(label="synchronize", command=use_rsync)
# filemenu.add_separator()
# filemenu.add_command(label="Exit", command=master.quit)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# weird tab  menu section start
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

notebook = ttk.Notebook(master)
notebook.pack()                  
page1 = Frame(notebook)         
page2 = Frame(notebook)

notebook.add(page1, text="Tab 1")
notebook.add(page2, text="Tab 2")
notebook.pack()


frame4 = Frame(master)
frame4.config(bg="white")
frame4.pack(fill=BOTH, expand=TRUE, side=TOP)

frame1 = Frame(master)
frame1.config(bg="white")
frame1.pack(fill=BOTH, expand=TRUE, side=LEFT)

frame2 = Frame(master)
frame2.config(bg="white")
frame2.pack(fill=BOTH, expand=TRUE, side=RIGHT)

frame3 = Frame(master)
frame3.config(bg="white")
frame3.pack(fill=BOTH, expand=TRUE, side=BOTTOM)

# ~~~~~~~~~~~~~~~~~~~~~~~~
# creating buttons
# ~~~~~~~~~~~~~~~~~~~~~~~~

selFileButton = Button(frame1, text="Select file", command=select_file, relief=FLAT, font=("Helvetica", 17), bg="white")
selFileButton.pack(anchor = "w")

selDirButton = Button(frame2, text="Select directory", command=select_dir, relief=FLAT, font=("Helvetica", 17), bg="white")
selDirButton.pack(anchor = "e")

selSyncButton = Button(frame3, text="Synchronize files", command=use_rsync, relief=FLAT, font=("Helvetica", 17), bg="white")
selSyncButton.pack(side=BOTTOM) 

welcome = Label(frame4, text="Welcome to the usb696!", font=("Helvetica", 25), bg="white")
welcome.pack(side=TOP)

selFileButton = Button(frame1, text="Select file", command=select_file, relief=FLAT, font=("Helvetica", 17), bg="white")
selFileButton.pack(anchor = "w")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~
# weird tab menu section end
# ~~~~~~~~~~~~~~~~~~~~~~~~~~

backgroundImage = PhotoImage(file="screenshot5.png")
backgroundLabel = Label(master, image=backgroundImage)
backgroundLabel.place(x = 0, y = 0, relwidth = 1, relheight = 1)
backgroundLabel.pack(fill=BOTH, expand=TRUE, side=LEFT)

mainloop()
