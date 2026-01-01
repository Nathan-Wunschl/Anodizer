import os
from titlecase import titlecase
import music_tag
import json

types = [".mp3", ".aac", ".ogg", ".flac", ".m4a", ".wav", ".aiff", ".aif"]

with open("config.json") as file:
    config = json.load(file)
    path = config["path_override"]
    labels = list(config["labels"])
    separators = list(config["separators"])
    split = bool(config["split"])

if path == "":
    path = "./music"

def label_check(f):
    skip = False
    if "split" in str(f["album"]).lower():
        split_check(f)
        skip = True
    for label in labels:
        if label in str(f["albumartist"]):
            for sep in separators:
                if not skip:
                    if sep in str(f["album"]):
                        artist = titlecase(str(f["album"]).split(f" {sep} ", 1)[0].lower())
                        if artist  + f" {sep} " in str(f["album"]):
                            album = str(f["album"]).split(f" | ", 1)[1]
                            f["album"] = album
                    else:
                       artist = f["artist"]
                    f["album artist"] = artist
                    f["artist"] = artist
                    f.save()
        else:
            f['albumartist'] = titlecase(str(f['albumartist']))
            f['artist'] = titlecase(str(f["artist"]))
            f.save()

def split_check(f):
    for sep in separators:
        if sep in str(f["tracktitle"]):
            artist = str(f["tracktitle"]).split(f" {sep} ")[0]
            f["artist"] = artist
            if split:
                f["albumartist"] = artist
            f.save()
            if artist in str(f['tracktitle']):
                f["tracktitle"] = str(f["tracktitle"]).replace(artist + f" {sep} ", "")
                f.save()

for subdir, dirs, files in os.walk(path):
    for track in sorted(files):
        file = subdir + "/" + track
        if track.endswith(tuple(types)):
            if not track.startswith("._"):
                try:
                    f = music_tag.load_file(file)
                    label_check(f)
                    if str(f['album'] == ""):
                        f['album'] = str(f["tracktitle"] + " Single")
                        f.save()
                except Exception as e:
                    print(f"Error loading file: {e}")