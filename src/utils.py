RED = "\033[0;31m"
GREEN =  "\033[0;32m"
RESET = "\033[0m"

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

