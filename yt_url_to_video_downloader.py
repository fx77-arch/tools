# This script is designed for downloading youtube conrtant as a video file.
import os
import yt_dlp

def download_yt_video(url, output_folder=r'C:\Users\sarra\OneDrive\Desktop\ops'):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    ydl_opts = {
        'format': 'bestvideo[height<=1080]+bestaudio/best',
        'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),  # Save here
        'noplaylist': True,
        'merge_output_format': 'mp4',
        'postprocessors': [{
            'key': 'FFmpegMerger',
        }],
        'quiet': False,
        'no_warnings': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    video_url = input('Enter the YouTube video URL: ').strip()
    if video_url:
        download_yt_video(video_url)
        print("Download complete! Check your folder at:")
        print(r'C:\Users\sarra\OneDrive\Desktop\ops')
    else:
        print("No URL entered. Exiting.")
