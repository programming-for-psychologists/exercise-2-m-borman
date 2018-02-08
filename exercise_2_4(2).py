# -*- coding: utf-8 -*-
"""
Created on Mon Feb 05 20:13:16 2018

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
firstNameStim = visual.TextStim(win,text="", height=40, color="white",pos=[0,0])
while True:
    x=random.randint(0,1)
    firstNames = [name.split(' ')[x] for name in names]
    nameShown = random.choice(firstNames)
    firstNameStim.setText(nameShown)
    firstNameStim.draw()
    win.flip()
    if x==1:
        event.waitKeys(keyList=['l'])
        win.flip()
    if x==0:
#        print ("first name")
        event.waitKeys(keyList=['f'])
        win.flip()    
    win.flip()

    if event.getKeys(['q']):
        break