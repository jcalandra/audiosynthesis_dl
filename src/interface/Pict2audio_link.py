import cv2
import csv
import IPython.display
import numpy as np
import tensorflow as tf
import keras
import load_models

print('tensorflow:', tf.__version__)
print('keras:', keras.__version__)


def process_data(image):
    fimg = image.astype('float32')
    norm_img = fimg / 255
    return norm_img


def match_algorithm(y, file):
    next(file)
    for row in file:
        i = 0
        while y[i] == int(row[i + 1]):
            i = i + 1
            if i == 3:
                name = row[0]
                print(name)
                return name
    print("Can't find any sound from the Library that match with the given picture")
    return 'ERROR'


def main():
    # 1) Load the Pict2Audio_multineural network (they are loaded before in load_moedls.py)
    model_pitch = load_models.model_level
    model_thick = load_models.model_thick
    model_color = load_models.model_color

    # 2) Load a tab or csv with all sound labellised
    print('[INFO] Loading the csv file...')
    csv_file = open('audioLib.csv', newline='')
    file_reader = csv.reader(csv_file, delimiter=';')

    # 3) draw the picture OK
    #    - exec paint.py
    #    - save the picture in a precise folder with a precise name

    # in the interface, button to display the following algorithm

    # 1) take the picture drawn
    #    - load the specific picture with the special name

    print('[INFO] loading the picture...')
    img_tab = np.empty((0, 400, 400, 3))
    img = cv2.imread('img2analyse.png')
    img_tab = np.concatenate((img_tab, np.reshape(img, (1, 400, 400, 3))), axis=0)

    x_img = process_data(img_tab)

    # 4) classify the picture
    #    - Put as entry of the neural network
    #    - 3 labels are obtained : pitch & thick & color
    print('[INFO] Prediction of the classes...')
    y_img = []
    y_img.append(model_pitch.predict_classes(x_img))
    y_img.append(model_thick.predict_classes(x_img))
    y_img.append(model_color.predict_classes(x_img))

    # 5) match the label of the picture with the labels of the sound dataset
    #    - search algorithm in a tab
    print('[INFO] Running algorithm...')
    sound = match_algorithm(y_img, file_reader)

    # 6) play the adequate sound
    #    - take the name in the tab,
    #    - look for the sound with this name in the lib
    #    - play the sound

    # TODO : trouver le son le plus proche avec une notification expliquant qu'il ne s'agit pas d'une correspondance
    #  exacte
    # TODO : afficher le bouton display ?
    if sound != 'ERROR':
        print('sound displaying')
        IPython.display.Audio(sound, autoplay=True)
    else:
        print('No sound can be displayed')
