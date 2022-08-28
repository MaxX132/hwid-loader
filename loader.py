from subprocess import check_output
from time import sleep
import pyinjector
import subprocess
import keyboard
import urllib.request
import requests

path = "daddy.dll"
hwid = str(subprocess.check_output('wmic csproduct get uuid'), 'utf-8').split('\n')[1].strip()  # gets pc hwid

def cls(): print ("\n" * 696)

def check_hwid():
    hwid = str(subprocess.check_output('wmic csproduct get uuid'), 'utf-8').split('\n')[1].strip()  # gets pc hwid

    link = "https://raw.githubusercontent.com/MaxX132/hwid-loader/main/hwid"
    hwids = urllib.request.urlopen(link)       # gets HWID list
    for line in hwids:
        hwids = "b'" + str(subprocess.check_output('wmic csproduct get uuid'), 'utf-8').split('\n')[1].strip() + "'"
        lines = line.strip()
        if str(lines) == str(hwids): # if pc hwid is on hwid list it grants access
            AccessGrant = 1
            break
        else:
            AccessGrant = 0 # if pc hwid is not on hwid list it wont grant access
    if AccessGrant == 0:
        print("You are not authorised!")
        print("Your HWID: " + hwids)
        sleep(10)
        exit()

def get_dll():
    print("Please Wait...")
    URL = "https://github.com/MaxX132/hwid-loader/raw/main/foreverlose%20(1).dll"
    dll = requests.get(URL)
    open(path, "wb").write(dll.content)    # dowloads dll
    sleep(1)
    try:
        csgo = int(input("Enter cs:go PID: "))   # gets pid
    except:
        print("Enter a number and try again!")
        sleep(1)
        exit()
    
    try:
        pyinjector.inject(csgo, path)    # dll injection
    except:
        exit()
    print("Cheat injected!")


def main():
    check_hwid()

    print("Welcome to HWID Loader")
    print("----------------------")        # sum text
    print("   * 1 for Inject *   ")
    print("   * 2 for Exit   *   ")
    print("----------------------")
    print("   made by d0t#4007   ")

    while True:
        if keyboard.read_key() == "1": 
            get_dll()
            sleep(1)
            exit()
        
                                            # selection
        
        if keyboard.read_key() == "2":
            break

if __name__ == "__main__":
    main()