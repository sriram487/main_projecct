import librosa
import os
import json
import math

# 0-->Akshat
# 1-->GeekyRanjit
# 2-->mkbhd
# 3-->mosh

json_path = "data_1Test.json"

SAMPLE_RATE = 22050
TRACK_DURATION = 5  # measured in seconds
hop_length = 512
SAMPLES_PER_TRACK = SAMPLE_RATE * TRACK_DURATION
num_segments = 1
samples_per_segment = int(SAMPLES_PER_TRACK / num_segments)
num_mfcc_vectors_per_segment = math.ceil(samples_per_segment / hop_length)


def compute_features(signal, sr):

    mfcc_feature = librosa.feature.mfcc(y=signal, sr=sr, n_mfcc=13, hop_length=512, n_fft=2048)
    mfcc_feature = mfcc_feature.T
    print(mfcc_feature.shape)
    return mfcc_feature 


def load_data():
    counter = 0
    t_counter = 0
    
    data_dict = {
        "mapping": [],
        "labels": [],
        "mfcc": []
    } 

    '''Akshat'''
    for file_name in os.listdir(r"D:\\Youtube_Voices_Test\\Akshat\\"):
    
        file = r"D:\\Youtube_Voices_Test\\Akshat\\" + file_name
        
        data, sr = librosa.load(file)
        mfcc = compute_features(data, sr)
        t_counter += 1
        if len(mfcc) == num_mfcc_vectors_per_segment:
            data_dict["mfcc"].append(mfcc.tolist())
            data_dict["labels"].append(0)
            data_dict["mapping"].append("Akshat")
            counter += 1

    '''GeekyRanjit'''
    for file_name in os.listdir(r"D:\\Youtube_Voices_Test\\GeekyRanjit\\"):
    
        file = r"D:\\Youtube_Voices_Test\\GeekyRanjit\\" + file_name

        data, sr = librosa.load(file)
        mfcc = compute_features(data, sr)
        t_counter += 1
        if len(mfcc) == num_mfcc_vectors_per_segment:
            data_dict["mfcc"].append(mfcc.tolist())
            data_dict["labels"].append(1)
            data_dict["mapping"].append("GeekyRanjit")
            counter += 1
       
    '''mkbhd'''
    for file_name in os.listdir(r"D:\\Youtube_Voices_Test\\mkbhd\\"):
    
        file = r"D:\\Youtube_Voices_Test\\mkbhd\\" + file_name

        data, sr = librosa.load(file)
        mfcc = compute_features(data, sr)
        t_counter += 1
        if len(mfcc) == num_mfcc_vectors_per_segment:
            data_dict["mfcc"].append(mfcc.tolist())
            data_dict["labels"].append(2)
            data_dict["mapping"].append("mkbhd")
            counter += 1

    '''mosh'''
    for file_name in os.listdir(r"D:\\Youtube_Voices_Test\\mosch"):
    
        file = r"D:\\Youtube_Voices_Test\\mosch\\" + file_name

        data_dict["mapping"].append("mosh")
        data, sr = librosa.load(file)
        mfcc = compute_features(data, sr)
        t_counter += 1
        if len(mfcc) == num_mfcc_vectors_per_segment:
            data_dict["mfcc"].append(mfcc.tolist())
            data_dict["labels"].append(3)
            data_dict["mapping"].append("mosh")
            counter += 1

    print(counter)
    print(t_counter)
    with open(json_path, "w") as fp:
        json.dump(data_dict, fp, indent=4)


if __name__ == "__main__":
    load_data()
