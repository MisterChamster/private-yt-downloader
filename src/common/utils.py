from socket import create_connection
from typing import Literal



def clean_url(in_url: str) -> str:
    #If user copies browser link when on vid from playlist
    #ID tracker lmao
    #A/B testing
    #How opened
    #Promotion
    #Time stamp
    bad_stuff = ['&list', '?si', '&ab_channel', '&feature', '&pp', '&t']

    for el in bad_stuff:
        if el in in_url:
            in_url = in_url[:in_url.find(el)]
    return in_url


def determine_url_type(url: str) -> Literal['plist', 'single'] | None:
    if ((len(url) > 17 and url.startswith('https://youtu.be/')) or
          (len(url) > 29 and url.startswith('https://www.youtube.com/watch'))):
        return 'single'

    elif (len(url) > 34 and url.startswith('https://youtube.com/playlist?list=')):
        return 'plist'

    else:
        return


def is_internet_available() -> bool:
    """
    Checks internet availability.

    Returns:
        True:   Internet is available.
        False:  Internet is not available
    """
    try:
        create_connection(("www.google.com", 80))
        return True
    except OSError:
        return False


def illegal_char_remover(suspect_string: str) -> str:
    """
    Removes chars that are illegal in naming a file from string.

    From given string, function removes \\, /, :, *, ?, ", <, >, | 
    (chars illegal in naming files) and returns it.

    Args:
        suspect_string (str): String with potenetial characters to remove.

    Returns:
        str: Argument string without signs illegal in filenaming.
    """
    charlist = [a for a in suspect_string]
    i = 0
    while i < len(charlist):
        if charlist[i] in ["\\", "/", ":", "*", "?", '"', "<", ">", "|"]:
            charlist.pop(i)
        else:
            i += 1

    policedstring = "".join(charlist)
    if policedstring == "":
        return "Invalid title"
    return policedstring


def get_ydl_options(extension: str) -> dict:
    ydl_opts = {"quiet": True}
    if extension == "mp4":
        ydl_opts["merge_output_format"] = "mp4"
        ydl_opts["format"] = "bestvideo+bestaudio/best"
    elif extension == "mp3":
        ydl_opts["postprocessors"] = [{"key": "FFmpegExtractAudio",
                                       "preferredcodec": "mp3"}]
        ydl_opts["format"] = "bestaudio"
    elif extension == "flac":
        ydl_opts["postprocessors"] = [{"key": "FFmpegExtractAudio",
                                       "preferredcodec": "flac"}]
        ydl_opts["format"] = "bestaudio"

    return ydl_opts
