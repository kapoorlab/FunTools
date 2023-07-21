import speech_recognition as sr
from playsound import playsound

def main(sound_file):
       
       r = sr.Recognizer()
       playsound(sound_file)
       audio_file = sr.AudioFile(sound_file)
       with audio_file as source:
           audio = r.record(source)
       text = r.recognize_google(audio) 
       print(f'The audio that you just heard said: {text}')
       
       
if __name__=="__main__":
   
   sound_files = ['./english.wav', './audio/example.mp4']   
   
   
   for sound_file in sound_files:
     main(sound_file)   