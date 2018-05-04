from Tkinter import *

master = Tk()

def callback():
	print "click!"

f = Frame(master, height=132, width=32)
f.pack_propagate(0) # don't shrink
f.pack()


b = Button(f, text="OK", command=callback)
b.pack(fill=BOTH, expand=1)



mainloop()


