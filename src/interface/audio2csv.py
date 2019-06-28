# Importing the python librairies
print('[INFO] Importing Python libraries...')
from __future__ import print_function
import glob
import numpy as np
import librosa
import tensorflow as tf
import keras
from keras.models import load_model
print('tensorflow:', tf.__version__)
print('keras:', keras.__version__)

# Some needed functions
#TODO : factoriser le code
SAMPLE_RATE = 16000
INPUT_LENGTH = SAMPLE_RATE*4
batch_size = 32
NB_MELS = 320

def preprocess_audio_mel(audio, sample_rate=SAMPLE_RATE):
  """ Generate a mel spectrogram in dB given an `audio` """
  MAX = 10000
  mel_spec = librosa.feature.melspectrogram(y=audio, sr=sample_rate, n_mels= NB_MELS)
  mel_db = (librosa.power_to_db(mel_spec, ref=MAX) + 80)/80
  #TODO :trouver une valeur adaptée pour MAX : on voudrait dans l'idéal tout entre 0 et 1.
  return mel_db

def load_audio_file(file_path, input_length=INPUT_LENGTH):
  """ Extend/Reduce an audio `file_path` to the given `input_lengh` then generate its mel spectrogram """
  data = librosa.core.load(file_path, sr=SAMPLE_RATE)[0] #, sr=16000
  if len(data)>input_length:
    max_offset = len(data)-input_length
    offset = np.random.randint(max_offset)
    data = data[offset:(input_length+offset)]
  else:
    if input_length > len(data):
      max_offset = input_length - len(data)
      offset = np.random.randint(max_offset)
    else:
      offset = 0
      data = np.pad(data, (offset, input_length - len(data) - offset), "constant")
      #note : maybe adding silence could be more accurate depending of the type of sound in input
  data = preprocess_audio_mel(data)
  return data

def generate_mels(snd_tab):
  """ Put and reshape the mel spectrograms in a tab `snd_tab` """
  x_tab = np.empty((len(snd_tab),NB_MELS,126, 1))
  for i in range(len(snd_tab)) :
    x_tab_i = np.reshape(load_audio_file(snd_tab[i]),(1,NB_MELS,126,1))
    x_tab[i] = x_tab_i
  return x_tab

# Importation of sounds libraries
print('[INFO] Importing the sounds library...')
path = "../"
path_snd = "data/bdd_snd/"
snd_train = glob.glob(path + path_snd + "snd_train/*.wav") #train_files
snd_validation = glob.glob(path + path_snd + "snd_validation/*.wav") #validation_files
snd_test = glob.glob(path + path_snd + "snd_test/*.wav") #test_files

snd = snd_train + snd_validation + snd_test
NB_SND = len(snd)

# Data processing for the neural network
print('[INFO] generation of mel spectrograms...')
x_tab = generate_mels(snd)

# Loading the needed neural networks
print('[INFO] Loading Sounds Neural Networks...')
path_models = "models/sound/"
model_pitch = load_model(path + path_models + "model_pitchsnd.h5")
model_vol = load_model(path + path_models + "model_thicksnd.h5")
model_tone = load_model(path + path_models + "model_colorsnd.h5")

# Creation of the CSV file
print('[INFO] Creation of the CSV file...')

headers = [
     u'Audio_names',
     u'label_pitch',
     u'label_vol',
     u'label_tone'
]

# remplir avec les labels correspondants
labels_pitch = model_pitch.predict_classes(x_tab)
labels_vol = model_vol.predict_classes(x_tab)
labels_tone = model_tone.predict_classes(x_tab)

# modifier label
labels = [[snd[i],str(labels_pitch[i]), str(labels_vol[i]), str(labels_tone[i])] for i in range(NB_SND)]

f = open('audioLib.csv', 'w')
lineHeader = ";".join(headers) + "\n"
f.write(lineHeader)
for label in labels:
     line = ";".join(label) + "\n"
     f.write(line)
f.close()
