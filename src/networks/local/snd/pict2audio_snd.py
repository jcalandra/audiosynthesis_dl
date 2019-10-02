from __future__ import print_function
import os
import glob
import numpy as np
import tensorflow as tf
import keras
import global_values_snd as gv
import data_processor_snd
import network_snd

print('tensorflow:', tf.__version__)
print('keras:', keras.__version__)

NB_PITCH = gv.NB_PITCH
NB_THICK = gv.NB_THICK
NB_COLOR = gv.NB_COLOR
NB_CHARACTERISTICS = gv.NB_CHARACTERISTICS
SAMPLE_RATE = gv.SAMPLE_RATE
INPUT_LENGTH = gv.INPUT_LENGTH
batch_size = gv.batch_size
NB_MEL = gv.NB_MEL
snd_path = gv.snd_path

snd_train = glob.glob(snd_path + "snd_train/*.wav")  # train_files
snd_validation = glob.glob(snd_path + "snd_validation/*.wav")
NB_TRAIN = len(snd_train)
NB_VALIDATION = len(snd_validation)

# ---------------------------------------------PROCESSING SOUNDS------------------------------------------------------
print('[INFO] generation of train mel spectrograms...')
x_train = data_processor_snd.generate_mel(snd_train)
print('[INFO] generation of validation mel spectrograms...')
x_validation = data_processor_snd.generate_mel(snd_validation)


# ----------------------------------------------PROCESSING LABELS-----------------------------------------------------
sndPath_train = os.listdir(snd_path + "snd_train")[:]
sndPath_validation = os.listdir(snd_path + "snd_validation")[:]

label_train = data_processor_snd.create_label_tab(sndPath_train)
label_validation = data_processor_snd.create_label_tab(sndPath_validation)

print(label_train)
print(label_validation)


print('[INFO] conversion of train labels into int...')
y_train = data_processor_snd.label2int(label_train)
print('[INFO] conversion of validation labels into int...')
y_validation = data_processor_snd.label2int(label_validation)


# --------------------------------------------PLOT THE MELSPECTROGRAM-------------------------------------------------

# TODO : trouver un meilleur affichage car on croirait avoir les même valeurs
# pour low et med (les valeurs des spectrogrammes sont effectivement différentes
# - voir les échelles) ou alors les tons pour low deviennent dans les bleus qd MAX >env60

ind1 = snd_path + 'snd_train/guitar_acoustic_021-069-025-low.wav'
# low corresponds to -22dB compared to med
data_processor_snd.plot_mel(ind1)

ind2 = snd_path + 'snd_train/guitar_acoustic_021-069-025-med.wav'
data_base = data_processor_snd.load_audio_file(ind2)
data_processor_snd.plot_mel(ind2)

ind3 = snd_path + 'snd_train/guitar_acoustic_021-069-025-high.wav'
# high corresponds to +10dB compared to med
data_processor_snd.plot_mel(ind3)
# note : there is saturation due to the modification of the medium sound


# ----------------------------------GENERATION OF THE PITCH FEATURES TABS--------------------------------------------

print('[INFO] generation of the pitch features tabs...')
y_train_pitch = np.empty(NB_TRAIN)
y_validation_pitch = np.empty(NB_VALIDATION)

y_train_pitch = data_processor_snd.gen_features_tabs(y_train, y_train_pitch, 1)
y_validation_pitch = data_processor_snd.gen_features_tabs(y_validation, y_validation_pitch, 1)

# Convert class vectors to binary class matrices ("one hot encoding")
print('[INFO] converting pitch class vectors...')
y_train_pitch, y_validation_pitch = network_snd.categorical(y_train_pitch, y_validation_pitch, NB_PITCH)

# ------------------------------------CREATION OF THE PITCH NEURAL NETWORK-------------------------------------------
opt_pitch = keras.optimizers.Adam(lr=0.0001, beta_1=0.9, beta_2=0.999, epsilon=None, decay=0.0, amsgrad=False)
model_pitch, hist_pitch = network_snd.architecture(x_train, y_train_pitch, x_validation, y_validation_pitch, NB_PITCH,
                                                   'model_pitchsnd', opt=opt_pitch, nb_epoch=10)
network_snd.plot(hist_pitch)

del y_train_pitch
del y_validation_pitch

# -------------------------------GENERATION OF THE THICK=VOLUME FEATURES TABS-----------------------------------------
print('[INFO] generation of the thick features tabs...')
y_train_thick = np.empty(NB_TRAIN)
y_validation_thick = np.empty(NB_VALIDATION)

y_train_thick = data_processor_snd.gen_features_tabs(y_train, y_train_thick, 2)
y_validation_thick = data_processor_snd.gen_features_tabs(y_validation, y_validation_thick, 2)

print('[INFO] converting thick class vectors...')
y_train_thick, y_validation_thick = network_snd.categorical(y_train_thick, y_validation_thick, NB_THICK)

# ---------------------------------------CREATION OF THE THICK NEURAL NETWORK-----------------------------------------

opt_thick = keras.optimizers.Adam(lr=0.00005, beta_1=0.9, beta_2=0.999, epsilon=None, decay=0.0, amsgrad=False)
model_thick, hist_thick = network_snd.architecture(x_train, y_train_thick, x_validation, y_validation_thick, NB_THICK,
                                                   'model_thicksnd', opt=opt_thick, nb_epoch=10)
network_snd.plot(hist_thick)

del y_train_thick
del y_validation_thick

# -------------------------------GENERATION OF THE COLOR=TONE FEATURES TABS-------------------------------------------
print('[INFO] generation of the color features tabs...')
y_train_color = np.empty(NB_TRAIN)
y_validation_color = np.empty(NB_VALIDATION)

y_train_color = data_processor_snd.gen_features_tabs(y_train, y_train_color, 0)
y_validation_color = data_processor_snd.gen_features_tabs(y_validation, y_validation_color, 0)

print('[INFO] converting color class vectors...')
y_train_color, y_validation_color = network_snd.categorical(y_train_color, y_validation_color, NB_COLOR)

# -------------------------------------CREATION OF THE COLOR NEURAL NETWORK-------------------------------------------
opt_color = keras.optimizers.Adam(lr=0.0001, beta_1=0.9, beta_2=0.999, epsilon=None, decay=0.0, amsgrad=False)
model_color, hist_color = network_snd.architecture(x_train, y_train_color, x_validation, y_validation_color, NB_COLOR,
                                                   'model_colorsnd', opt=opt_color, nb_epoch=10)
network_snd.plot(hist_color)

del y_train_color
del y_validation_color


# -----------------------------------------------------TEST----------------------------------------------------------
def test_accuracy(y_tab, y_guessed):
    accuracy_sum = 0
    for lab in range(len(y_tab)):
        if float(y_tab[lab]) == float(y_guessed[i]):
            accuracy_sum += 1
    accuracy = float(accuracy_sum) / float(len(y_guessed))
    print('accuracy = ', accuracy)


snd_test = glob.glob(snd_path + "snd_test/*.wav")  # test_files
NB_TEST = len(snd_test)

print('[INFO] generation of test mel spectrograms...')
x_test = data_processor_snd.generate_mel(snd_test)

sndPath_test = os.listdir(snd_path + "snd_test")[:]
label_test = data_processor_snd.create_label_tab(sndPath_test)
print(label_test)

print('[INFO] conversion of test labels into int...')
y_teststat = data_processor_snd.label2int(label_test)
print(y_teststat)

y_teststat_pitch = np.empty(NB_TEST)
y_teststat_pitch = data_processor_snd.gen_features_tabs(y_teststat, y_teststat_pitch, 1)
print(y_teststat_pitch)

y_teststat_thick = np.empty(NB_TEST)
y_teststat_thick = data_processor_snd.gen_features_tabs(y_teststat, y_teststat_thick, 2)

y_teststat_color = np.empty(NB_TEST)
y_teststat_color = data_processor_snd.gen_features_tabs(y_teststat, y_teststat_color, 0)

y_test_pitch = model_pitch.predict_classes(x_test)
y_test_thick = model_thick.predict_classes(x_test)
y_test_color = model_color.predict_classes(x_test)

# show the inputs and predicted outputs
for i in range(len(y_test_pitch)):
    print(
        "label y_test_pitch[%s] = %s, label y_teststat_pitch[%s] = %s " % (i, y_test_pitch[i], i, y_teststat_pitch[i]))
    print(
        "label y_test_thick[%s] = %s, label y_teststat_thick[%s] = %s " % (i, y_test_thick[i], i, y_teststat_thick[i]))
    print("label y_test_color[%s] = %s, label y_teststat_color[%s] = %s \n" % (
        i, y_test_color[i], i, y_teststat_color[i]))

# TODO : check test_accuracy qui imprime une mauvaise accuracy, les résultats sont pourtant ok
print('pitch :')
test_accuracy(y_teststat_pitch, y_test_pitch)
print('thick :')
test_accuracy(y_teststat_thick, y_test_thick)
print('color :')
test_accuracy(y_teststat_color, y_test_color)
