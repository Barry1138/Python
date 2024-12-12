from tkinter import *
import tkinter.messagebox as box

window = Tk()
window.title('Check Button Example')

frame = Frame(window)

var_1 = BooleanVar()
var_2 = BooleanVar()
var_3 = BooleanVar()
var_4 = BooleanVar()
var_5 = BooleanVar()
var_6 = BooleanVar()
var_7 = BooleanVar()
var_8 = BooleanVar()
var_9 = BooleanVar()

book_1 = Checkbutton(frame, text = 'HTML', \
                     variable = var_1)
book_2 = Checkbutton(frame, text = 'CSS', \
                     variable = var_2)
book_3 = Checkbutton(frame, text = 'JS', \
                     variable = var_3)
book_4 = Checkbutton(frame, text = 'Py', \
                     variable = var_4)
book_5 = Checkbutton(frame, text = 'SQL', \
                     variable = var_5)
book_6 = Checkbutton(frame, text = 'PHP', \
                     variable = var_6)
book_7 = Checkbutton(frame, text = 'MySQL', \
                     variable = var_7)
book_8 = Checkbutton(frame, text = 'Sh', \
                     variable = var_8)

def dialog():
        s = 'Your Choice:'
        if var_1.get() == 1 : s += 'HTML in easy steps'
        if var_2.get() == 1 : s += 'CSS in easy steps'
        if var_3.get() == 1 : s += 'JavaScript in easy steps'
        if var_4.get() == 1 : s += 'Python in easy steps'
        if var_5.get() == 1 : s += 'SQL in easy steps'
        if var_6.get() == 1 : s += 'PHP in easy steps'
        if var_7.get() == 1 : s += 'MYSQL in easy steps'
        if var_8.get() == 1 : s += 'Bash in easy steps'
        box.showinfo('Selection', s)

        btn = Button(frame, text = 'Choose', command = dialog)

        btn.pack(side = RIGHT, padx = 5)
        book_1.pack(side = LEFT)
        book_2.pack(side = LEFT)
        book_3.pack(side = LEFT)
        book_4.pack(side = LEFT)
        book_5.pack(side = LEFT)
        book_6.pack(side = LEFT)
        book_7.pack(side = LEFT)
        book_8.pack(side = LEFT)
        frame.pack(padx = 30, pady = 30)

        window.mainloop()
