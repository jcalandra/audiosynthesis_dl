from __future__ import print_function
import os
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import keras
import global_values_img as gv
import data_generator_img
import data_processor_img
import network_img

# TODO: mettre le chargement des images dans data_processor ?
# TODO: séparer la phase de tests ?

print('tensorflow:', tf.__version__)
print('keras:', keras.__version__)

# GLOBAL VALUES
NB_PITCH = gv.NB_PITCH
NB_THICK = gv.NB_THICK
NB_COLOR = gv.NB_COLOR
PICT_WIDTH = gv.PICT_WIDTH
NB_CHANNEL = gv.NB_CHANNEL
LINE_WIDTH = PICT_WIDTH // NB_PITCH  # 33
NB_CHARACTERISTICS = gv.NB_CHARACTERISTICS
# number of versions for a same pitch
NB_VERSION_TRAIN = gv.NB_VERSION_TRAIN
NB_VERSION_VALIDATION = gv.NB_VERSION_VALIDATION
NB_VERSION_TESTGEN = gv.NB_VERSION_TESTGEN
# number of trained and validation pictures 
NB_TRAIN = NB_THICK * NB_COLOR * NB_PITCH * NB_VERSION_TRAIN
NB_VALIDATION = NB_THICK * NB_COLOR * NB_PITCH * NB_VERSION_VALIDATION
NB_TESTGEN = NB_COLOR * NB_THICK * NB_PITCH * NB_VERSION_TESTGEN

img_path = gv.img_path

# --------------------------------------------PICTURE GENERATION----------------------------------------------------

# generating exactly the same path line for every color, pitch and thickness
print('[INFO] generating training dataset...')
# data_generator.generate_pict(NB_VERSION_TRAIN, 'train', 0, [1, 1, 1])
print('[INFO] generating validation dataset...')
# data_generator.generate_pict(NB_VERSION_VALIDATION, 'validation', 0, [1, 1, 1])

# ---------------------------------------------LOADING THE PICTURES--------------------------------------------------
print('[INFO] loading training dataset...')
imagePath_train = sorted(os.listdir(img_path + "img_train")[:])
imagePath_validation = sorted(os.listdir(img_path + "img_validation")[:])

label_train = []
img_train = np.empty((0, PICT_WIDTH, PICT_WIDTH, NB_CHANNEL))
img_train = data_processor_img.load_data(label_train, img_train, imagePath_train, "img_train/")

print('[INFO] loading validation dataset...')
label_validation = []
img_validation = np.empty((0, PICT_WIDTH, PICT_WIDTH, NB_CHANNEL))
img_validation = data_processor_img.load_data(label_validation, img_validation, imagePath_validation, "img_validation/")

print(label_train)
print(label_validation)
print('img_train.shape=', img_train.shape)
print('img_validation.shape=', img_validation.shape)

print('[INFO] shuffle datasets...')
[x_train, y_train] = data_processor_img.shuffle_data(img_train, label_train, NB_TRAIN)
[x_validation, y_validation] = data_processor_img.shuffle_data(img_validation, label_validation, NB_VALIDATION)

del img_train
del img_validation
del label_train
del label_validation


# -------------------------------------GENERATION OF THE PITCH FEATURES TABS------------------------------------------
y_train_pitch = np.empty(NB_TRAIN)
y_validation_pitch = np.empty(NB_VALIDATION)

print('[INFO] generating pitch label tabs...')
y_train_pitch = data_processor_img.gen_features_tabs(y_train, y_train_pitch, 0)
y_validation_pitch = data_processor_img.gen_features_tabs(y_validation, y_validation_pitch, 0)

print('y_train_pitch.shape=', y_train_pitch.shape)
print('y_validation_pitch.shape=', y_validation_pitch.shape)

y_train_pitch, y_validation_pitch = network_img.categorical(y_train_pitch, y_validation_pitch, NB_PITCH)

# --------------------------------------GENERATION OF THE PITCH NEURAL NETWORK----------------------------------------

print('[INFO] generating PITCH NETWORK...')
opt_pitch = keras.optimizers.Adam(lr=0.0001, beta_1=0.9, beta_2=0.999, epsilon=None, decay=0.0, amsgrad=False)
model_pitch, hist_pitch = network_img.architecture(x_train, y_train_pitch, x_validation, y_validation_pitch, NB_PITCH,
                                                   'model_pitch', opt=opt_pitch, nb_epoch=100)
network_img.plot(hist_pitch)

del y_train_pitch
del y_validation_pitch

# --------------------------------------GENERATION OF THE THICKNESS FEATURES TABS-------------------------------------

y_train_thick = np.empty(NB_TRAIN)
y_validation_thick = np.empty(NB_VALIDATION)

print('[INFO] generating thickness label tabs...')
data_processor_img.gen_features_tabs(y_train, y_train_thick, 1)
data_processor_img.gen_features_tabs(y_validation, y_validation_thick, 1)
y_train_thick, y_validation_thick = network_img.categorical(y_train_thick, y_validation_thick, NB_THICK)


# ---------------------------------------CREATION OF THE NEURAL NETWORK-----------------------------------------------
print('[INFO] training THICK NETWORK...')
opt_thick = keras.optimizers.Adam(lr=0.0001, beta_1=0.9, beta_2=0.999, epsilon=None, decay=0.0, amsgrad=False)
model_thick, hist_thick = network_img.architecture(x_train, y_train_thick, x_validation, y_validation_thick, NB_THICK,
                                                   'model_thick', opt=opt_thick, nb_epoch=100)
network_img.plot(hist_thick)

del y_train_thick
del y_validation_thick

# --------------------------------------GENERATION OF THE COLOR FEATURES TABS---------------------------------------

y_train_color = np.empty(NB_TRAIN)
y_validation_color = np.empty(NB_VALIDATION)

print('[INFO] generating color label tabs...')
data_processor_img.gen_features_tabs(y_train, y_train_color, 2)
data_processor_img.gen_features_tabs(y_validation, y_validation_color, 2)
y_train_color, y_validation_color = network_img.categorical(y_train_color, y_validation_color, NB_COLOR)

# ---------------------------------------CREATION OF THE COLOR NEURAL NETWORK----------------------------------------

print('[INFO] training COLOR NETWORK...')

opt_color = keras.optimizers.Adam(lr=0.0001, beta_1=0.9, beta_2=0.999, epsilon=None, decay=0.0, amsgrad=False)
model_color, hist_color = network_img.architecture(x_train, y_train_color, x_validation, y_validation_color, NB_COLOR,
                                                   'model_color', opt=opt_color, nb_epoch=100)
network_img.plot(hist_color)

del y_train_color
del y_validation_color


# ---------------------------------------------------- TEST ----------------------------------------------------------
def test_accuracy(y_tab, y_guessed):
    accuracy_sum = 0
    for i in range(len(y_tab)):
        if y_tab[i] == y_guessed[i]:
            accuracy_sum += 1
    accuracy = accuracy_sum / len(y_guessed)
    print('accuracy = ', accuracy)


print("[INFO] generating testgen dataset...")
data_generator_img.generate_pict(NB_VERSION_TESTGEN, 'testgen', 0, [1, 1, 1])

print("[INFO] loading the testgen dataset...")
imagePath_testgen = sorted(os.listdir(img_path + "img_testgen")[:])
label_testgen = []
img_testgen = np.empty((0, PICT_WIDTH, PICT_WIDTH, NB_CHANNEL))
img_testgen = data_processor_img.load_data(label_testgen, img_testgen, imagePath_testgen, "img_testgen/")


print("[INFO] shuffle testgen dataset...")
[x_testgen, y_testgenstat] = data_processor_img.shuffle_data(img_testgen, label_testgen, NB_TESTGEN)
y_testgenstat_pitch = [y_testgenstat[i][0] for i in range(NB_TESTGEN)]
y_testgenstat_thick = [y_testgenstat[i][1] for i in range(NB_TESTGEN)]
y_testgenstat_color = [y_testgenstat[i][2] for i in range(NB_TESTGEN)]

y_testgen_pitch = model_pitch.predict_classes(x_testgen)
y_testgen_thick = model_thick.predict_classes(x_testgen)
y_testgen_color = model_color.predict_classes(x_testgen)


# show the inputs and predicted outputs
for i in range(10):
    print("label y_testgen_pitch[%s] = %s, label y_testgenstat_pitch[%s] = %s "
          % (i, y_testgen_pitch[i], i, y_testgenstat_pitch[i]))
    print("label y_testgen_thick[%s] = %s, label y_testgenstat_thick[%s] = %s "
          % (i, y_testgen_thick[i], i, y_testgenstat_thick[i]))
    print("label y_testgen_color[%s] = %s, label y_testgenstat_color[%s] = %s \n"
          % (i, y_testgen_color[i], i, y_testgenstat_color[i]))

print('pitch :')
test_accuracy(y_testgenstat_pitch, y_testgen_pitch)
print('thick :')
test_accuracy(y_testgenstat_thick, y_testgen_thick)
print('color :')
test_accuracy(y_testgenstat_color, y_testgen_color)

i = 3
print('x_testgen.shape', x_testgen.shape, 'dtype', x_testgen.dtype)
print("y_testgen_pitch[%s] = %s, y_testgenstat_pitch[%s] = %s " % (i, y_testgen_pitch[i], i, y_testgenstat_pitch[i]))
print("y_testgen_thick[%s] = %s, y_testgenstat_thick[%s] = %s " % (i, y_testgen_thick[i], i, y_testgenstat_thick[i]))
print("y_testgen_color[%s] = %s, y_testgenstat_color[%s] = %s " % (i, y_testgen_color[i], i, y_testgenstat_color[i]))
plt.imshow(x_testgen[i, :].reshape(PICT_WIDTH, PICT_WIDTH, NB_CHANNEL))
plt.axis("off")
plt.show()
plt.gcf().clear()
