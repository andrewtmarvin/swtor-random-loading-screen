@ECHO OFF
cls
:start
ECHO.
set choice=
set /p choice=Get loading screen image: online or local?
ECHO '%choice%'
if '%choice%' == '' goto local
if '%choice%' == 'online' goto online
if '%choice%' == 'local' goto local
ECHO '%choice%' not valid. Enter "online" or "local"
ECHO.
goto start

:online
START python "C:\Program Files (x86)\Electronic Arts\BioWare\Star Wars-The Old Republic\swtor\retailclient\LoadingScreens\change_backgrounds_alt.py"
goto end

:local
START python "C:\Program Files (x86)\Electronic Arts\BioWare\Star Wars-The Old Republic\swtor\retailclient\LoadingScreens\change_backgrounds.py"
goto end

:end
START "launcher.exe" "C:\Program Files (x86)\Electronic Arts\BioWare\Star Wars-The Old Republic\launcher.exe"
EXIT