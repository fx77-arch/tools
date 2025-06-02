
import os
import yt_dlp

def download_audio_as_mp3(youtube_url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'C:/Users/sarra/OneDrive/Desktop/ops/%(title)s.%(ext)s',  # C:/Users/sarra/OneDrive/Desktop/ops/ this is the path where we can store the outputs files
        'keepvideo': True,
        'quiet': False,        ## C:/Users/sarra/OneDrive/Desktop/ops/ this is the path where we can store the outputs files also we can modify the path to store another folder.
        'keepvideo': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'noplaylist': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])

if __name__ == "__main__":
    print("Saving to:", os.path.abspath("C:\\Users\\sarra\\OneDrive\\Desktop\\ops"))

    url = input("Enter the YouTube video URL: ").strip()
    if url:
        download_audio_as_mp3(url)
    else:
        print("No URL entered. Exiting.")

        
        



#  example: https://youtu.be/3bxYkBVzcmw?si=sjImO_9dZpnKB5Bk