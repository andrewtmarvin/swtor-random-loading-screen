from os import path
from random import choice
from urllib import request
from bs4 import BeautifulSoup

def main():
    # Gets the directory that this script is stored in (should be placed in the LoadingScreens directory to work)
    dir_path = path.dirname(path.realpath(__file__))

    # Grabs a random HD image from getwallpapers.com
    try:
        page = BeautifulSoup(request.urlopen("http://getwallpapers.com/collection/swtor-wallpapers-1920x1080").read(),
                             features='html.parser')
        rand_ele = choice(page('div', attrs={'data-fullimg': True}))
        img_url = ("http://getwallpapers.com" + rand_ele['data-fullimg'])
        request.urlretrieve(img_url, dir_path + "/loadingscreen.jpg")
    except Exception as e:
        print('Failed to download image: ' + e.__str__())
        print('exiting')


main()
