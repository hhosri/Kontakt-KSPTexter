import os
import sys
RED = "\033[0;31m"
GREEN =  "\033[0;32m"
RESET = "\033[0m"

#Get current directory of the executable OR script
def get_current_dir():
    if getattr(sys, 'frozen', False):
        current_dir = os.path.dirname(sys.executable)
    else:
        current_dir = os.path.dirname(os.path.abspath(__file__))
    return current_dir

current_dir = get_current_dir()

#function that creates a .txt file and fills it with the right information
def txt_maker(control):
    file_path = os.path.join(current_dir, (control["full_name"] + ".txt"))
    with open(file_path, "w") as file:
        file.write("Has Alpha Channel: yes\n")
        file.write(f'Number of Animations: {control["frames"]}\n')
        file.write("Horizontal Animation: no\n")
        file.write("Vertical Resizable: no\n")
        file.write("Horizontal Resizable: no\n")
        file.write("Fixed Top: 0\n")
        file.write("Fixed Bottom: 0\n")
        file.write("Fixed Left: 0\n")
        file.write("Fixed Right: 0\n")

