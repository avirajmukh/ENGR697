import os
import glob
import tkinter
from tkinter import filedialog
from tkinter import *
from tkinter import ttk
from subprocess import call

# Setting initial boolean values to check for the file and directory selection
file_check = False
dir_check = False

# Opens a file dialog to select a file in the filesystem
def select_file():
    global filename
    #filename =  filedialog.askopenfilename(initialdir = "C:\\", title = "Select file")
    filename =  filedialog.askopenfilename()
    curr_file.config(state='normal')
    curr_file.delete(0,END)
    curr_file.insert(0,filename)
    curr_file.config(state='disabled')
    curr_file.config(text = "Current file: " + filename)
    global file_check
    file_check = True

# Opens a file dialog to select a directory in the filesystem
def select_dir():
    global directory
    directory =  filedialog.askdirectory()
    curr_dir.config(state='normal')
    curr_dir.delete(0,END)
    curr_dir.insert(0,directory)
    curr_dir.config(state='disabled')
    global dir_check
    dir_check = True

# runs the rsync linux command to sync files to destination directories
def use_rsync():
    if (file_check and dir_check):
        sync_text.config(text = "File Transferred")
        args = ["rsync", filename, directory]
        print(args)
        call(args)
    else:
        sync_text.config(text = "ERROR: Missing File / Dir")

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
    populate_tree(tree, node)

#This function destroys and exits the program when called
def on_escape(event=None):
    print("Exiting program")
    app.destroy()


#Creating GUI Window
app = Tk()
app.title("USB Transfer Device and Server")
app.geometry('480x320')

#Creating Main Label and Frames
welcome_msg = Label(app, text="Please choose a source file and a destination directory")
welcome_msg.pack()

syncFrame = Frame(app)
syncFrame.pack(fill=X, side=BOTTOM)

srcFrame = Frame(app)
srcFrame.pack(fill=BOTH, expand=TRUE, side=LEFT)

destFrame = Frame(app)
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

#app.attributes("-fullscreen", True)  #force the app to run in fullscreen
app.bind("<Escape>", on_escape)

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

app.mainloop()