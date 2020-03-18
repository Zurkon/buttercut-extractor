import os
import sys
import argparse

parser = argparse.ArgumentParser(description="Download audio file from Youtube videos")
parser.add_argument(
    "-i", action="store", dest="url", required=True, help="URL from the video that you want extract audio.",
)
parser.add_argument(
    "-p",
    "--playlist",
    action="store_true",
    dest="isPlaylist",
    required=False,
    help="Indicates that the URL is a playlist. The program will download audio of each video in the playlist.",
)
parser.add_argument(
    "-o",
    action="store",
    dest="folder",
    required=False,
    help="Create a Folder with the specified name and save the audio files in it.",
)

args = parser.parse_args()

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
YT_DL_PATH = BASE_PATH + r"\youtube-dl"

simulado = False
URL = args.url
PLAYLIST = args.isPlaylist
FOLDER_NAME_TO_CREATE = args.folder

# print(URL)
# print(PLAYLIST)

if not simulado:
    folder_name = "downloads"
    folder_exists = os.path.exists(folder_name)

    if not folder_exists:
        os.mkdir(folder_name)

    download_path = f"{os.getcwd()}/{folder_name}"

    os.chdir(YT_DL_PATH)

    if PLAYLIST:
        if FOLDER_NAME_TO_CREATE:
            folder_name = FOLDER_NAME_TO_CREATE
            folder_exists = os.path.exists(f"{download_path}/{folder_name}")

            if not folder_exists:
                os.mkdir(f"{download_path}/{folder_name}")
                download_path = download_path + "/" + folder_name
                print(download_path)

        os.system(
            f'python -m youtube_dl --yes-playlist --add-metadata --extract-audio --audio-format mp3 --audio-quality 0 -o "{download_path}/%(title)s.%(ext)s" {URL}'
        )
        # print("playlist download")
    else:
        os.system(
            f'python -m youtube_dl --extract-audio --audio-format mp3 --audio-quality 0 -o "{download_path}/%(title)s.%(ext)s" {URL}'
        )
        # print("music download")

print("All Done!")

