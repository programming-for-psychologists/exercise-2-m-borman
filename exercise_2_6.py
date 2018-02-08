# -*- coding: utf-8 -*-
"""
Created on Wed Feb 07 13:04:57 2018

@author: mzbor
"""

import time
import sys
import random
from psychopy import visual,event,core,gui

names = open('names.txt', 'r').readlines()


"""
the two line above are a more compact way of writing: 
names = open('names.txt', 'r').readlines()
firstNames=[]
for name in names:
    firstNames.append(name.split(' ')[0])
"""	

win = visual.Window([800,600],color="black", units='pix')
nameStim = visual.TextStim(win,text="", height=40, color="white",pos=[0,0])
stimCorrect = visual.TextStim(win,text="O", height=40, color="green",pos=[0,0])
stimIncorrect = visual.TextStim(win,text="X", height=40, color="red",pos=[0,0])
firstNames = [name.split(' ')[0] for name in names]
lastNames = [name.split(' ')[1] for name in names]
firstLast = (firstNames, lastNames)


while True:
    nameType = random.choice(firstLast)
    nameShown = random.choice(nameType)
    nameStim.setText(nameShown)
    nameStim.draw()
    win.flip()
    response = event.waitKeys(maxWait=1)
    if nameShown in firstNames:
        correctAns = ['f']
    if nameShown in lastNames:
        correctAns = ['l']
    if response == correctAns:
            stimCorrect.draw()
            win.flip()
            core.wait(.5)
    else:
            stimIncorrect.draw()
            win.flip()
            core.wait(.5)
        
    if event.getKeys(['q']):
        break