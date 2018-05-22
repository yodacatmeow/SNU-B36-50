# Import public python modules
import os, sys
import numpy as np
import librosa as librosa
import librosa.display
import matplotlib.pyplot as plt
from scipy.misc import imsave

# Log scaled mel-spectrogram;
# Generate a mel-filterbank and multiply the filterbank with a spectrogram
def melspec2(s_n, fs, n_fft, win_length, hop_length, n_mels, fmax, power):
    n_width = n_mels
    #- Spectrogram; dtype = complex64
    S = librosa.core.stft(y=s_n, win_length=win_length, n_fft=n_fft, hop_length=hop_length)
    #- To power; Square amplitude
    S = np.abs(S)**power
    #- Mel-filterbank
    fb = librosa.filters.mel(sr=fs, n_fft=n_fft, n_mels=n_mels, fmin=0, fmax=fmax, norm=None)
    #- To Mel-spectrogram
    S = np.matmul(fb, S)
    #- To dB
    S = librosa.logamplitude(S, ref_power=np.max)
    return S

# Folder path
path = "audio/038"
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

# Set parameters
time_len = 3
n_mels = 224
n_fft = 2048
win_length = 2048
hop_length = 592

# For loop
for file in filenames:
    #- Print current file name
    print("file:", file)
    #- Signal and sampling freq.
    s_n, fs = librosa.load(file, sr = None, mono = True)
    #- If audio input is shorter than the target time length, then pad 0
    if len(s_n) < time_len * fs:
        s_n = np.pad(s_n, (0, time_len * fs - len(s_n)), 'constant' )
        print("sample is shorter than time_len")

    #- Convert the current audio signal to a mel-spectrogram with library librosa
    #- 224x224 mel-spectrogram using FFT size of 2048, window size of 2048, and hop size of 592
    S = melspec2(s_n=s_n, fs=fs, n_fft=n_fft, win_length=win_length, hop_length=hop_length, n_mels=n_mels, fmax=int(fs/2), power=2)
    #print(S.shape)

    #- Draw log-scaled mel-spectrogram
    plt.imshow(S, aspect='auto')
    #plt.figure(figsize=(8, 6)), librosa.display.specshow(E, x_axis='time'), plt.colorbar(), plt.clim(np.min(E), np.max(E))
    plt.show()
"""
    #- (Option) Save the mel-spectrogram into image format
    #-- image format; ".jpg", ".png" were tested
    img_format = ".png" 
    #-- Image name
    img_name_pos_init = file.find("/")
    img_name_pos_end = file.find(".wav")
    img_name = "img_out/" + file[img_name_pos_init + 1:img_name_pos_end] + img_format
    #-- Save image
    imsave(img_name, P)
"""
print("Finish!")
