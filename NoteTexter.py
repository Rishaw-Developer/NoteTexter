"""
Note Texter is a text editor made for editing txt files.

Author: Rishaw
Author-Email: ratneshthakur.40@gmail.com or rishav.9212@gmail.com
"""
# Main Note Texter Code
# This is based on object oriented programming
import os
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename

class NoteTexter:
    def __init__(self):
        self.app = Tk()
        self.app.title("Note Texter")
        self.frame1 = self.createFrame(BOTH, True)
        self.t1 = self.createTextBox()
        self.menuBar = Menu(self.app)
        self.createButtons()
        self.app.config(menu=self.menuBar)
        self.scrollbarY = self.createScrollbar()
        self.t1.config(yscrollcommand=self.scrollbarY.set)
        self.scrollbarY.config(command=self.t1.yview)


    def newFile(self):
        # global filename
        self.app.title("Untitled - Notepad")
        self._filename = None
        self.t1.delete(1.0, END)

    def openFile(self):
        """This function opens the txt file"""
        self._filename = askopenfilename(parent=self.app, filetype=[("TXT file", "*.txt")])
        if self._filename is None:
            messagebox.showinfo("Info", "Nothing is selected", parent=self.app)
        else:
            try:
                file = open(self._filename, "r")
                self.app.title(os.path.basename(self._filename) + " - Note Texter")
                self.t1.delete("1.0", "end")
                self.t1.insert(END, file.read())
            except Exception as e:
                messagebox.showerror("Error", e, parent=self.app)

    def saveFile(self):
        """This function saves the changes done in txt file"""
        # global filename
        if self._filename == None:
            self._filename = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt",
                                     filetypes=[("All Files", "*.*"),
                                                ("Text Documents", "*.txt")])
            if self._filename == "":
                filename = None

            else:
                f = open(self._filename, "w")
                f.write(self.t1.get(1.0, END))
                f.close()

                self.app.title(os.path.basename(self._filename) + " - Notepad")
                print("File Saved")
        else:
            f = open(self._filename, "w")
            f.write(self.t1.get('1.0', END))
            f.close()

    def saveAsFile(self):
        # global filename
        self._filename = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt",
                                     filetypes=[("All Files", "*.*"),
                                                ("Text Documents", "*.txt")])

        f = open(self._filename, "w")
        f.write(self.t1.get('1.0', END))
        f.close()
        self.app.title(os.path.basename(self._filename) + " - Note Texter")

    def createScrollbar(self):
        scrollbarY = Scrollbar(self.frame1)
        scrollbarY.pack(side=RIGHT, fill=Y)
        return scrollbarY

    def createTextBox(self):
        """This funtion returns the widget where the text is shown and written"""
        t1 = Text(self.frame1, font=("cascadia code", 10))
        t1.pack(fill=BOTH, expand=True)
        return t1

    def createButtons(self):
        """This function creates Menu Bar in window"""
        file = Menu(self.menuBar, tearoff=0)
        self.menuBar.add_cascade(label='File', menu=file)
        file.add_command(label='New File', command=lambda: self.newFile())
        file.add_command(label='Open...', command=lambda: self.openFile())
        file.add_command(label='Save', command=lambda: self.saveFile()) 
        file.add_command(label='Save As', command=lambda: self.saveAsFile()) 
        file.add_separator()
        file.add_command(label='Exit', command=self.app.destroy)

    def createFrame(self, *args):
        """This function creates the frames"""
        frame = Frame(self.app, relief=None)
        frame.pack(fill=args[0], expand=args[1])
        return frame
    
    def run(self):
        """This function runs the app"""
        self.app.mainloop()

editor = NoteTexter()
editor.run()