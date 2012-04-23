#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os

commands = ("pyuic4 -o treelist.py treelist.ui",
						"pyuic4 -o edititem.py edititem.ui",
						"pyuic4 -o pwditem.py pwditem.ui",
						"pyrcc4 -o images_rc.py ../images/images.qrc")

for command in commands:
	print command
	os.system(command)
