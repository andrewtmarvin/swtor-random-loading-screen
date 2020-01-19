# swtor-random-loading-screen

This is a simple script to randomly change the swtor loading screen each time the game is launched.

REQUIREMENTS

It goes without saying you need python3 installed on your machine for this to work. If python3 is accessible from the PATH (open command prompt and type 'python -V' to check), then you don't need to do anything. If it's not, add it to your PATH or change the batch file to point directly to your python3 executable instead of just calling python.

The online script uses a library called BeautifulSoup4. To install this, open command prompt and type "pip install beautifulsoup4" If you can't figure this part out, just stick with the local batch file. 

INSTALLATION

***Local images only***

Step 1

Place change_backgrounds.py in the swtor\retailclient\LoadingScreens\ directory

Step 2

Create a \jpgs\ directory inside the \LoadingScreens\ directory and place your custom background images there.

Step 3

Place local.bat in the swtor\retailclient\LoadingScreens\ directory

Step 4

Create a shortcut to local.bat on your desktop. 

Open the shortcut properties, click on advanced, and make sure it runs as administrator. 

Change the icon image to the SWTOR launcher icon

Done


***Online images only***

Step 1

Place change_backgrounds_alt.py in the swtor\retailclient\LoadingScreens\ directory

Step 2

Place online.bat in the swtor\retailclient\LoadingScreens\ directory

Step 3

Create a shortcut to online.bat on your desktop. 

Open the shortcut properties, click on advanced, and make sure it runs as administrator. 

Change the icon image to the SWTOR launcher icon

Done


***local and online iamges***

Step 1

Place both change_backgrounds.py and change_backgrounds_alt.py in the swtor\retailclient\LoadingScreens\ directory

Step 2

Create a \jpgs\ directory inside the \LoadingScreens\ directory and place your custom background images there.

Step 3

Place choice.bat in the swtor\retailclient\LoadingScreens\ directory

Step 4

Create a shortcut to online.bat on your desktop. 

Open the shortcut properties, click on advanced, and make sure it runs as administrator. 

Change the icon image to the SWTOR launcher icon

Done


NOTES

Bitraider overrides the loading screen image. Since I have it removed on my computer, everything works fine. If you don't want to remove Bitraider, I think this will still work if you call the programs in reverse order in the batch file (start SWTOR, then run script). If that doesn't work, just remove Bitraider.

If you're running into errors, open the batch file and change "EXIT" to "PAUSE" to see the error messages in command prompt


