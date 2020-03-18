import os
import sys
import argparse

parser = argparse.ArgumentParser(description="Split audio file into multiple files")
parser.add_argument(
    "-i",
    action="store",
    dest="audio_file",
    required=True,
    help="input audio file that you wanna split. It needs to be inside Downloads Folder.",
)
parser.add_argument(
    "-l",
    action="store",
    dest="playlist_file",
    required=True,
    help="text file with songs name and duration. It needs to be inside Downloads Folder.",
)
parser.add_argument(
    "-o",
    action="store",
    dest="dest_folder",
    required=False,
    help="Folder's name to save the songs. By default will be the audio file name.",
)
parser.add_argument(
    "-I",
    "--include-index",
    action="store_true",
    dest="includeIndex",
    required=False,
    help="Indicates that you want the program to insert the track number in filename",
)

args = parser.parse_args()

FILE_NAME = args.audio_file
PLAYLIST_NAME = args.playlist_file
FOLDER_NAME = FILE_NAME.split(".")[0] if not args.dest_folder else args.dest_folder
INSERT_INDEX = args.includeIndex


BASE_PATH = os.path.dirname(os.path.abspath(__file__))

YT_DL_PATH = BASE_PATH + r"\youtube-dl"
DOWNLOADS_PATH = BASE_PATH + r"\downloads"


FOLDER_PATH = DOWNLOADS_PATH + "\\" + FOLDER_NAME

PLAYLIST_PATH = DOWNLOADS_PATH + "\\" + PLAYLIST_NAME

if not os.path.exists(DOWNLOADS_PATH + "\\" + FILE_NAME):
    print("File name not found...")
    sys.exit(0)

songs = []
songs_duration = []
songs_filename = []
songs_artist = []
songs_name = []


# Change to the youtube-dl folder. The ffmpeg.exe is there
os.chdir(YT_DL_PATH)

# Check if folder exists, if not create it
folder_exists = os.path.exists(FOLDER_PATH)

if not folder_exists:
    os.mkdir(FOLDER_PATH)

# Read the text file with plyalist's durations and name of songs
with open(PLAYLIST_PATH, mode="r") as track_file:
    line = track_file.readline()
    while line != "":
        songs.append(line.rstrip())
        # print(line)
        line = track_file.readline()

# split the duration and name of each song on 2 separated lists
for song in songs:
    songs_duration.append(song.split(" = ")[0])
    songs_filename.append(song.split(" = ")[1])

# split the artist name and the song name of each song on 2 separated lists
# [:-1] makes the For Loop iteracts to all items from 'song_filename' list except for the last one ('END')
for song in songs_filename[:-1]:
    songs_artist.append(song.split(" - ")[0])
    songs_name.append(song.split(" - ")[1])

# print(songs_artist)
# print("Length: " + str(len(songs_artist)))
# print(songs_name)
# print("Length: " + str(len(songs_name)))
# print(songs_filename)
# print("Length: " + str(len(songs_filename)))
# print(songs_duration)
# print("Length: " + str(len(songs_duration)))

# zip into only iterable object
songs = zip(songs_duration, songs_duration[1:], songs_filename, songs_name, songs_artist)

# call FFMPEG for each song
for index, (start, end, filename, name, artist) in enumerate(songs):
    print(f"{start} - {end} - {name}")
    if INSERT_INDEX:
        include_zero = '0' if index <= 9 else ''
        os.system(f'ffmpeg -i "{DOWNLOADS_PATH}\{FILE_NAME}" -metadata track={index + 1} -metadata title="{name}" -metadata artist="{artist}" -metadata album="{FOLDER_NAME}" -ss {start} -to {end} -c copy "{FOLDER_PATH}\{include_zero}{index + 1} {filename}.mp3" ')
    else:
        os.system(f'ffmpeg -i "{DOWNLOADS_PATH}\{FILE_NAME}" -metadata track={index + 1} -metadata title="{name}" -metadata artist="{artist}" -metadata album="{FOLDER_NAME}" -ss {start} -to {end} -c copy "{FOLDER_PATH}\{filename}.mp3" ')

print("All Done!")

