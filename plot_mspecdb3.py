import os, sys
import numpy as np
import librosa as librosa
import librosa.display
import matplotlib.pyplot as plt
from scipy.misc import imsave


# Folder
path = "011"
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
#print(filenames)
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
    E = librosa.feature.melspectrogram(y = s_n, sr = fs, n_mels = n_mels, n_fft = 2048, hop_length = 592, power = 1)

    ## Cut the mel-spectrogram into "n_width" x "n_mels" mel-spectrogram
    E_col_sum = np.sum(E, axis = 0) # Column sum of "E"
    E_area_sum = np.zeros(len(E_col_sum) - n_width + 1)  # initialize array
    # Calculate sum of E[i,j] in an area using "E_col_sum"
    for i in range(len(E_area_sum)):
        E_area_sum[i] = np.sum(E_col_sum[i:i + n_width])
        #print(E_area_sum)
    # A patch from "E" size of "n_mel" x "n_width" with the maximum area sum
    index = [np.argmax(E_area_sum), np.argmax(E_area_sum) + n_width]
    # If index start is negative,
    if index[0] < 0:
        index = [0, n_width]
    else:
        pass
            
    P = E[:, index[0] : index[1] ]
    P = librosa.logamplitude(P, ref_power=np.max)
    print(P.shape)

    ## Draw the patch
    plt.figure(figsize=(8, 6)), librosa.display.specshow(P, x_axis='time'), plt.colorbar(), plt.clim(np.min(P), np.max(P))
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
