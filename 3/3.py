from gtts import gTTS
from playsound import playsound
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

file_name = "mytext.txt"
try:
    with open(file_name, 'rt', encoding='UTF-8') as f:
        file_read = f.read()
except Exception as e:
    print(e)

tts = gTTS(file_read, lang='ko')
sound_file = file_name[:-3] + "mp3"
tts.save(sound_file)

playsound(sound_file)