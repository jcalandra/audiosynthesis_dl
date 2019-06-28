# reference : https://gist.github.com/nikhilkumarsingh/85501ee2c3d8c0cfa9d1a27be5781f06

from tkinter import *
from tkinter.colorchooser import askcolor
import PIL
from PIL import Image, ImageDraw, ImageTk
print('PIL',Image.VERSION)

### PICT2AUDIO graphic interface
### Graphic interface to draw picutres assimilated to sounds

#TODO :
#       1) trouver comment faire une gomme pour l'affichage (blanc ok pour la sauvegarde)
#       2) fonction clear l'image
#       3) agencer les boutons correctement (grid ou pack)
#       4) laisser une possibilite de sauvegarde avec ou sans grille.
#       5) afficher un pointeur avec la taille du trait


class Paint(object):

    DEFAULT_PEN_SIZE = 10.0
    DEFAULT_COLOR = 'black'

    def __init__(self):
        self.root = Tk()

        ## --- title
        title = Label(self.root, text="Pict2Audio", font=("Helvetica", 24))
        title.grid(row=0, columnspan=5)
        subtitle = Label(self.root, text="From Pictures to Sounds", font=("Helvetica", 16))
        subtitle.grid(row=1, columnspan=5)

        self.pen_button = Button(self.root, text='pen', command=self.use_pen)
        self.pen_button.grid(row=3, column=0)

        self.color_button = Button(self.root, text='color', command=self.choose_color)
        self.color_button.grid(row=3, column=1)

        self.eraser_button = Button(self.root, text='eraser', command=self.use_eraser)
        self.eraser_button.grid(row=3, column=2)

        self.clear_button = Button(self.root, text='clear', command=self.use_clear, fg="red")
        self.clear_button.grid(row=3, column=3)

        self.choose_size_button = Scale(self.root, from_=1, to=30, orient=HORIZONTAL)
        self.choose_size_button.grid(row=3, column=4)

        self.c = Canvas(self.root, bg='white', width=400, height=400)
        self.c.grid(row=4, columnspan=5)

        self.base = PIL.ImageTk.PhotoImage(file = "base_quadrillage.png")
        self.c.create_image(400, 400, image = self.base, anchor = SE)

        self.img = PIL.Image.new('RGB', (400, 400), 'white')
        self.draw = ImageDraw.Draw(self.img)

        self.ent = Entry(self.root)
        self.ent.grid(row=5, columnspan=3)
        self.ent.insert(0, "filename (w/ extention)")

        self.save_button = Button(self.root, text="save", command=self.use_save, fg="green")
        self.save_button.grid(row=5, column=4)

        self.sound_button = Button(self.root, text="GET SOUND", command=self.get_sound, fg="maroon3")
        self.sound_button.grid(row=6, columnspan=5)

        self.setup()
        self.root.mainloop()

    def setup(self):
        self.old_x = None
        self.old_y = None
        self.line_width = self.choose_size_button.get()
        self.color = self.DEFAULT_COLOR
        self.eraser_on = False
        self.active_button = self.pen_button
        self.c.bind('<B1-Motion>', self.paint)
        self.c.bind('<ButtonRelease-1>', self.reset)

    def use_pen(self):
        self.activate_button(self.pen_button)

    def use_clear(self):
        self.activate_button(self.clear_button)

    def choose_color(self):
        self.eraser_on = False
        self.color = askcolor(color=self.color)[1]
        self.activate_button(self.pen_button)


    def use_eraser(self):
        self.activate_button(self.eraser_button, eraser_mode=True)

    def use_save(self):
        self.imagename = self.ent.get()
        filename = self.imagename +'.png'
        self.img.save(filename)
        print(filename + " has been saved")

    def get_sound(self):
        self.activate_button(self.sound_button)

    def activate_button(self, some_button, eraser_mode=False):
        self.active_button.config(relief=RAISED)
        some_button.config(relief=SUNKEN)
        self.active_button = some_button
        self.eraser_on = eraser_mode

    def paint(self, event):
        self.line_width = self.choose_size_button.get()
        paint_color = 'white' if self.eraser_on else self.color
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x, self.old_y, event.x, event.y,
                               width=self.line_width, fill=paint_color, capstyle=ROUND, smooth=TRUE, splinesteps=36)
            self.draw.line([(self.old_x, self.old_y), (event.x, event.y)], width=self.line_width, fill=paint_color, joint='curve')
            Offset = (self.line_width-3)/2
            self.draw.ellipse((self.old_x-Offset,self.old_y-Offset, self.old_x+Offset,self.old_y+Offset), fill=paint_color)
        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event):
        self.old_x, self.old_y = None, None


if __name__ == '__main__':
    Paint()
