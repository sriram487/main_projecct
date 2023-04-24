import sounddevice
from scipy.io.wavfile import write
from datetime import datetime
import librosa
from keras.models import load_model
import numpy as np

model = load_model(r"C:\Users\paramesh reddy\Desktop\Main_Project\Project_Model_DL\model_CNN_4c.h5")

fs = 22050
second = 5

print("Recording.....n")


def compute_mfcc(signal, sr):
    mfcc_feature = librosa.feature.mfcc(y=signal, sr=sr, n_mfcc=13, hop_length=512, n_fft=2048)
    mfcc_feature = mfcc_feature.T
    # print(mfcc_feature.shape)
    return mfcc_feature 


while True:
    record_voice = sounddevice.rec(int(second * fs), samplerate=fs, channels=2)
    sounddevice.wait()
    name = datetime.now()
    audio_file = "audio_rec/sound.wav"
    write(audio_file, fs, record_voice)
    data, sr = librosa.load(audio_file)
    mfcc = compute_mfcc(data, sr)
    # print(sr)
    mfcc = mfcc[np.newaxis, ...]
    prediction = model.predict(mfcc)
    predicted_index = np.argmax(prediction, axis=1)
    print(prediction)
    print(predicted_index)

    # os.remove(audio_file)
