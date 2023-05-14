import os
import sys
from utils import *


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

#create objects for each ui_control with the appropriate file_name, type, ui name and frames number
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

