from tkinter import *
import tkinter.messagebox as box

window = Tk()
window.title('Radio Button Example')

frame = Frame(window)

book = StringVar()

radio_1 = Radiobutton(frame, text = 'HTML', \
                      variable = book, value = 'HTML in easy steps')
radio_2 = Radiobutton(frame, text = 'CSS', \
                      variable = book, value = 'CSS in easy steps')
radio_3 = Radiobutton(frame, text = 'JS', \
                      variable = book, value = 'JavaScript in easy steps')
radio_4 = Radiobutton(frame, text = 'PY', \
                      variable = book, value = 'Python in easy steps')
radio_5 = Radiobutton(frame, text = 'SQL', \
                      variable = book, value = 'SQL in easy steps')
radio_6 = Radiobutton(frame, text = 'PHP', \
                      variable = book, value = 'PHP in easy steps')
radio_7 = Radiobutton(frame, text = 'MySQL', \
                      variable = book, value = 'MySQL in easy steps')
radio_8 = Radiobutton(frame, text = 'SH', \
                      variable = book, value = 'Bash in easy steps')

radio_1.select()

def dialog():
    box.showinfo('Selection', \
                 'Your Choice: \n' + book.get())
btn = Button(frame, text = 'Choose', command = dialog)

btn.pack(side = RIGHT, padx = 5)
radio_1.pack(side = LEFT)
radio_2.pack(side = LEFT)
radio_3.pack(side = LEFT)
radio_4.pack(side = LEFT)
radio_5.pack(side = LEFT)
radio_6.pack(side = LEFT)
radio_7.pack(side = LEFT)
radio_8.pack(side = LEFT)
frame.pack(padx = 30, pady = 30)

window.mainloop()
