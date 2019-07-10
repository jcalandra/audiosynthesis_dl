# reference : https://gist.github.com/nikhilkumarsingh/85501ee2c3d8c0cfa9d1a27be5781f06

from tkinter import *
from tkinter.colorchooser import askcolor
import PIL
from PIL import Image, ImageDraw, ImageTk
import Pict2audio_link
import audio2csv


# PICT2AUDIO graphic interface
# Graphic interface to draw pictures assimilated to sounds

# TODO :
#       Pour l'interface :
#       1) faire jouer le son correctement
#       2) nettoyer le code
#       Pour l'appli paint :
#       1) trouver comment faire une gomme pour l'affichage
#       2) laisser une possibilite de sauvegarde avec ou sans grille.
#       3) interface d'entrainement et de chargement des réseaux


class Paint:
    DEFAULT_COLOR = 'black'
    DEFAULT_NAME = 'default'

    def __init__(self):
        # Creation of the window
        self.root = Tk()
        self.root.title('Pict2Audio')

        # Title
        title = Label(self.root, text="Pict2Audio", font=("Helvetica", 24))
        title.grid(row=0, columnspan=5)
        subtitle = Label(self.root, text="From Pictures to Sounds", font=("Helvetica", 16))
        subtitle.grid(row=1, columnspan=5)

        # Buttons for the drawing interface
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

        # Drawing interface
        self.c = Canvas(self.root, bg='white', cursor="cross", width=400, height=400)
        self.c.grid(row=4, columnspan=5)
        path_base = "../../data/base_quadrillage.png"
        self.base = PIL.ImageTk.PhotoImage(file=path_base)
        self.c.create_image(400, 400, image=self.base, anchor=SE)

        self.img = Image.open(path_base)
        self.rgb_img = self.img.convert('RGB')
        self.draw = ImageDraw.Draw(self.img)

        # Saving and neural network buttons
        self.ent = Entry(self.root)
        self.ent.grid(row=5, column=0, columnspan=2)
        self.ent.insert(0, "filename (w/ extention)")

        self.save_button = Button(self.root, text="save", command=self.use_save, fg="green")
        self.save_button.grid(row=5, column=4)

        self.sound_button = Button(self.root, text="GET SOUND", command=self.get_sound, fg="maroon3")
        self.sound_button.grid(row=6, columnspan=5)

        # Initialisation for functions
        self.old_x = None
        self.old_y = None
        self.line_width = self.choose_size_button.get()
        self.color = self.DEFAULT_COLOR
        self.eraser_on = False
        self.active_button = self.pen_button
        self.c.bind('<B1-Motion>', self.paint)
        self.c.bind('<ButtonRelease-1>', self.reset)
        self.image_name = self.DEFAULT_NAME

        # Mainloop
        self.root.mainloop()

    def use_pen(self):
        self.activate_button(self.pen_button)

    def use_clear(self):
        self.c.create_image(400, 400, image=self.base, anchor=SE)
        path_base = "../../data/base_quadrillage.png"
        self.img = Image.open(path_base)
        self.draw = ImageDraw.Draw(self.img)
        self.activate_button(self.pen_button)

    def choose_color(self):
        self.activate_button(self.color_button)
        self.eraser_on = False
        self.color = askcolor(color=self.color)[1]
        self.activate_button(self.pen_button)

    def use_eraser(self):
        self.activate_button(self.eraser_button, eraser_mode=True)

    def use_save(self):
        self.image_name = self.ent.get()
        filename = self.image_name + '.png'
        self.img.save(filename)
        print(filename + " has been saved")

    def get_sound(self):
        self.activate_button(self.sound_button)
        self.img.save("img2analyse.png")
        Pict2audio_link.main()
        # supprimer éventuellement l'image
        self.activate_button(self.pen_button)

    def activate_button(self, some_button, eraser_mode=False):
        self.active_button.config(relief=RAISED)
        some_button.config(relief=SUNKEN)
        self.active_button = some_button
        self.eraser_on = eraser_mode

    def paint(self, event):
        self.line_width = self.choose_size_button.get()
        paint_color = self.color
        if self.old_x and self.old_y:
            if self.eraser_on:
                paint_color = "white"
            # Draw the line on the interface
            self.c.create_line(self.old_x, self.old_y, event.x, event.y, width=self.line_width,
                               fill=paint_color, capstyle=ROUND, smooth=TRUE, splinesteps=36)
            # Draw a line on background for the saved picture
            self.draw.line([(self.old_x, self.old_y), (event.x, event.y)], width=self.line_width,
                           fill=paint_color, joint='curve')
            offset = (self.line_width - 3) / 2
            self.draw.ellipse((self.old_x - offset, self.old_y - offset, self.old_x + offset, self.old_y + offset),
                              fill=paint_color)
        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event):
        self.old_x, self.old_y = None, None


def main():
    audio2csv.main()
    Paint()


if __name__ == '__main__':
    main()
