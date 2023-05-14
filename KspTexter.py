import os
import sys

RED = "\033[0;31m"
GREEN =  "\033[0;32m"
RESET = "\033[0m"
#--------------------------INIT---------------------------
current_dir = ""
png_files = []
all_controls = []

FRAME_PER_TYPE = {
    "background": 1,
    "icon": 1,
    "button": 6,
    "switch": 6,
    "menu": 6,
}


def fixed_frames(split_name):
    if split_name[1] in ["background","icon"]:
        all_controls.append({"full_name":png_item, "ui_name":split_name[0], "frames":FRAME_PER_TYPE[split_name[1]]})

    elif split_name[1] in ["button", "switch", "menu"]:
        all_controls.append({"full_name":png_item, "ui_name":split_name[0], "frames":FRAME_PER_TYPE[split_name[1]]})

    elif split_name[1] in ["slider", "label" ]:
        print(f'{RED}this type of ui {GREEN}{split_name[1]}{RED} in the file {GREEN}{png_item}.png {RED}needs one extra parameter for the frames number{RESET}')
    elif not split_name[1] in FRAME_PER_TYPE.keys():
        print(f'{RED}invalid UI type: {GREEN}{split_name[1]}{RED} in the file {GREEN}{png_item}.png{RESET}')

def flexible_frames(split_name):
    if split_name[1] in ["slider", "label"]:
        if not split_name[2].isdigit():
            print(f'{RED}Format Error in: {GREEN}{png_item}.png{RED} - 3rd argument after _ should be a numeric valyle (Number of frames){RESET}')
        else:
            all_controls.append({"full_name":png_item, "ui_name":split_name[0], "frames":split_name[2]})

    elif split_name[1] in ["button","switch" ,"menu" ,"icon" ,"background"]:
        print(f'{RED}the type: {GREEN}{split_name[1]}{RED} in {GREEN}{png_item}.png {RED}doesn\'t need the number of frames in it\'s name{RESET}')
    elif not split_name[1] in FRAME_PER_TYPE.keys():
        print(f'{RED}invalid UI type: {GREEN}{split_name[1]}{RED} in the file {GREEN}{png_item}.png{RESET}')

#function that creates a .txt file and fills it with the right information
def txt_maker(control):
    with open((control["full_name"] + ".txt"), "w") as file:
        file.write("Has Alpha Channel: yes\n")
        file.write(f'Number of Animations: {control["frames"]}\n')
        file.write("Horizontal Animation: no\n")
        file.write("Vertical Resizable: no\n")
        file.write("Horizontal Resizable: no\n")
        file.write("Fixed Top: 0\n")
        file.write("Fixed Bottom: 0\n")
        file.write("Fixed Left: 0\n")
        file.write("Fixed Right: 0\n")

#class ui_control for each control component


#--------------------------CODE---------------------------

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
        fixed_frames(split_name)
    elif len(split_name) == 3:
        flexible_frames(split_name)
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

