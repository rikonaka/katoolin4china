#!/usr/bin/env python3

import os
import sys
import traceback
import shutil

# Custom module here

from core import pstr
from core import core


def main():
    '''
    here is the main function
    '''

    try:
        # Init the apt sources.list
        core.init_apt()
        # Print logo
        pstr.plogo()
        # Into loop
        core.loop_1()
    except KeyboardInterrupt:
        print('Exit...Goodbye...')
        if os.path.exists('/etc/apt/sources.list.bak'):
            os.remove('/etc/apt/sources.list')
            shutil.copy('/etc/apt/sources.list.bak', '/etc/apt/sources.list')
            os.remove('/etc/apt/sources.list.bak')
            print(
                '\n\n\033[1;31m\nAll kali linux repositories have been deleted !\n\033[1;m')


if __name__ == "__main__":
    main()
