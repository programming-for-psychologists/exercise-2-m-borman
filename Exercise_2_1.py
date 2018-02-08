# -*- coding: utf-8 -*-
"""
Created on Mon Feb 05 17:59:01 2018

@author: mzbor
"""

import time
import sys
import random
from psychopy import visual,event,core,gui

names = open('names.txt', 'r').readlines()
firstNames = [name.split(' ')[0] for name in names]

win = visual.Window([800,600],color="black", units='pix')
firstNameStim = visual.TextStim(win,text="", height=40, color="white",pos=[0,0])

while True:
    nameShown = random.choice(firstNames)
    fixCross = "+"
    firstNameStim.setText(fixCross)
    firstNameStim.draw()
    win.flip()
    core.wait(.5)
    win.flip()
    firstNameStim.setText(nameShown)
    firstNameStim.draw()
    win.flip()
    core.wait(.75)
    win.flip()
    core.wait(.15)
    
    if event.getKeys(['q']):
        break
 