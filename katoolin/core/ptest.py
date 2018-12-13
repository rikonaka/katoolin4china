#!/usr/bin/env python3

import pstr
import os

pstr.plogo()

pstr.phelp()

if os.geteuid() != 0:
    print(os.geteuid())
    print "This program must be run as root. Aborting."