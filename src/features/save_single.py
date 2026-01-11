from yt_dlp import YoutubeDL
from os import path
from src.common.askers import Askers
from src.common.utils import (illegal_char_remover,
                              is_internet_available,
                              get_ydl_options)
from src.common.ydl_support import get_video_title



def save_single(url: str) -> None:
    extension = Askers.ask_save_ext()
    print()

    ydl_opts = get_ydl_options(extension)
    og_title = get_video_title(url)

    save_path = Askers.ask_save_path()
    if save_path == "":
        print("Empty path was chosen.")
        return
    ydl_opts["paths"] = {"home": save_path}

    finalname = illegal_char_remover(og_title)
    i = 1
    while path.exists(save_path + "/" + finalname):
        finalname += "_d"*i
        i += 1
    ydl_opts["outtmpl"] = finalname

    print("Downloading...")
    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"{finalname} has been successfully downloaded.\n\n")
    except:
        if not is_internet_available():
            print("Internet connection failed.\n\n")
        else:
            print("Something went wrong.\n\n")
        return
