# GLOBAL VALUES
NB_PITCH = 12
NB_THICK = 3
NB_COLOR = 8
NB_CHARACTERISTICS = 4  # In our database, the intensity is also labelised in the third position of the name # but we
# don't want to analyse it

SAMPLE_RATE = 16000
INPUT_LENGTH = SAMPLE_RATE * 4
batch_size = 32
NB_MEL = 320

snd_path = "../../../../data/bdd_snd/"
