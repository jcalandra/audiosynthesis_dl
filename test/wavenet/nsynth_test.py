""" REFERENCES :
code & jupiter sheet : https://github.com/tensorflow/magenta-demos/blob/master/jupyter-notebooks/NSynth.ipynb
magenta installation guide : https://github.com/tensorflow/magenta#installation
"""

'''importation of necessary packages'''
import os
import numpy as np
import matplotlib.pyplot as plt
from magenta.models.nsynth import utils
from magenta.models.nsynth.wavenet import fastgen
from IPython.display import Audio
%matplotlib inline
%config InlineBackend.figure_format = 'jpg'

'''Sound loading'''
# sound that I choose to load
fname = 'pinkfloyd_extrait1.wav'
sr = 16000
# adapt the parameters.
audio = utils.load_audio(fname, sample_length=40000, sr=sr) #resample the audio
sample_length = audio.shape[0]
print('{} samples, {} seconds'.format(sample_length, sample_length / float(sr)))

'''Encoding'''
%time encoding = fastgen.encode(audio, 'model.ckpt-200000', sample_length)
print(encoding.shape)
np.save(fname + '.npy', encoding)

# Show the encoding of the audio file
fig, axs = plt.subplots(2, 1, figsize=(10, 5))
axs[0].plot(audio);
axs[0].set_title('Audio Signal')
axs[1].plot(encoding[0]);
axs[1].set_title('NSynth Encoding')

'''Decoding'''
%time fastgen.synthesize(encoding, save_paths=['gen_' + fname], samples_per_save=sample_length)
sr = 16000
synthesis = utils.load_audio('gen_' + fname, sample_length=sample_length, sr=sr)
