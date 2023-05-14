RED = "\033[0;31m"
GREEN =  "\033[0;32m"
RESET = "\033[0m"

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
