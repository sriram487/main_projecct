import requests
import sounddevice
from scipy.io import wavfile
from datetime import datetime
import librosa
from keras.models import load_model
import numpy as np
import os
from spectral_gating import get_file

model = load_model(r"C:\Users\sriram\Desktop\Main_Project\Project_Model_DL\model_CNN_4c_V2.h5")
classes = ["Akshat", "GeekyRanjit", "Mkbhd", "Mosh"]

fs = 22050
second = 5

print("Recording.....n")


def compute_mfcc(signal, sr):
    mfcc_feature = librosa.feature.mfcc(y=signal, sr=sr, n_mfcc=13, hop_length=512, n_fft=2048)
    mfcc_feature = mfcc_feature.T
    # print(mfcc_feature.shape)
    return mfcc_feature


for i in os.listdir("audios"):

    audio_file = "audios/" + i

    reduced_noise = get_file(audio_file)
    wavfile.write(audio_file, fs, reduced_noise)
    data, sr = librosa.load(audio_file)
    mfcc = compute_mfcc(data, sr)
    # print(sr)
    mfcc = mfcc[np.newaxis, ...]
    prediction = model.predict(mfcc)
    predicted_index = np.argmax(prediction, axis=1)
    print(prediction)
    print(predicted_index)
    data = classes[predicted_index[0]]
    print(data)
    os.remove(audio_file)
    #os.remove("audio_rec/noise_reduced.wav")

    r = requests.post("http://127.0.0.1:5000/update_db", data=data)
    print(r)
