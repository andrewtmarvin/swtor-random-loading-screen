# swtor-random-loading-screen

This is a simple script to randomly change the swtor loading screen each time the game is launched.

INSTALLATION

Step 1

Place change_backgrounds.py in the swtor\retailclient\LoadingScreens\ directory

Step 2

Create a \jpgs\ directory inside the \LoadingScreens\ directory and place your custom background images there.

Step 3

Place change_backgrounds_alt.py in the swtor\retailclient\LoadingScreens\ directory

Step 4

Place one of the three batch files (choice.bat, local.bat, online.bat) in the swtor\retailclient\LoadingScreens\ directory

Local.bat changes the background image from local, then starts the game

Online.bat downloads a new background, then starts the game

Choice.bat prompts you for a choice each time, either online or local.

Step 5

Create a shortcut to the batch file on your desktop. 

Open the shortcut properties, click on advanced, and make sure it runs as administrator. 

Change the icon to SWTOR launcher icon.

If you're running into errors, open the batch fild and change "EXIT" to "PAUSE" to see the error messages.



REQUIREMENTS

It goes without saying you need python installed on your machine for this to work. If python is accessible from the PATH, then you don't need to do anything. If it's not, add it to your PATH or change the batch file to point directly to your python executable instead of just calling python.

The online script uses a library called BeautifulSoup4. To install this, open cmd and type "pip install beautifulsoup4" If you can't figure this part out, just stick with the local batch file. 
