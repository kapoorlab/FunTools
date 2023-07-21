import speech_recognition as sr
from playsound import playsound
from pytube import YouTube
def main(sound_file):
       
       r = sr.Recognizer()
       playsound(sound_file)
       audio_file = sr.AudioFile(sound_file)
       with audio_file as source:
           audio = r.record(source)
       text = r.recognize_google(audio) 
       print(text)
       
def download_audio(video_url):
    video = YouTube(video_url)
    audio = video.streams.filter(only_audio = True).first()

    try:
        audio.download("./audio")
    except:
        print("Failed to download audio")

    print("audio was downloaded successfully")    
       
if __name__=="__main__":
   
   sound_files = ['./english.wav', './audio/example.mp4']   
   
   
   for sound_file in sound_files:
     main(sound_file)   