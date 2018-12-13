#!/usr/bin/env python3

import os
import sys
import subprocess

# Custom module here

from core import pstr
from core import function


def main():
    '''
    here is the main function
    '''

    if os.geteuid() != 0:
        print('\033[1;31mThis program must be run as root! Aborting.\033[1;m')
        sys.exit(1)

    try:
        # Init the apt sources.list
        function.init_apt()
        # Print logo
        pstr.plogo()
        # Into loop
        function.loop_1()
    except KeyboardInterrupt:
        print('\033[1;31mExit...Goodbye...\033[1;m')
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
                '\n\n\033[1;31m\nAll kali linux repositories have been deleted !\n\033[1;m')


if __name__ == "__main__":
    main()
