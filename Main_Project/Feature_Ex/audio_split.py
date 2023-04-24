import os
import librosa.display
import soundfile as sf 

audio_dir = r'D:\\Youtube_Voice_Wav\\GeekyRanjit\\'
out_dir = r"D:\\YouTube_voices\\GeekyRanjit\\"
counter = 3939
samples_wrote = 0
sr = 22050

for file_name in os.listdir(audio_dir):
    print(file_name)
    # First load the file
    audio = librosa.load(audio_dir+file_name)
    # Get number of samples for 5 seconds; 
    buffer = 5 * sr
    samples_total = len(audio)
    print(file_name)
    print(counter)

    while samples_wrote < samples_total:

        # check if the buffer is not exceeding total samples
        if buffer > (samples_total - samples_wrote):
            buffer = samples_total - samples_wrote

        block = audio[samples_wrote: (samples_wrote + buffer)]
        out_filename = "Track_" + str(counter) + '.wav'

        # Write 2 second segment
        sf.write(out_dir + out_filename, block, sr)
        counter += 1
        samples_wrote += buffer
    
    samples_wrote = 0
    
