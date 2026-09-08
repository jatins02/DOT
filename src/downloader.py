import yt_dlp
import os
import sys


def get_ffmpeg_directory():
    if getattr(sys, "frozen", False):
        application_directory = os.path.dirname(sys.executable)
    else:
        application_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    ffmpeg_directory = os.path.join(application_directory, "ffmpeg")
    if os.path.isdir(ffmpeg_directory):
        return ffmpeg_directory

    return None

def download_playlist(playlist_url):
    os.makedirs("downloads", exist_ok=True)
    ffmpeg_directory = get_ffmpeg_directory()
    ydl_opts = {
        'format': 'bestaudio/best',                         # get the highest quality audio available
        'outtmpl': f'downloads/%(title)s.%(ext)s',          # save path and filename
        'noplaylist': False,                                # ensure it only downloads the specific video, not the whole playlist again
        'ffmpeg_location': ffmpeg_directory,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
        'quiet': True,                                      # set to True if you want to hide the download progress bars
    }
    try: 
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([playlist_url])
    except:
        print(f"error in donwloading playlist")
