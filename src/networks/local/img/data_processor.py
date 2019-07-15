import numpy as np
import random
import global_values as gv
from keras.preprocessing import image


# LOADING THE DATA
def load_data(label_tab, img_tab, path, dir_path):
    for imgP in path:
        if imgP.split(".")[-1] != "git" and imgP.split(".")[-1] != "gitignore":
            img = image.load_img(gv.img_path + dir_path + imgP, target_size=(gv.PICT_WIDTH, gv.PICT_WIDTH),
                                 color_mode='rgb')
            img_tab = np.concatenate((img_tab, np.reshape(img, (1, gv.PICT_WIDTH, gv.PICT_WIDTH, gv.NB_CHANNEL))),
                                     axis=0)
            lab = imgP.split("_")
            labels = lab[:gv.NB_CHARACTERISTICS]
            label_tab.append(labels)
    return img_tab


# CONVERTING THE DATA
def converting_data(img_tab):
    """ convert the data in float between 0 et 1"""
    # Convert to float
    img_tab = img_tab.astype('float32')
    # Normalize inputs from [0; 255] to [0; 1]
    imgnorm_tab = img_tab / 255
    return imgnorm_tab


# MIXING THE DATA FOR A GOOD LEARNING
def shuffle_data(img_tab, label_tab, nb_pict):
    """ create shuffled tabs of data and corresponding labels """
    imgnorm_tab = converting_data(img_tab)
    xy_tab = []
    for i in range(nb_pict):
        label_tab_i = []
        pitch = int(label_tab[i][0].split('pitch')[
                        1]) - 69  # labels are converted into integer between 0 and the number of classes
        thick = int(label_tab[i][1].split('thick')[1])
        color = int(label_tab[i][2].split('color')[1])
        label_tab_i.append(pitch)
        label_tab_i.append(thick)
        label_tab_i.append(color)
        xy = [imgnorm_tab[i], label_tab_i]
        xy_tab.append(xy)
    random.shuffle(xy_tab)
    x_tab = np.empty((nb_pict, 400, 400, gv.NB_CHANNEL))
    y_tab = np.empty((nb_pict, gv.NB_CHARACTERISTICS))
    for i in range(nb_pict):
        x_tab[i] = xy_tab[i][0]
        y_tab[i] = xy_tab[i][1]
    del imgnorm_tab
    del xy_tab
    return [x_tab, y_tab]


def gen_features_tabs(y_tab, y_feature, i_feature):
    """ generate a tab containing the labels for one specific feature """
    for i in range(len(y_tab)):
        y_feature[i] = y_tab[i][i_feature]
    return y_feature
