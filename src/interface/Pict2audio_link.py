print('[INFO] loading the librairies...')
import os

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

import librosa

import tensorflow as tf
import keras
from keras.models import load_model

print('tensorflow:', tf.__version__)
print('keras:', keras.__version__)

print('[INFO] number of classes as global values')
NB_PITCH = 12
NB_THICK = 5
NB_COLOR = 8
NB_CARACTERISTICS = 3

SAMPLE_RATE = 16000
INPUT_LENGTH = SAMPLE_RATE*4

# Prerequiered
# 1) Load the Pict2Audio_multineural network
# 2) Load a tab or csv with all sound labellised

print('[INFO] Loading Neural Networks...')
model_pitch = load_model('model_pitch.h5')
model_thick = load_model('model_thick.h5')
model_color = load_model('model_color.h5')

print('[INFO] Running algorithm...')

# 0) draw the picture OK
#    - exec paint.py
#    - save the picture in a precise folder with a precise name

# in the interface, button to display the following algorithm

# 1) take the picture drawn
#    - load the specific picture with the special name

print('[INFO] loading the picture...')
img = cv2.imread('2analyse.png')

# 2) classify the picture
#    - Put as entry of the neural network
#    - 3 labels are obtained : pitch & thick & color



# 3) match the label of the picture with the labels of the sound dataset
#    - match only pitch & color (thick doens't work for sound)
#    - search algorithm in a tab

# 4) play the adequated sound
#    - take the name in the tab,
#    - look for the sound with this name in the lib
#    - play the sound
