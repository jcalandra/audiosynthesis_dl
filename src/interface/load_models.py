from keras.models import load_model

print('[INFO] Loading Picture Neural Networks...')
path_models = "../../models/img/"
model_level = load_model(path_models + 'model_pitch.h5')
model_thick = load_model(path_models + 'model_thick.h5')
model_color = load_model(path_models + 'model_color.h5')

print('[INFO] Loading Sounds Neural Networks...')
path_models = "../../models/snd/"
model_pitch = load_model(path_models + "model_pitchsnd.h5")
model_vol = load_model(path_models + "model_thicksnd.h5")
model_tone = load_model(path_models + "model_colorsnd.h5")