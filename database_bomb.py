#!/usr/bin/python
# -*- coding: utf-8 -*-

from DBomberClass import *
import sys

"""
Copyright (c) 2015 Spade Team - Sk1M4x (http://github.com/sk1m4x/)
www.github.com/sk1m4x/DatabaseBomb/

WARNING! Read it!
➤ If you do not have minimum knowledge of Python, it is highly recommended not to change any line of this code!

Thank you, Spade Team Developers. ♠
"""

try:
	Execute().connect(sys.argv[1], int(sys.argv[2]))

except IndexError:
	print "\033[1;31mVocê digitou incorretamente. Corrija-se:"
	print "\033[0;31m$ python %s <target> <bots>\033[0m" % sys.argv[0]
