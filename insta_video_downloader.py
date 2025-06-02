# instagram video downloader using yt-dlp library with 1080p quality support.

# import yt_dlp
# import os

# # ✅ Add ffmpeg to PATH correctly
# os.environ['PATH'] += os.pathsep + r'C:\ffmpeg\bin'

# # ✅ Output folder
# output_folder = r'C:\Users\sarra\OneDrive\Desktop\ops\instagram_ops'
# os.makedirs(output_folder, exist_ok=True)

# def download_instagram_video(url):
#     ydl_opts = {
#         'format': 'bestvideo+bestaudio/best',  # ✅ Download best video and best audio
#         'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
#         'merge_output_format': 'mp4',  # ✅ Merge into mp4
#         'postprocessors': [
#             {
#                 'key': 'FFmpegMerger',  # ✅ Merge video + audio
#             }
#         ],
#         'noplaylist': True,
#         'quiet': False,
#         'no_warnings': True,
#     }

#     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#         ydl.download([url])

# if __name__ == "__main__":
#     video_url = input("Enter the Instagram video URL: ").strip()
#     if video_url:
#         download_instagram_video(video_url)
#         print("\n✅ Download complete!")
#         print("📁 Saved to:", output_folder)
#     else:
#         print("⚠️ No URL provided. Exiting.")


#==================instagram video downloader using yt-dlp library with 4k quality support======================================================

# instagram video downloader using yt-dlp library with 4k quality support.
# import os
# import yt_dlp

# # ✅ Add ffmpeg to PATH
# os.environ['PATH'] += os.pathsep + r'C:\ffmpeg\bin'  # Make sure this path is correct on your system

# # ✅ Set the output folder
# output_folder = r'C:\Users\sarra\OneDrive\Desktop\ops\instagram_ops'
# os.makedirs(output_folder, exist_ok=True)  # Create folder if it doesn't exist

# def download_instagram_video(url):
#     ydl_opts = {
#         'format': 'bestvideo[height<=2160]+bestaudio/best/best',  # up to 4K video + best audio
#         'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),  # Save to your custom folder
#         'merge_output_format': 'mp4',
#         'postprocessors': [{
#             'key': 'FFmpegMerger',
#         }],
#         'noplaylist': True,
#         'quiet': False,
#         'no_warnings': True,
#     }

#     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#         ydl.download([url])

# if __name__ == "__main__":
#     video_url = input("Enter the Instagram video URL: ").strip()
#     if video_url:
#         download_instagram_video(video_url)
#         print("\n✅ Download complete!")
#         print("📁 Saved to:", output_folder)
#     else:
#         print("⚠️ No URL provided. Exiting.")


#===================================================================================================================================================



