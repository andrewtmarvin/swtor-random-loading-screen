# swtor-random-loading-screen

This is a simple script to randomly change the swtor loading screen each time the game is launched. See README for quick setup.

Installation

Step 1: Place change_backgrouns.py in the swtor\retailclient\LoadingScreens\ directory

Step 2: Create a \jpgs\ directory inside the \LoadingScreens\ directory and place your jpgs there.

Execution

I created a batch file to first run this script and then launch SWTOR. You could just run this script and then launch swtor manually, but then you'd have to remember to do that everytime. Just make a batch file and place a shortcut to it on your desktop.

Example batch file:

@ECHO OFF 
python "C:\Program Files (x86)\Electronic Arts\BioWare\Star Wars-The Old Republic\swtor\retailclient\LoadingScreens\change_backgrounds.py" 
"C:\Program Files (x86)\Electronic Arts\BioWare\Star Wars-The Old Republic\launcher.exe" 
EXIT

If you're running into errors, change "EXIT" to "PAUSE" to see the error messages.
