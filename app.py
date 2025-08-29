from gtts import gTTS
from playsound import playsound
import tempfile
import os
text="Hello BSD, How can I help you"

def do_tts(text):
    tts =gTTS(text)
    temp_file = tempfile.NamedTemporaryFile(suffix=".mp3",delete=False)
    tts.save(temp_file.name)
    #file_url="file://",os.path.abspath(temp_file.name)
    temp_file.close()
    return temp_file.name
    #return file_url
file_path = do_tts(text)
playsound(file_path)
os.remove(file_path)