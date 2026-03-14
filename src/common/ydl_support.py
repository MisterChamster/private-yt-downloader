from yt_dlp import YoutubeDL

from src.common.utils import Utils



def get_video_title(url):
    ydl_getdata = {
        'quiet': True,
        'extract_flat': True,
        'force_generic_extractor': True}

    try:
        with YoutubeDL(ydl_getdata) as ydl:
            return ydl.extract_info(url, download=False)["title"]
    except:
        if not Utils.is_internet_available():
            print("Internet connection failed.\n\n")
        else:
            print("Something went wrong.\n\n")
        return "Error"


def get_plist_dict(url) -> dict | None:
    ydl_getdata = {
        'quiet': True,
        'extract_flat': True,
        'force_generic_extractor': True}

    try:
        with YoutubeDL(ydl_getdata) as ydl:
            extract_info = ydl.extract_info(url, download=False)
            return extract_info
    except:
        if not Utils.is_internet_available():
            print("Internet connection failed.\n\n")
        else:
            print("Something went wrong.\n\n")
        return
