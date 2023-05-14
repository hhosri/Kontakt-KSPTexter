# Kontakt-KSPTexter

Kontakt-KSPTexter is a Python script that generates the appropriate .txt files for .png spritesheets. It is designed to make the process of creating Kontakt instrument GUIs faster and easier.

## How to Use

1. Copy the scripts to the folder where your .png files are located.
2. Open a terminal or command prompt and navigate to the folder where the scripts and .png files are located.</br>
3. Run `python3 KspTexter.py`
4. The script will generate all the appropriate .txt files in the same folder. The files will be initialized with the proper name and number of frames, with all other parameters default to 0/no (except for alpha, which is set to "yes").

## Naming Conventions

To ensure that the script works properly, it's important to follow these naming conventions:

### Backgrounds and Icons

* For background images: `anyName_background.png`
* For icon images: `anyName_icon.png`

### Buttons, Switches, and Menus

* For button images: `anyName_button.png`
* For switch images: `anyName_switch.png`
* For menu images: `anyName_menu.png`

### Sliders and Labels

* For slider images: `anyName_slider_numOfFrames.png`
* For label images: `anyName_label_numOfFrames.png`

Note: Replace `anyName` with a unique name for your images, and `numOfFrames` with the number of frames in your spritesheet.
