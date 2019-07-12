# GLOBAL VALUES
# TODO : the objective is to let the composer choose the number of characteristics that he wants
NB_CHARACTERISTICS = 3
NB_PITCH = 12
NB_THICK = 3
NB_COLOR = 8

PICT_WIDTH = 400
NB_CHANNEL = 3
LINE_WIDTH = PICT_WIDTH // NB_PITCH  # 33

# number of versions for a same pitch
# (now automatically generated, then will be the number of picture drawn by the composer)
NB_VERSION_TRAIN = 2
NB_VERSION_VALIDATION = 1
NB_VERSION_TESTGEN = 1

img_path = "../../../data/bdd_img/"
