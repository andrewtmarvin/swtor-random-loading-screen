from os import path, listdir
from shutil import copy2
from random import choice


def main():
    # Gets the directory that this script is stored in (should be placed in the LoadingScreens directory to work)
    dir_path = path.dirname(path.realpath(__file__))

    # Grabs a random picture from jpgs subdirectory
    try:
        new_pic = choice(listdir(dir_path + "\\jpgs"))
    except Exception as e:
        print('Error: ' + e.__str__())
        exit()

    # Copies and renames the randomly chosen pic to the correct location
    try:
        copy2(dir_path + "\\jpgs\\" + new_pic, dir_path + "\\loadingscreen.jpg")
    except Exception as e:
        print(e)
    finally:
        print('new picture: ' + new_pic)


main()