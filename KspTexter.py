import os
import sys

RED = "\033[0;31m"
GREEN =  "\033[0;32m"
RESET = "\033[0m"
#--------------------------INIT---------------------------
current_dir = ""
png_files = []
all_controls = []

#function that creates a .txt file and fills it with the right information
def txt_maker(file_name, frames):
    with open((file_name + ".txt"), "w") as file:
        file.write("Has Alpha Channel: yes\n")
        file.write(f'Number of Animations: {frames}\n')
        file.write("Horizontal Animation: no\n")
        file.write("Vertical Resizable: no\n")
        file.write("Horizontal Resizable: no\n")
        file.write("Fixed Top: 0\n")
        file.write("Fixed Bottom: 0\n")
        file.write("Fixed Left: 0\n")
        file.write("Fixed Right: 0\n")

#class ui_control for each control component
class ui_control:
    def __init__(self, file_name, ui_name, type, frames):
        self.file_name = file_name
        self.ui_name = ui_name
        self.type = type
        self.frames = frames

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

if (len(png_files) == 0):
    print(f'{RED}Could not find any .PNG files in the current folder{RESET}')
    sys.exit()

#create objects for each ui_control with the appropriate file_name, type, ui name and frames number
for png_item in png_files:
    split_name = png_item.split("_")
    if (len(split_name) == 2):
        if (split_name[1] == "background" or split_name[1] == "icon"):
            newOne = ui_control(png_item, split_name[0], split_name[1], 1)
            all_controls.append(newOne)
        elif (split_name[1] == "button" or split_name[1] == "switch" or split_name[1] == "menu"):
            newOne = ui_control(png_item, split_name[0], split_name[1], 6)
            all_controls.append(newOne)
        elif (split_name[1] == "slider" or split_name[1] == "label" ):
            print(f'{RED}this type of ui {GREEN}{split_name[1]}{RED} in the file {GREEN}{png_item}.png {RED}needs one extra parameter for the frames number{RESET}')
        elif not(split_name[1] == "slider" or split_name[1] == "label" or split_name[1] == "button" or split_name[1] == "switch" or split_name[1] == "menu" or split_name[1] == "background" or split_name[1] == "icon" ):
            print(f'{RED}invalid UI type: {GREEN}{split_name[1]}{RED} in the file {GREEN}{png_item}.png{RESET}')
    elif (len(split_name) == 3):
        if (split_name[1] == "slider" or split_name[1] == "label"):
            if not (split_name[2].isdigit()):
                print(f'{RED}Format Error in: {GREEN}{png_item}.png{RED} - 3rd argument after _ should be a numeric valyle (Number of frames){RESET}')
            else:
                newOne = ui_control(png_item, split_name[0], split_name[1], split_name[2])
                all_controls.append(newOne)
        elif(split_name[1] == "button" or split_name[1] == "switch" or split_name[1] == "menu" or split_name[1] == "icon" or split_name[1] == "background"):
            print(f'{RED}the type: {GREEN}{split_name[1]}{RED} in {GREEN}{png_item}.png {RED}doesn\'t need the number of frames in it\'s name{RESET}')
        elif not(split_name[1] == "slider" or split_name[1] == "label" or split_name[1] == "button" or split_name[1] == "switch" or split_name[1] == "menu" or split_name[1] == "icon" or split_name[1] == "background"):
            print(f'{RED}invalid UI type: {GREEN}{split_name[1]}{RED} in the file {GREEN}{png_item}.png{RESET}')
    else:
        print(f'{RED}Wrong format for the file {GREEN}{png_item}.png{RESET}')

#create a .txt file for each control
for control in all_controls:
    txt_maker(control.file_name, control.frames)

#result
print(f'{GREEN}---------------')
if (len(all_controls) == len(png_files)):
    print(f'{GREEN}** ALL PNG FILES CONVERTED SUCCESFULLY **')
else:
    print(f'{RED}** NOT ALL PNG FILES CONVERTED SUCCESFULLY **')
    print(f'{RED}{len(all_controls)}{GREEN} TXT out of {RED}{len(png_files)}{GREEN} PNG files generated.')
print(f'{GREEN}---------------')


