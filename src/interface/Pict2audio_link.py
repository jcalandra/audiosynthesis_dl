print('[INFO] loading the librairies...')
import librosa
import cv2
import numpy as np
import csv
import IPython
import tensorflow as tf
import keras
from keras.models import load_model

print('tensorflow:', tf.__version__)
print('keras:', keras.__version__)

NB_CARACTERISTICS = 3

# 1) Load the Pict2Audio_multineural network

print('[INFO] Loading Neural Networks...')
model_pitch = load_model('model_pitch.h5')
model_thick = load_model('model_thick.h5')
model_color = load_model('model_color.h5')

# 2) Load a tab or csv with all sound labellised
print('[INFO] Loading the csv file...')
csvfile = open('audioLib.csv', newline='')
filereader = csv.reader(csvfile, delimiter=';')

# 3) draw the picture OK
#    - exec paint.py
#    - save the picture in a precise folder with a precise name

# in the interface, button to display the following algorithm

# 1) take the picture drawn
#    - load the specific picture with the special name

print('[INFO] loading the picture...')
img_tab = np.empty((0,400,400,3))
img = cv2.imread('2analyse.png')
img_tab = np.concatenate((img_tab,np.reshape(img,(1,400,400,3))),axis=0)

def process_data(image):
  fimg = image.astype('float32')
  norm_img = fimg / 255
  return norm_img

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

def match_algorithm(y, file):
    next(file)
    for row in file:
        i = 0
        while (y[i] == int(row[i+1])):
            i++;
            if (i == 3):
                name = row[0]
                print(name)
                return(name)
    print("Can't find any sound from the Library that match with the given picture")
    return('NULL')

sound = match_algorithm(y_img, filereader)

# 6) play the adequated sound
#    - take the name in the tab,
#    - look for the sound with this name in the lib
#    - play the sound

IPython.display.Audio((sound))
