from tkinter import *
import tkinter.messagebox as box

window = Tk()
window.title('Listbox Example')

frame = Frame(window)

listbox = Listbox(frame)
listbox.insert(1, 'HTML in easy steps')
listbox.insert(2, 'CSS in easy steps')
listbox.insert(3, 'JavaScript in easy steps')
listbox.insert(4, 'Python in easy steps')
listbox.insert(5, 'SQL in easy steps')
listbox.insert(6, 'PHP in easy steps')
listbox.insert(7, 'MySQL in easy steps')
listbox.insert(8, 'Bash in easy steps')

def dialog():
    box.showinfo('Selection', 'Your Choice: '+\
                 listbox.get(listbox.curselection()))

btn = Button(frame, text = 'Choose', command = dialog)

btn.pack(side = RIGHT, padx = 5)
listbox.pack(side = LEFT)
frame.pack(padx = 30, pady = 30)

window.mainloop()
