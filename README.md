# About
This script aims to change metadata for albums/music distributed by labels that add their name to the tags. An example is New Standard Elite

### Warning
This script commits metadata automatically and does not make a backup. I would personally backup any music in case you cant afford to lose it, or don't feel like redownloading ones that could potentially error. 

### Features
1. Changes album artist and artist tags to the correct artist
2. If the album is a split between multiple bands, by default it will make seperate albums for each artist. This is a personal preference thing, and can be toggled off in the config.json file.
3. Artist names will be changed to a titlecased version (ex. PUTRID PILE will change to Putrid Pile)
4. Singles will append the single title and the word Single to the album tag

# Installation for Binaries
1. Download Zip file for OS
2. Unzip to desired location
3. Edit config.json (if needed)
4. If not editing config to point to a custom path, put music to be edited in the music folder within the zip
5. Run the executable
6. Done!!!

# Running in terminal
1. Clone this repo
  ```git clone https://github.com/Nathan-Wunschl/Anodizer/main && cd Anodizer```
2. Install requirements
  ```pip install -r requirements.txt```
3. Edit config.json if desired
4. If using default config, move music to the music folder within the repo
5. Run the script!
  ```python3 main.py```
