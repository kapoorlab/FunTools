from pytube import YouTube



def download_audio(video_url):
    video = YouTube(video_url)
    audio = video.streams.filter(only_audio = True).first()

    try:
        audio.download("./audio")
    except:
        print("Failed to download audio")

    print("audio was downloaded successfully") 
    
    
if __name__ == '__main__':
    
    video_url =  'https://www.youtube.com/watch?v=Vhh_GeBPOhs'
    download_audio(video_url)    