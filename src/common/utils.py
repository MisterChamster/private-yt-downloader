from socket import create_connection

from typing import Literal
from pathlib import Path
import json



class Utils():
    settings_path: Path

    # =========================================================
    # ======================= URL UTILS =======================
    # =========================================================
    @staticmethod
    def clean_url(in_url: str) -> str:
        bad_stuff = ['&list', #If user copies browser link when on vid from playlist
                    '&si',   #ID tracker lmao
                    '?si',
                    '&ab_channel', #A/B testing
                    '&feature',    #How opened
                    '&pp',         #Promotion
                    '&t']          #Time stamp

        for el in bad_stuff:
            if el in in_url:
                in_url = in_url[:in_url.find(el)]
        return in_url


    @staticmethod
    def determine_url_type(url: str) -> Literal['plist', 'single'] | None:
        if ((len(url) > 17 and url.startswith('https://youtu.be/')) or
            (len(url) > 29 and url.startswith('https://www.youtube.com/watch'))):
            return 'single'

        elif (len(url) > 34 and url.startswith('https://youtube.com/playlist?list=')):
            return 'plist'

        else:
            return


    # =========================================================
    # ====================== JSON UTILS  ======================
    # =========================================================
    @staticmethod
    def save_value_to_settings(
        json_key: Literal[
            "SAVE_PATH",
            "PLIST_SAVE_FORMAT",
            "PLIST_DEFAULT_SAVE_PATH",
            "PLIST_NUMBERING",
            "PLIST_DUPLICATES",
            "MIMI",
            "PIPI"],
        json_val: bool|str|int|float
    ) -> None:

        with open(Utils.settings_path) as f:
            config = json.load(f)

        config[json_key] = json_val
        with open(Utils.settings_path, "w") as f:
            json.dump(config, f, indent=2)


    @staticmethod
    def fix_value_in_json(
        adress:      Path,
        json_key:    str,
        default_val: bool|str|int|float
    ) -> None:

        with open(adress) as f:
            config = json.load(f)

        if json_key not in config.keys():
            print(f"[WARNING] Key value '{json_key}' could not be found in {adress}. Resorting to default value ('{default_val}').\nFixing {adress}...")
            try:
                Utils.save_value_to_settings(json_key, default_val)
                print(f"{json_key} has been fixed in {adress}")
            except Exception as e:
                print(f"{json_key} could not have been fixed in {adress}\n{e}")
        return


    @staticmethod
    def _get_val_from_json(
        adress:   Path,
        json_key: str
    ) -> str|bool|int|float:

        with open(adress) as f:
            config = json.load(f)

        temp = config[json_key]
        return temp


    @staticmethod
    def get_val_from_settings(json_key: str) -> str|bool|int|float:
        return Utils._get_val_from_json(
            Utils.settings_path,
            json_key)


    # =========================================================
    # ====================== UTILS UTILS ======================
    # =========================================================
    @staticmethod
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


    @staticmethod
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


    @staticmethod
    def get_ydl_options(extension: str) -> dict:
        ydl_opts = {"quiet": True}
        if extension == "mp4":
            ydl_opts["merge_output_format"] = "mp4"
            ydl_opts["format"] = "bestvideo+bestaudio/best"
        elif extension == "mp3":
            ydl_opts["postprocessors"] = [
                {"key": "FFmpegExtractAudio",
                "preferredcodec": "mp3"}]
            ydl_opts["format"] = "bestaudio"
        elif extension == "flac":
            ydl_opts["postprocessors"] = [
                {"key": "FFmpegExtractAudio",
                "preferredcodec": "flac"}]
            ydl_opts["format"] = "bestaudio"

        return ydl_opts
