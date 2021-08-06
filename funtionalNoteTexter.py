"""
Note Texter is a text editor made for editing txt files.

Author: Rishaw
Author-Email: ratneshthakur.40@gmail.com or rishav.9212@gmail.com
"""

# This is not based on object oriented programming
import os
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile, askopenfilename

app = Tk()
app.title("Note Texter")

# frame 1
frame1 = Frame(app, relief=None)
frame1.pack()

# frame 2
frame2 = Frame(app, relief=None)
frame2.pack(fill=BOTH, expand=True)


def openFile():
    global filename
    filename = askopenfilename(parent=app, filetype=[("TXT file", "*.txt")])
    if filename is None:
        messagebox.showinfo("Info", "Nothing is selected", parent=app)
    else:
        try:
            file = open(filename, "r")
            app.title(os.path.basename(filename) + " - Note Texter")
            t1.delete("1.0", "end")
            t1.insert(END, file.read())
        except Exception as e:
            messagebox.showerror("Error", e, parent=app)


def saveFile():
    file = open(filename, "w")
    file.write(t1.get("1.0", END))
    file.close()


# frame 1 components
b1 = Button(frame1, text="Open", command=lambda: openFile()) # This is button for opening a file
b1.grid(row=0, column=0)

b2 = Button(frame1, text="Save", command=lambda: saveFile()) # This is button for saving a file
b2.grid(row=0, column=1)

b3 = Button(frame1, text="Exit", command=exit) # This is button for closing the window
b3.grid(row=0, column=2)

# frame 2 components
t1 = Text(frame2, font=("cascadia code", 10))
t1.pack(fill=BOTH, expand=True)

app.mainloop()
