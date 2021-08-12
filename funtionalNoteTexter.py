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
from tkinter.filedialog import askopenfilename, asksaveasfilename
from speakText import speak

app = Tk()
app.title("Note Texter")

# frame 1
frame1 = Frame(app, relief=None)
frame1.pack(fill=BOTH, expand=True)

# Created menu bar
menuBar = Menu(app)

# Scroll View in Text widget
scrollbarY = Scrollbar(frame1)
scrollbarY.pack(side=RIGHT, fill=Y)


def newFile():
    global filename
    app.title("Untitled - Notepad")
    filename = None
    t1.delete(1.0, END)


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
            file.close()
        except Exception as e:
            messagebox.showerror("Error", e, parent=app)


def saveFile():
    global filename
    if filename == None:
        filename = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt",
                                     filetypes=[("All Files", "*.*"),
                                                ("Text Documents", "*.txt")])
        if filename == "":
            filename = None

        else:
            f = open(filename, "w")
            f.write(t1.get(1.0, END))
            f.close()

            app.title(os.path.basename(filename) + " - Notepad")
            print("File Saved")
    else:
        f = open(filename, "w")
        f.write(t1.get('1.0', END))
        f.close()

def saveAsFile():
    global filename
    filename = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt",
                                     filetypes=[("All Files", "*.*"),
                                                ("Text Documents", "*.txt")])

    f = open(filename, "w")
    f.write(t1.get('1.0', END))
    f.close()
    app.title(os.path.basename(filename) + " - Note Texter")
    


# Adding File Menu and commands
file = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label='File', menu=file)
file.add_command(label='New File', command=lambda: newFile())
file.add_command(label='Open...', command=lambda: openFile())
file.add_command(label='Save', command=lambda: saveFile()) 
file.add_command(label='Save As', command=lambda: saveAsFile()) 
file.add_separator()
file.add_command(label='Exit', command=app.destroy)

power = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label='Power', menu=power)
power.add_command(label='Read the text', command=lambda: speak(t1.get('1.0', END)))

# frame 1 component
t1 = Text(frame1, font=("cascadia code", 10))
t1.pack(fill=BOTH, expand=True)

t1.config(yscrollcommand=scrollbarY.set)
scrollbarY.config(command=t1.yview)

app.config(menu=menuBar)
app.mainloop()
