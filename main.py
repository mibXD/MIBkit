#!usr/bin/python3

# Imports
import os
import sys
import time


# Banner
def Banner():
        print("""


     .        :   ::::::::::.
    ;;,.    ;;;  ;;; ;;;'';;'
    [[[[, ,[[[[, [[[ [[[__[[\.
    $$$$$$$$"$$$ $$$ $$----Y$$
    888 Y88" 888o888_88o,,od8P
    MMM  M'  "MMMMMM""YUMMMP"


          ToolKit v1.0""")

Banner()

# Import console
def main_console():


        run_console_command = f'python3 /data/data/com.termux/files/home/MIBkit/console.py'
        os.system(run_console_command)


main_console()
