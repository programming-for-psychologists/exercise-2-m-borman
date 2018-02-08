# -*- coding: utf-8 -*-
"""
Created on Wed Feb 07 16:42:26 2018

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


userVar = {'Name':'Enter your name'}
dlg = gui.DlgFromDict(userVar)

if userVar['Name'] in firstNames:
        print 'ok'

else:
    def popupError(text):
        errorDlg = gui.Dlg(title="Error", pos=(200,400))
        errorDlg.addText('Error: '+text, color='Red')
        errorDlg.show()

    popupError('Name does not exist')

if event.getKeys(['q']):
    break
