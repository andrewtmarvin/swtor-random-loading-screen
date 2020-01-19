from os import path, listdir, remove
from shutil import copy2
from random import choice


def main():
    # Gets the directory that this script is stored in (should be placed in the LoadingScreens directory to work)
    dir_path = path.dirname(path.realpath(__file__))

    # Grabs a random picture from jpgs subdirectory
    new_pic = choice(listdir(dir_path + "/jpgs"))

    # Deletes the old background image
    try:
        remove(dir_path + "/loadingscreen.jpg")
    except(FileNotFoundError, IOError):
        print('Deletion failed because loading screen picture file was not found.')

    # Copies and renames the randomly chosen pic to the correct location
    try:
        copy2(dir_path + "/jpgs/" + new_pic, dir_path + "/loadingscreen.jpg")
    except Exception as e:
        print(e)
    finally:
        print('new picture: ' + new_pic)


main()
