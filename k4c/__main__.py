#!/usr/bin/env python3

import os
import sys
import subprocess

# Custom module here

from . import interface
from . import function

r'''
 $$\   $$\             $$\                         $$\ $$\
 $$ | $$  |            $$ |                        $$ |\__|
 $$ |$$  /  $$$$$$\  $$$$$$\    $$$$$$\   $$$$$$\  $$ |$$\ $$$$$$$\
 $$$$$  /   \____$$\ \_$$  _|  $$  __$$\ $$  __$$\ $$ |$$ |$$  __$$\
 $$  $$<    $$$$$$$ |  Kali tools installer |  $$ |$$ |$$ |      $$ |
 $$ |\$$\  $$  __$$ |  $$ |$$\ $$ |  $$ |$$ |  $$ |$$ |$$ |$$ |  $$ |
 $$ | \$$\ \$$$$$$$ |  \$$$$  |\$$$$$$  |\$$$$$$  |$$ |$$ |$$ |  $$ |
 \__|  \__| \_______|   \____/  \______/  \______/ \__|\__|\__|  \__|


               $$\                          $$$$$$$\ $$\
              $$  |                        $$ ______|$$ |     $$\
             $$  /_           $$    $$\   $$ /       $$ \     \__|         $$$$$$$\
          $$$$$$$  | $$$$$$\  $$\ $$ /    $$ |       $$$$$$\  $$\ $$$$$$ \ \_____$$\
            $$  __/ $$    $$\ $$$$ _/     $$ \       $$\__$$\ $$ |$$\__$$ | $$$$$$$ |
            $$ |    $$    $$ |$$  /       \$$ \      $$ | $$ |$$ |$$ | $$ |$$    $$ |
            $$ |    \$$$$$$$ |$$ |         \$$$$$$$$\$$ | $$ |$$ |$$ | $$ |\$$$$$$$ |
            \__|     \_______|\__|          \_______|\__| \__|\__|\__|  \_| \_______|
'''


def main():
    '''
    here is the main function
    '''

    if os.geteuid() != 0:
        print('\033[1;31mThis program must be run as root! Aborting.\033[1;m\n')
        sys.exit(1)

    try:
        # Init the apt sources.list
        function.init_apt()
        # Print logo
        interface.plogo()
        # Into loop
        function.loop()
    except KeyboardInterrupt:
        print('\033[1;31m\nExit...Goodbye...\033[1;m')
        if os.path.exists('/etc/apt/sources.list.bak'):
            try:
                subprocess.check_call(
                    'rm -f /etc/apt/sources.list', shell=True)
            except subprocess.CalledProcessError as error_output:
                print('\033[1;31mRemove failed: {0}\033[1;m'.format(
                    error_output))

            try:
                subprocess.check_call(
                    'cp /etc/apt/sources.list.bak /etc/apt/sources.list', shell=True)
            except subprocess.CalledProcessError as error_output:
                print('\033[1;31mCopy failed: {0}\033[1;m'.format(
                    error_output))

            try:
                subprocess.check_call(
                    'rm -f /etc/apt/sources.list.bak', shell=True)
            except subprocess.CalledProcessError as error_output:
                print("\033[1;31mRemove failed: {0}\033[1;m".format(
                    error_output))

            print(
                '\n\n\033[1;31m\nAll Kali repositories have been deleted !\n\033[1;m')


if __name__ == "__main__":
    main()
