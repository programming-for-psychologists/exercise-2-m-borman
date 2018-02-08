# -*- coding: utf-8 -*-
"""
Created on Mon Feb 05 18:50:42 2018

@author: mzbor
"""

import time
import sys
import random
from psychopy import visual,event,core,gui


names = open('names.txt', 'r').readlines()
firstNames = [name.split(' ')[1] for name in names]
lastNames = [name.split(' ')[0] for name in names]
firstLast = (firstNames, lastNames)


"""
the two line above are a more compact way of writing: 
names = open('names.txt', 'r').readlines()
firstNames=[]
for name in names:
    firstNames.append(name.split(' ')[0])
"""	

win = visual.Window([800,600],color="black", units='pix')
firstNameStim = visual.TextStim(win,text="", height=40, color="white",pos=[0,0])

while True:
    nameType = random.choice(firstLast)
    nameShown = random.choice(nameType)
    firstNameStim.setText(nameShown)
    firstNameStim.draw()
    win.flip()
    core.wait(.75)
    win.flip()
    core.wait(.15)

    if event.getKeys(['q']):
        break