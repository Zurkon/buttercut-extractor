# Buttercut-extractor
A Python Command-line Interface to Extract audio from Youtube videos and Split them :headphones: .

- [Description](#description)
- [Setup](#setup)
- [Usage](#usage)
- [Arguments](#arguments)
- [COPYRIGHT](#copyright)

# Description
The idea behind of **Buttercut-extrator** project was to create a program to download those  1hour music videos :headphones: and create the audio files for each track in that playlist video separately :musical_note: .

# Setup
First of all this project have dependencies on [youtube-dl](https://github.com/ytdl-org/youtube-dl) and [FFMPEG](https://www.ffmpeg.org/download.html) . You can either install them on your machine or just put them here inside this folder.

Make sure that you have Python installed on your machine:
> Python version: 3.7.6 or above

## Setup inside this folder
Placing the dependencies inside that project's folder makes it more portable and can be easily executed on other machines.

First of all, put the `youtube-dl` on the root of this project
```
git clone https://github.com/ytdl-org/youtube-dl.git
```

After download `FFMPEG` get the `ffmpeg.exe` inside the `bin/` folder and place it inside the `youtube-dl` folder at the root of your project. Something like this:
```
Buttercut-extrator/youtube-dl/ffmpeg.exe
```

Now you are ready to go :sunglasses: :sparkles:

# Usage
The project has two main scripts:
Script       | Description
-------------|-------------
`download.py`| extracts audio from youtube url you pass
`splitter.py`| splits the audio file based on the time of each song that you pass inside a simple `playlist.txt`

First, you need to extract audio from the youtube video that you wanna split.
```
python download.py -i {url}
```

> ##### note that you can still use `download.py` to extract audio from single song video.

The script will create a `downloads` folder on the project's root and place the audio file inside.

Next step is create a simple `playlist.txt` inside `downloads` folder with song's name and the time that starts each song in the video. The video description usually has this information.

format the text on `playlist.txt` as bellow:
```
00:00 = Artist's name - song's name
04:55 = Artist's name - song's name
08:55 = Artist's name - song's name
14:12 = Artist's name - song's name
17:50 = Artist's name - song's name
22:23 = Artist's name - song's name
23:11 = Artist's name - song's name
26:55 = Artist's name - song's name
30:26 = Artist's name - END
```

## Explaining
* each line represents a song file that will be created;
* `time` needs to be in `MM:SS` format;
* the `=` is used to split the `time` and the `filename` into separate lists;
* the `-` is used to split the `Artist's name` and the `song's name` into separate lists;
* **you need to put the time that video ends** - the last line `30:26 = Artist's name - END` indicates the end of the audio file.

> ##### if you dont put the last line, the script will not create the last song audio file from the splitted audio.

After that just execute the `splitter.py` scripts:
```
python splitter.py -i "audiofile.mp3" -l "playlist.txt"
```

The songs will be saved on `downloads/` inside a folder with audiofile's name.

# Arguments

## Download arguments

Use the `download.py` to extract audio from youtube videos.
```
python download -i {url}
```

You can put additional arguments for custom extraction:
```
usage: download.py [-h] -i URL [-p] [-o FOLDER]

Download audio file from Youtube videos        

optional arguments:
  -h, --help              show this help message and exit
  -i [URL]                URL from the video that you want extract audio.
  -p, --playlist          Indicates that the URL is a playlist. It will download each audio in the playlist.
  -o [FOLDER]             Create a Folder with the specified name and save the audio files in it.
```

## Splitter arguments

Use the `splitter.py` to split and create a audiofile for each song on the `audiofile.mp3`

```
python splitter.py -i "audiofile.mp3" -l "playlist.txt"
```

You can put additional arguments for custom split:
```
usage: splitter.py [-h] -i AUDIO_FILE -l PLAYLIST_FILE [-o DEST_FOLDER] [-I]

Split audio file into multiple files

optional arguments:
  -h, --help               show this help message and exit
  -i [AUDIO_FILE]          input audio file that you wanna split. It needs to be inside Downloads Folder.
  -l [PLAYLIST_FILE]       text file with songs name and duration. It needs to be inside Downloads Folder.
  -o [DEST_FOLDER]         Folder's name to save the songs. By default will be the audio file name.
  -I, --include-index      Indicates that you want the program to insert the track number in filename.
```

# COPYRIGHT

Just like the `youtube-dl`, this project is released into the public domain.
