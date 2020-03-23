#Import all the dependencies

import librosa as lr
from glob import glob
import pylab
import librosa.display
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data='/Users/bidhanbashyal/Acoustic/Bus2/audio/'
audio_file=glob(data+'/*.wav')



# The following code generates the spectrogram for an audio signal and saves in the desired directory.

for file in range(0, len(audio_file), 1):
    x,sr=lr.load(audio_file[file])
    X = librosa.stft(x)
    Xdb = librosa.amplitude_to_db(abs(X))
    plt.figure(figsize=(14, 5))
    librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='hz')
    save_path = './desktop/Acoustic/Airport Data/Spectrogram/0.jpg'
    pylab.savefig(save_path, bbox_inches=None, pad_inches=0)
