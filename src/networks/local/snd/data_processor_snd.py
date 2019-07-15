import numpy as np
import librosa
from librosa import display
import matplotlib.pyplot as plt
import global_values_snd as gv


# Function to process sound into mel spectrogramms
def process_audio_mel(audio, sample_rate=gv.SAMPLE_RATE):
    """ Generate a mel spectrogram in dB given an `audio` """
    max_val = 10000
    mel_spec = librosa.feature.melspectrogram(y=audio, sr=sample_rate, n_mels=gv.NB_MEL)
    mel_db = (librosa.power_to_db(mel_spec, ref=max_val) + 80) / 80
    # TODO :trouver une valeur adaptée pour MAX : on voudrait dans l'idéal tout entre 0 et 1.
    return mel_db


def load_audio_file(file_path, input_length=gv.INPUT_LENGTH):
    """ Extend/Reduce an audio `file_path` to the given `input_lengh` then generate its mel spectrogram """
    data = librosa.core.load(file_path, sr=gv.SAMPLE_RATE)[0]  # , sr=16000
    if len(data) > input_length:
        max_offset = len(data) - input_length
        offset = np.random.randint(max_offset)
        data = data[offset:(input_length + offset)]
    else:
        if input_length > len(data):
            max_offset = input_length - len(data)
            offset = np.random.randint(max_offset)
        else:
            offset = 0
        data = np.pad(data, (offset, input_length - len(data) - offset), "constant")
        # note : maybe adding silence could be more accurate depending of the type of sound in input
    data = process_audio_mel(data)
    return data


def generate_mel(snd_tab):
    """ Put and reshape the mel spectrograms in a tab `snd_tab` """
    x_tab = np.empty((len(snd_tab), gv.NB_MEL, 126, 1))
    for i in range(len(snd_tab)):
        x_tab_i = np.reshape(load_audio_file(snd_tab[i]), (1, gv.NB_MEL, 126, 1))
        x_tab[i] = x_tab_i
    return x_tab


# functions to process labels
def create_label_tab(snd_path_tab):
    """ Create a tab of labels considering a tab of filenames filenames_tab """
    labels_tab = []
    for sndP in snd_path_tab:
        snd = sndP.split('.')[0]
        lab = snd.split("-")
        labels = lab[:gv.NB_CHARACTERISTICS]
        labels_tab.append(labels)
    return labels_tab


def gen_features_tabs(y_tab, y_feature, i_feature):
    """ Generate a tab containing the labels for one specific feature """
    for i in range(len(y_tab)):
        y_feature[i] = y_tab[i][i_feature]
    return y_feature


def label2int(label_tab):
    """Converts the label tab into int between 0 and n """
    y_tab = []
    for i in range(len(label_tab)):
        label_tab_i = []

        # Pitch labelisation
        pitch = int(label_tab[i][1]) - 69

        # Thick labelisation
        label_thick = label_tab[i][3]
        if label_thick == 'low':
            thick = 0
        elif label_thick == 'med':
            thick = 1
        else:
            thick = 2

        # Color labelisation
        label_color = label_tab[i][0].split('_')[0]
        if label_color == 'brass':
            color = 0
        elif label_color == 'guitar':
            color = 1
        elif label_color == 'keyboard':
            color = 2
        elif label_color == 'organ':
            color = 3
        elif label_color == 'string':
            color = 4
        elif label_color == 'vocal':
            color = 5
        elif label_color == 'flute':
            color = 6
        else:
            color = 7

        label_tab_i.append(color)
        label_tab_i.append(pitch)
        label_tab_i.append(thick)
        y_tab.append(label_tab_i)
    return y_tab


def plot_mel(sound_path):
    """Plot the melspectrogramm of the sound indicated by 'sound_path' """
    data_base = load_audio_file(sound_path)
    plt.figure(figsize=(7, 4))
    plt.title('Mel Spectrogram : %s ' % sound_path)
    librosa.display.specshow(data_base, sr=gv.SAMPLE_RATE, x_axis='time', y_axis='mel')
    plt.colorbar(format='%+02.0f dB')
    plt.show()
