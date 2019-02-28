""" REFERENCES :
code & jupiter sheet : https://github.com/tensorflow/magenta-demos/blob/master/jupyter-notebooks/NSynth.ipynb
magenta installation guide : https://github.com/tensorflow/magenta#installation
"""

import os
import sys
import numpy as np
import matplotlib.pyplot as plt
from magenta.models.nsynth import utils
from magenta.models.nsynth.wavenet import fastgen
from IPython.display import Audio
from skimage.transform import resize


def load_encoding(fname, sample_length=None, sr=16000, ckpt='model.ckpt-200000'):
    '''sound loading'''
    audio = utils.load_audio(fname, sample_length=sample_length, sr=sr)
    sample_length = audio.shape[0]
    print('{} samples, {} seconds'.format(sample_length, sample_length / float(sr)))
    '''encoding'''
    encoding = fastgen.encode(audio, ckpt, sample_length)
    print("(batch_size, time_steps, dimensions) :",encoding.shape)
    np.save(fname + '.npy', encoding)
    return audio, encoding

def decoding(fname, sample_length, sr, encoding):
    fastgen.synthesize(
        encoding,
        save_paths=['gen_' + fname],
        samples_per_save=sample_length)
    synthesis = utils.load_audio('gen_' + fname,
                                 sample_length=sample_length,
                                 sr=sr)

def show_encoding(audio, encoding):
    fig, axs = plt.subplots(2, 1, figsize=(10, 5))
    axs[0].plot(audio);
    axs[0].set_title('Audio Signal')
    axs[1].plot(encoding[0]);
    axs[1].set_title('NSynth Encoding')

def timestretch(encoding, factor):
    min_encoding, max_encoding = encoding.min(), encoding.max()
    encodings_norm = (encodings - min_encoding) / (max_encoding - min_encoding)
    timestretches = []
    for encoding_i in encodings_norm:
        stretched = resize(encoding_i, (int(encoding_i.shape[0] * factor), encoding_i.shape[1]), mode='reflect')
        stretched = (stretched * (max_encoding - min_encoding)) + min_encoding
        timestretches.append(stretched)
    return np.array(timestretches)

# main
fname = sys.argv[1] # de la forme '../data/pinkfloyd_extrait1.wav'
#TODO : gerer l'erreur si pas de type .wav
sample_length = 32000
sr = 16000
audio, encoding = load_encoding(fname, sample_length)
show_encoding(audio, encoding)
encoding_slower = timestretch(encoding, 1.5)
encoding_faster = timestretch(encoding, 0.5)
decoding(fname, sample_length, sr, encoding)
decoding(fname, sample_length, sr, encoding_slower)
decoding(fname, sample_length, sr, encoding_faster)
show_encoding(audio, encoding)
show_encoding(audio, encoding_slower)
show_encoding(audio, encoding_faster)
