# Love in the Terminal: A Linux Romance

## Setup

(0. Add Ren'Py extension to VSCode)
1. Download Ren'Py SDK from https://www.renpy.org/latest.html
2. Unzip the SDK and run the `renpy.exe` file
3. Set up the project folder
4. Git clone this repository into the project folder
5. Refresh Ren'Py's projects
6. Load the project, and run it with "Launch Project"

You will also need to download the images and place them in game/images. There's a curl script you can run by opening a terminal and running "./get-images.sh" in the same directory as the script. This will download the images. You then need to place them in game/images. Currently, there is only the background images, so you should created a folder in images called "backgrounds" and place the images in there.

## Project Overview
This dating sim reimagines Linux distros as charismatic entities within the Kernel Kingdom. Players navigate relationships with Ubuntu, Fedora, Arch Linux, Debian, and Linux Mint through branching dialogue and stat-based  
compatibility.

## Current Features
- 5 dateable characters with unique personalities and routes
- Stat tracking: intimacy, shared interests, risk, innovation
- Time management system (morning/afternoon/evening)
- Branching dialogue trees
- Compatibility calculation system

## Required Art Assets

### Character Design Guidelines
- Ubuntu: Modern business casual, orange/purple accents
- Fedora: Tech professional, blue/red theme
- Arch: Minimalist monochrome style
- Debian: Classic professional attire
- Mint: Elegant casual wear

### Background Art 
- Terminal Festival main plaza
- Ubuntu's Pavilion
- Fedora's Lounge
- Arch's Hub
- Debian's Center
- Mint's Cafe

## TODO

### Character Sprites
Each character needs these expressions (PNG, 1920x1080):
- neutral (default pose)
- happy/smiling
- flirting/charming
- thinking/contemplative
- surprised/shocked
- worried/concerned
- excited/enthusiastic
- annoyed/frustrated
- blushing/embarrassed
- special (unique to character)

### Event CGs
5 special scenes per character:
- First meeting
- Casual interaction
- Technical collaboration
- Romantic moment
- Route ending
