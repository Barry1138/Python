from tkinter import *

window = Tk()
window.title('Image Example')

img = PhotoImage(file = '200-3746732327.gif')

label = Label(window, image = img, bg = 'magenta')

small_img = PhotoImage.subsample(img, x = 2, y = 2)

btn = Button(window, image = small_img)

txt = Text(window, width = 25, height = 7)
txt.image_create('1.0', image = small_img)
txt.insert('1.1', 'Python Fun!')

can = \
    Canvas(window, width = 100, height = 100, bg = 'pink')
    can.create_image((59, 59), image = small_img)
    can.create_line(0, 0, 100, 100, width = 25, fill = 'magenta')

label.pack(side = TOP)
btn.pack(side = LEFT, padx = 10)
txt.pack(side = LEFT)
can.pack(side = LEFT, padx = 10)

window.mainloop()
