# -*- coding: utf-8 -*-
"""
Created on Mon Feb 05 18:45:17 2018

@author: mzbor
"""

import time
import sys
import random
from psychopy import visual,event,core,gui


names = open('names.txt', 'r').readlines()
lastNames = [name.split(' ')[randint(0,1)] for name in names]


win = visual.Window([800,600],color="black", units='pix')
lastNameStim = visual.TextStim(win,text="", height=40, color="white",pos=[0,0])

while True:
    nameShown = random.choice(lastNames)
    lastNameStim.setText(nameShown)
    lastNameStim.draw()
    win.flip()
    core.wait(.75)
    win.flip()
    core.wait(.15)

    if event.getKeys(['q']):
        break