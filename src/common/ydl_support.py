from yt_dlp import YoutubeDL
from src.common.utils import is_internet_available



def get_video_title(url):
    ydl_getdata = {
        'quiet': True,
        'extract_flat': True,
        'force_generic_extractor': True}

    try:
        with YoutubeDL(ydl_getdata) as ydl:
            return ydl.extract_info(url, download=False)["title"]
    except:
        if not is_internet_available():
            print("Internet connection failed.\n\n")
        else:
            print("Something went wrong.\n\n")
        return "Error"


def get_plist_dict(url):
    ydl_getdata = {
        'quiet': True,
        'extract_flat': True,
        'force_generic_extractor': True}

    try:
        with YoutubeDL(ydl_getdata) as ydl:
            return ydl.extract_info(url, download=False)
    except:
        if not is_internet_available():
            print("Internet connection failed.\n\n")
        else:
            print("Something went wrong.\n\n")
        return
