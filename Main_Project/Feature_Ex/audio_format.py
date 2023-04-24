import os
from pydub import AudioSegment

directory = r"D:\\YouTube_voices\\Mosh\\"
dst_path = r"D:\\Youtube_Voice_Wav\\Mosh\\"
counter = 1

for file in os.listdir(directory):
    print(file)
    src = directory + file
    dst = dst_path + "track_" + str(counter) + '.wav'
    # convert wav to mp3                                                            
    sound = AudioSegment.from_mp3(src)
    sound.export(dst, format="wav")
    counter += 1
