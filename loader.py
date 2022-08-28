from subprocess import check_output
from time import sleep
import os
import pyinjector
import subprocess
import keyboard
import urllib.request
import requests

#path = "C:/Users/maxkr/Desktop/hake/ravo.dll"
path = "daddy.dll"
hwid = str(subprocess.check_output('wmic csproduct get uuid'), 'utf-8').split('\n')[1].strip()  # gets pc hwid

def cls(): print ("\n" * 696)

def check_hwid():
    hwid = str(subprocess.check_output('wmic csproduct get uuid'), 'utf-8').split('\n')[1].strip()  # gets pc hwid

    link = "https://raw.githubusercontent.com/MaxX132/hwid-loader/main/hwid"
    hwids = urllib.request.urlopen(link)
    for line in hwids:
        hwids = "b'" + str(subprocess.check_output('wmic csproduct get uuid'), 'utf-8').split('\n')[1].strip() + "'"
        lines = line.strip()
        if str(lines) == str(hwids):
            AccessGrant = 1
            break
        else:
            AccessGrant = 0
    if AccessGrant == 0:
        print("You are not authorised!")
        print("Your HWID: " + hwids)
        sleep(10)
        exit()

def get_dll():
    URL = "https://github.com/MaxX132/hwid-loader/raw/main/foreverlose%20(1).dll"
    dll = requests.get(URL)
    open(path, "wb").write(dll.content)
    sleep(1)
    try:
        csgo = int(input("Enter cs:go PID: "))
    except:
        print("Enter a number and try again!")
        sleep(1)
        exit()
    
    try:
        pyinjector.inject(csgo, path)
    except:
        os.remove(path)
        exit()
    print("Cheat injected!")
    os.remove(path)

def main():
    check_hwid()

    print("Welcome to HWID Loader")
    print("----------------------")
    print("   * 1 for Inject *   ")
    print("   * 2 for Exit   *   ")
    print("----------------------")
    print("   made by d0t#4007   ")

    while True:
        if keyboard.read_key() == "1":
            get_dll()
            sleep(1)
            exit()
        

        
        if keyboard.read_key() == "2":
            break

if __name__ == "__main__":
    main()