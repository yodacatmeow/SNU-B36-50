import os, sys
import numpy as np
import librosa as librosa
import librosa.display
import matplotlib.pyplot as plt
from scipy.misc import imsave


# Folder
path = "038"
dir = os.listdir(path)
# Audio format
audio_format = ".m4a"

filenames = []
# List file names in 'path'
for file in dir:
    # if 'file' doesn't include '.wav'
    if file.find(audio_format) == -1:
        pass
    else:
        filenames.append(os.path.join(path,file))
filenames = np.sort(filenames)
print(filenames)
print("Loading files...")

## log-melspectrogram
time_len = 3    # time_len Second
for file in filenames:
    print("file:", file)
    s_n, fs = librosa.load(file, sr = None, mono = True)
    # zero-padding; if audio input is shorter than 3 sec
    if len(s_n) < time_len * fs:
        s_n = np.pad(s_n, (0, time_len * fs - len(s_n)), 'constant' )
        print("sample is shorter than time_len")

    # Mel-spectrogram
    # For 3 sec (@fs = 44100 Hz), window size of 2048; hop size of 592 gives 224 x 224 mel-spectromgram
    # If input audio has length of > 3 sec (@fs = 44100 Hz), width of output > 224
    n_mels = 224
    n_width = n_mels
    E = librosa.feature.melspectrogram(y = s_n, sr = fs, n_mels = n_mels, n_fft = 2048, hop_length = 2048, power = 2)
    E = librosa.logamplitude(E, ref_power=np.max)
    #print(E.shape)

    ## Draw the patch
    plt.imshow(E, aspect='auto')
    #plt.figure(figsize=(8, 6)), librosa.display.specshow(E, x_axis='time'), plt.colorbar(), plt.clim(np.min(E), np.max(E))
    plt.show()

    ## Save the mel-spectrogram into image format
    """
    img_format = ".png" # ".jpg", ".png" were tested
    # Image name
    img_name_pos_init = file.find("/")
    img_name_pos_end = file.find(".wav")
    img_name = "img_out/" + file[img_name_pos_init + 1:img_name_pos_end] + img_format
    # Save image
    imsave(img_name, P)
    """

print("Finish!")
