import tkinter
from tkinter import filedialog
from tkinter import *
from subprocess import call
from tkinter import ttk
import platform
import os
import glob


dir_check = False
file_check = False

master = Tk()
master.geometry("480x320")
master.title("File Transfer Device")

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

# show and hide the scrollbar, taken from dirbrowser.py
def autoscroll(sbar, first, last):
    first, last = float(first), float(last)
    if first <= 0 and last >= 1:
        sbar.grid_remove()
    else:
        sbar.grid()
    sbar.set(first, last)

def populate_tree(tree, node):
    if tree.set(node, "type") != 'directory':
        return

    path = tree.set(node, "fullpath")
    tree.delete(*tree.get_children(node))

    parent = tree.parent(node)
    special_dirs = [] if parent else glob.glob('.') + glob.glob('..')

    for p in special_dirs + os.listdir(path):
        ptype = None
        p = os.path.join(path, p).replace('\\', '/')
        if os.path.isdir(p): ptype = "directory"
        elif os.path.isfile(p): ptype = "file"

        fname = os.path.split(p)[1]
        id = tree.insert(node, "end", text=fname, values=[p, ptype])

        if ptype == 'directory':
            if fname not in ('.', '..'):
                tree.insert(id, 0, text="dummy")
                tree.item(id, text=fname)
        elif ptype == 'file':
            size = os.stat(p).st_size
            tree.set(id, "size", "%d bytes" % size)


def populate_roots(tree):
    dir = os.path.abspath('.').replace('\\', '/')
    node = tree.insert('', 'end', text=dir, values=[dir, "directory"])
    populate_tree(tree, node)	# show and hide the scrollbar, taken from dirbrowser.py
def autoscroll(sbar, first, last):
    first, last = float(first), float(last)
    if first <= 0 and last >= 1:
        sbar.grid_remove()
    else:
        sbar.grid()
    sbar.set(first, last)

def populate_tree(tree, node):
    if tree.set(node, "type") != 'directory':
        return

    path = tree.set(node, "fullpath")
    tree.delete(*tree.get_children(node))

    parent = tree.parent(node)
    special_dirs = [] if parent else glob.glob('.') + glob.glob('..')

    for p in special_dirs + os.listdir(path):
        ptype = None
        p = os.path.join(path, p).replace('\\', '/')
        if os.path.isdir(p): ptype = "directory"
        elif os.path.isfile(p): ptype = "file"

        fname = os.path.split(p)[1]
        id = tree.insert(node, "end", text=fname, values=[p, ptype])

        if ptype == 'directory':
            if fname not in ('.', '..'):
                tree.insert(id, 0, text="dummy")
                tree.item(id, text=fname)
        elif ptype == 'file':
            size = os.stat(p).st_size
            tree.set(id, "size", "%d bytes" % size)


def populate_roots(tree):
    dir = os.path.abspath('.').replace('\\', '/')
    node = tree.insert('', 'end', text=dir, values=[dir, "directory"])
    populate_tree(tree, node)

#This function destroys and exits the program when called
def on_escape(event=None):
    print("Exiting program")
    master.destroy()

def list_contents(event=None):

master.bind("<Escape>", on_escape)


# ~~~~~~~~~~~~~~~~~~~~~~~~
# GUI section
# ~~~~~~~~~~~~~~~~~~~~~~~~



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# tab menu section start
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

notebook = ttk.Notebook(master, width = 480, height = 320)
page1 = Frame(notebook)
page2 = Frame(notebook)
page3 = Frame(notebook)
page4 = Frame(notebook)
notebook.add(page1, text="Sync")
notebook.add(page2, text="Tree")
# notebook.add(page3, text="Tree")
# notebook.add(page4, text="Quit")
notebook.pack()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~
# define frames
# ~~~~~~~~~~~~~~~~~~~~~~~~~~

# 
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

frame7 = Frame(page3)
frame7.config(bg="white")
frame7.pack(fill=BOTH, expand=TRUE, side=TOP)

# ~~~~~~~~~~~~~~~~~~~~~~~~
# creating buttons
# ~~~~~~~~~~~~~~~~~~~~~~~~

welcome = Label(frame4, text="Welcome to the usb696!", font=("Helvetica", 25), bg="white")
welcome.pack()

selFileButton = Button(frame1, text="Select file", command=select_file, relief=FLAT, font=("Helvetica", 13), bg="white")
selFileButton.pack()

selDirButton = Button(frame2, text="Select directory", command=select_dir, relief=FLAT, font=("Helvetica", 13), bg="white")
selDirButton.pack()

selSyncButton = Button(frame3, text="Synchronize files", command=use_rsync, relief=FLAT, font=("Helvetica", 13), bg="white")
selSyncButton.pack() 


#Creating Main Label and Frames
welcome_msg = Label(frame6, text="Please choose a source file and a destination directory")
welcome_msg.pack()

syncFrame = Frame(frame6)
syncFrame.pack(fill=X, side=BOTTOM)

srcFrame = Frame(frame6)
srcFrame.pack(fill=BOTH, expand=TRUE, side=LEFT)

destFrame = Frame(frame6)
destFrame.pack(fill=BOTH, expand=TRUE, side=RIGHT)

#Creating Buttons, Labels and Entry fields for each frame
file_lbl = Label(srcFrame, text="Current file: ")
file_lbl.pack(fill=BOTH, side=TOP)
curr_file = Entry(srcFrame, state='disabled')
curr_file.pack(fill=X, side=TOP)
file_btn = Button(srcFrame, text="Select a source file", command=select_file)
file_btn.pack(fill=X, side=TOP)

dir_label = Label(destFrame, text="Current directory: ")
dir_label.pack(fill=BOTH, side=TOP)
curr_dir = Entry(destFrame, state='disabled')
curr_dir.pack(fill=X, side=TOP)
dir_btn = Button(destFrame, text="Select a destination folder", command=select_dir)
dir_btn.pack(fill=X, side=TOP)

sync_btn = Button(syncFrame, text="Sync file to destination", command=use_rsync)
sync_btn.pack(fill=BOTH, side=BOTTOM)
sync_text = Label(syncFrame, text="")
sync_text.pack(fill=BOTH, side=BOTTOM)

#master.attributes("-fullscreen", True)  #force the master to run in fullscreen
master.bind("<Escape>", on_escape)

#creating file browser using tree view
f_vsb = ttk.Scrollbar(orient="vertical")
f_hsb = ttk.Scrollbar(orient="horizontal")

d_vsb = ttk.Scrollbar(orient="vertical")
d_hsb = ttk.Scrollbar(orient="horizontal")

file_tree = ttk.Treeview(srcFrame, columns=("fullpath", "type", "size"),
    displaycolumns="size", yscrollcommand=lambda f, l: autoscroll(f_vsb, f, l),
    xscrollcommand=lambda f, l:autoscroll(f_hsb, f, l))

dir_tree = ttk.Treeview(destFrame, columns=("fullpath", "type", "size"),
    displaycolumns="size", yscrollcommand=lambda f, l: autoscroll(d_vsb, f, l),
    xscrollcommand=lambda f, l:autoscroll(d_hsb, f, l))

f_vsb['command'] = file_tree.yview
f_hsb['command'] = file_tree.xview

d_vsb['command'] = file_tree.yview
d_hsb['command'] = file_tree.xview

file_tree.heading("#0", text="Directory Structure", anchor='w')
file_tree.heading("size", text="File Size", anchor='w')
file_tree.column("size", stretch=0, width=100)

dir_tree.heading("#0", text="Directory Structure", anchor='w')
dir_tree.heading("size", text="File Size", anchor='w')
dir_tree.column("size", stretch=0, width=100)

populate_roots(file_tree)
populate_roots(dir_tree)

file_tree.pack(fill=X)
dir_tree.pack(fill=X)



# ~~~~~~~~~~~~~~~~~~~~~~~~
# background image
# ~~~~~~~~~~~~~~~~~~~~~~~~

backgroundImage = PhotoImage(file="background6.png")
backgroundLabel = Label(page1, image=backgroundImage)
backgroundLabel.place(x = 0, y = 0, relwidth = 1, relheight = 1)
backgroundLabel.pack(fill=BOTH, expand=TRUE, side=LEFT)
mainloop()
