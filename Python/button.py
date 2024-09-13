from tkinter import *
window = Tk()
window.title('Button Example')

btn_end = Button(window, text = 'Close', command=exit)

def tog():
    if window.cget('bg') == 'magenta':
        window.configure(bg = 'lightgrey')
    else:
        window.configure(bg = 'magenta')

btn_tog = Button(window, text = 'Switch', command=tog)

btn_tog.pack(padx = 120, pady = 20)
btn_end.pack(padx = 120, pady = 20)

window.mainloop()
