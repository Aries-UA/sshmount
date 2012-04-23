#!/usr/bin/env python
#-*- coding: utf-8 -*-

from glob import glob
from py2deb import Py2deb

version = "0.1"

p = Py2deb("sshmount")
p.author = "Aries"
p.mail = "aries.ua@gmail.com"
p.description = "Монтирование удаленных разделов по SSH"
p.url = "http://vkontakte.ru/ariesua"
p.depends = "python, python-qt4, pyqt-tools, sshfs"
p.license = "gpl"
p.section = "utils"
p.arch  = "all"

p[""] = ["sshmount.py|sshmount.py",
																				"connector/__init__.py", "connector/connector.py",
																				"images/gnome-fs-ssh.png", "images/images.qrc",
																				"forms/__init__.py", "forms/basewin.py", "forms/editform.py",
																				"forms/edititem.py", "forms/images_rc.py", "forms/listconnection.py",
																				"forms/messagebox.py", "forms/pwdform.py", "forms/pwditem.py",
																				"forms/treelist.py"]

p.generate(version)
