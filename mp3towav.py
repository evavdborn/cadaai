import os
from pydub import AudioSegment

path = os.getcwd() 
print(path)
# In Windows this is the root path is different: We will change it to the right path
os.chdir("C:\\Users\\s157874\\Documents\\GitHub\\wavegan\\data\\dir_long_audio_files\\houspa")
path = os.getcwd() 

audio_files = os.listdir()

print(audio_files)

# You dont need the number of files in the folder, just iterate over them directly using:
for file in audio_files:
    #spliting the file into the name and the extension
    name, ext = os.path.splitext(file)
    if ext == ".mp3":
       mp3_sound = AudioSegment.from_mp3(file)
       #rename them using the old name + ".wav"
       mp3_sound.export("{0}.wav".format(name), format="wav")