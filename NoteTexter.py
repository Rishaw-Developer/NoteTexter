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
from tkinter.filedialog import askopenfile, askopenfilename

class NoteTexter:
    def __init__(self):
        self.app = Tk()
        self.app.title("Note Texter")
        self.frame1 = self.createFrame(None, None)
        self.frame2 = self.createFrame(BOTH, True)
        self.createButtons()
        self.t1 = self.createTextBox()

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
        file = open(self._filename, "w")
        file.write(self.t1.get("1.0", END))
        file.close()

    def createTextBox(self):
        """This funtion returns the widget where the text is shown and written"""
        t1 = Text(self.frame2, font=("cascadia code", 10))
        t1.pack(fill=BOTH, expand=True)

        return t1

    def createButtons(self):
        """This function creates buttons to open and save files and exit the window"""
        b1 = Button(self.frame1, text="Open", command=lambda: self.openFile())
        b1.grid(row=0, column=0, sticky=NSEW)
        
        b2 = Button(self.frame1, text="Save", command=lambda: self.saveFile())
        b2.grid(row=0, column=1, sticky=NSEW)

        b3 = Button(self.frame1, text="Exit", command=lambda: self.app.destroy())
        b3.grid(row=0, column=2, sticky=NSEW)

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