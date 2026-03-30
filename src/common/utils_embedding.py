from pathlib import Path
from mutagen.easyid3 import EasyID3
from mutagen.flac import FLAC
from mutagen.oggvorbis import OggVorbis



def append_metadata_file_universal(
    file_path: Path,
    md_type: str,
    md_text: str
) -> None:
    # Safe against mac files ugh
    filename = file_path.name
    if filename.startswith("."):
        return

    audio = get_audio(file_path)

    audio[md_type] = md_text
    audio.save()


def get_audio(file_path: Path) -> FLAC | OggVorbis | EasyID3:
    extension = file_path.suffix

    if extension == ".mp3":
        try:
            audio = EasyID3(file_path)
        except Exception as e:
            print(f"Failed to create EasyID3 object. Error: {e}")
            return

    elif extension == ".flac":
        try:
            audio = FLAC(file_path)
        except Exception as e:
            print(f"Failed to create FLAC object. Error: {e}")
            return

    elif extension == ".ogg":
        try:
            audio = OggVorbis(file_path)
        except Exception as e:
            print(f"Failed to create OggVorbis object. Error: {e}")
            return

    if audio is None:
        print(f"Failed to load file: {file_path}")
        return

    return audio
