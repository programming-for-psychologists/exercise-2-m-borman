# -*- coding: utf-8 -*-
"""
Created on Wed Feb 07 23:28:07 2018

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


userVar = {'Name':'Enter your name'}
dlg = gui.DlgFromDict(userVar)

if userVar['Name'] in firstNames:
        print 'ok' #still prints ok, but also shows x

else:
    def popupError(text):
        errorDlg = gui.Dlg(title="Error", pos=(200,400))
        errorDlg.addText('Error: '+text, color='Red')
        errorDlg.show()

    popupError('Name does not exist')

timeLoaded = core.getTime() 
print timeLoaded   

while True:
    nameType = firstNames
    nameShown = random.choice(nameType)
    timer = core.clock()
    nameStim.setText(nameShown)
    nameStim.draw()
    win.flip()
    timer.reset(newT=0.0)
    response = event.waitKeys(maxWait=1)
    rt = event.waitKeys(timeStamped)
    print rt

    if userVar['Name'] == nameShown:
#        print 'nameshown is same as entered'
        correctAns = ['space']
    if userVar['Name'] != nameShown:
#        print 'not as entered'
        correctAns = None
#    if response == correctAns:
#        print 'it worked!'
    if response != correctAns:   
        stimIncorrect.draw()
        win.flip()
#        print 'it didn\'t work'
        core.wait(.5)
        
    if event.getKeys(['q']):
        break