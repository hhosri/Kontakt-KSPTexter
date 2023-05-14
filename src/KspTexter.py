import os
import sys
from utils import *

current_dir = ""
png_files = []
all_controls = []

FRAME_PER_TYPE = {
    "background": 1,
    "icon": 1,
    "button": 6,
    "switch": 6,
    "menu": 6,
    "slider": None,
    "label": None
}

#for background-icon-button-switch-menu
def fixed_frames(split_name, png_item):
    if split_name[1] in list(FRAME_PER_TYPE.keys())[5:7]:
        print(f'{RED}this type of ui {GREEN}{split_name[1]}{RED} in the file {GREEN}{png_item}.png {RED}needs one extra parameter for the frames number{RESET}')
        return
    elif not split_name[1] in FRAME_PER_TYPE.keys():
        print(f'{RED}invalid UI type: {GREEN}{split_name[1]}{RED} in the file {GREEN}{png_item}.png{RESET}')
        return
    elif split_name[1] in list(FRAME_PER_TYPE.keys())[:2]:
        all_controls.append({"full_name":png_item, "ui_name":split_name[0], "frames":FRAME_PER_TYPE[split_name[1]]})
    elif split_name[1] in list(FRAME_PER_TYPE.keys())[2:5]:
        all_controls.append({"full_name":png_item, "ui_name":split_name[0], "frames":FRAME_PER_TYPE[split_name[1]]})

#for slider-label
def flexible_frames(split_name, png_item):
    if split_name[1] in list(FRAME_PER_TYPE.keys())[:5]:
        print(f'{RED}the type: {GREEN}{split_name[1]}{RED} in {GREEN}{png_item}.png {RED}doesn\'t need the number of frames in it\'s name{RESET}')
        return
    elif not split_name[1] in FRAME_PER_TYPE.keys():
        print(f'{RED}invalid UI type: {GREEN}{split_name[1]}{RED} in the file {GREEN}{png_item}.png{RESET}')
        return
    elif split_name[1] in list(FRAME_PER_TYPE.keys())[5:7]:
        if not split_name[2].isdigit():
            print(f'{RED}Format Error in: {GREEN}{png_item}.png{RED} - 3rd argument after _ should be a numeric valyle (Number of frames){RESET}')
            return
        else:
            all_controls.append({"full_name":png_item, "ui_name":split_name[0], "frames":split_name[2]})


#Get current directory of the executable OR script
if getattr(sys, 'frozen', False):
    current_dir = os.path.dirname(sys.executable)
else:
    current_dir = os.path.dirname(os.path.abspath(__file__))

#finds and stores all png files in a list
for file in os.listdir(current_dir):
    if file.endswith(".png"):
        png_files.append(file[:-4])

if not len(png_files):
    print(f'{RED}Could not find any .PNG files in the current folder{RESET}')
    sys.exit()

#creates a dict for each ui element with the appropriate: filename, type and number of frames
for png_item in png_files:
    split_name = png_item.split("_")
    if len(split_name) == 2:
        fixed_frames(split_name, png_item)
    elif len(split_name) == 3:
        flexible_frames(split_name, png_item)
    else:
        print(f'{RED}Wrong format for the file {GREEN}{png_item}.png{RESET}')

#create a .txt file for each control
for control in all_controls:
        txt_maker(control)

#result
print(f'{GREEN}---------------')
if len(all_controls) == len(png_files):
    print(f'{GREEN}** ALL PNG FILES CONVERTED SUCCESFULLY **')
else:
    print(f'{RED}** NOT ALL PNG FILES CONVERTED SUCCESFULLY **')
    print(f'{RED}{len(all_controls)}{GREEN} TXT out of {RED}{len(png_files)}{GREEN} PNG files generated.')
print(f'{GREEN}---------------')

