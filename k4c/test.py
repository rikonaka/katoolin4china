#!/usr/bin/env python3

import interface
import os

interface.plogo()

interface.phelp()

if os.geteuid() != 0:
    print(os.geteuid())
    print("This program must be run as root. Aborting.")
