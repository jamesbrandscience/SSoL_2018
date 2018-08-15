#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.85.1),
    on Wed Aug 15 15:40:34 2018
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, gui, visual, core, data, event, logging, sound
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = u'Artificial_language_learning'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'/Users/jamesbrand/Desktop/SSoL_2018/ALL_experiment/Artificial_language_learning.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1280, 800], fullscr=False, screen=0,
    allowGUI=True, allowStencil=False,
    monitor='testMonitor', color='white', colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "instuctions"
instuctionsClock = core.Clock()
ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
instr1 = visual.TextStim(win=win, name='instr1',
    text=u'\ufeff\nWelcome to the planet Alpha-3-6a in a galaxy far, far away. We have encountered an intelligent alien life form with its own form of language. You must try to learn this language as best you can.\n\nDon\u2019t worry if you feel overwhelmed\u2014the alien knows that this is a difficult task for you to master, and it will do its best to understand everything that you say. \n\n\npress SPACE to continue.\n',
    font=u'Arial',
    pos=[0, 0], height=0.075, wrapWidth=1.8, ori=0, 
    color=u'black', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "instructions2"
instructions2Clock = core.Clock()
inst2 = visual.TextStim(win=win, name='inst2',
    text=u'\ufeff\nAs part of your training, you will see a series of pictures and the word the alien would use to describe those pictures. After being shown a picture and the word, you will be asked to retype the word you just saw.\u2028\n\nOnce your training is complete, the alien will test you on how well you have learnt the language, this will be done by only showing you the picture and you have to type in the word you think the alien uses to describe it.\n\n\npress SPACE to continue.',
    font=u'Arial',
    pos=(0, 0), height=0.075, wrapWidth=1.8, ori=0, 
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "train_display"
train_displayClock = core.Clock()
image_train1 = visual.ImageStim(
    win=win, name='image_train1',units='pix', 
    image='sin', mask=None,
    ori=0, pos=(0, 200), size=(300, 300),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
label_train1 = visual.TextStim(win=win, name='label_train1',
    text='default text',
    font=u'Arial',
    pos=(0, -0.2), height=0.1, wrapWidth=None, ori=0, 
    color=u'black', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "train_input"
train_inputClock = core.Clock()
inputText = ""
retype1 = visual.TextStim(win=win, name='retype1',
    text='default text',
    font=u'Arial',
    pos=[-0.1, -0.2], height=0.1, wrapWidth=None, ori=0, 
    color=u'black', colorSpace='rgb', opacity=1,
    depth=-1.0);
instr3 = visual.TextStim(win=win, name='instr3',
    text=u'Please retype the word you just saw and press ENTER',
    font=u'Arial',
    pos=(0, 0.4), height=0.075, wrapWidth=1.8, ori=0, 
    color=u'black', colorSpace='rgb', opacity=1,
    depth=-3.0);

# Initialize components for Routine "fixation1"
fixation1Clock = core.Clock()
fix1 = visual.TextStim(win=win, name='fix1',
    text=None,
    font=u'Arial',
    pos=(0, -0.2), height=0.1, wrapWidth=None, ori=0, 
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "test_instructions"
test_instructionsClock = core.Clock()
instr4 = visual.TextStim(win=win, name='instr4',
    text=u'You will now only be shown the image and your task is to type the word you think went with that image.\n\nAlways type a word you think could be part of the language, never leave it blank.\n\nPress SPACE to continue',
    font=u'Arial',
    pos=(0, 0), height=0.075, wrapWidth=1.8, ori=0, 
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "test_input"
test_inputClock = core.Clock()
testText = ""
retype_test = visual.TextStim(win=win, name='retype_test',
    text='default text',
    font=u'Arial',
    pos=[-0.1, -0.2], height=0.1, wrapWidth=None, ori=0, 
    color=u'black', colorSpace='rgb', opacity=1,
    depth=-1.0);
img_test1 = visual.ImageStim(
    win=win, name='img_test1',units='pix', 
    image='sin', mask=None,
    ori=0, pos=(0, 200), size=(300, 300),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
text = visual.TextStim(win=win, name='text',
    text=u'Type the word you think described this image',
    font=u'Arial',
    pos=(0, -0.5), height=0.075, wrapWidth=1.8, ori=0, 
    color=u'black', colorSpace='rgb', opacity=1,
    depth=-4.0);

# Initialize components for Routine "fixation1"
fixation1Clock = core.Clock()
fix1 = visual.TextStim(win=win, name='fix1',
    text=None,
    font=u'Arial',
    pos=(0, -0.2), height=0.1, wrapWidth=None, ori=0, 
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "end"
endClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text=u'Check the results file in the data sub folder',
    font=u'Arial',
    pos=[0, 0], height=0.075, wrapWidth=1.8, ori=0, 
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instuctions"-------
t = 0
instuctionsClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
cont1 = event.BuilderKeyResponse()
# keep track of which components have finished
instuctionsComponents = [ISI, instr1, cont1]
for thisComponent in instuctionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instuctions"-------
while continueRoutine:
    # get current time
    t = instuctionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr1* updates
    if t >= 0.0 and instr1.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr1.tStart = t
        instr1.frameNStart = frameN  # exact frame index
        instr1.setAutoDraw(True)
    
    # *cont1* updates
    if t >= 0.0 and cont1.status == NOT_STARTED:
        # keep track of start time/frame for later
        cont1.tStart = t
        cont1.frameNStart = frameN  # exact frame index
        cont1.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if cont1.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    # *ISI* period
    if t >= 0.0 and ISI.status == NOT_STARTED:
        # keep track of start time/frame for later
        ISI.tStart = t
        ISI.frameNStart = frameN  # exact frame index
        ISI.start(0.5)
    elif ISI.status == STARTED:  # one frame should pass before updating params and completing
        ISI.complete()  # finish the static period
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instuctionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instuctions"-------
for thisComponent in instuctionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instuctions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instructions2"-------
t = 0
instructions2Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
cont2 = event.BuilderKeyResponse()
# keep track of which components have finished
instructions2Components = [inst2, cont2]
for thisComponent in instructions2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instructions2"-------
while continueRoutine:
    # get current time
    t = instructions2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *inst2* updates
    if t >= 0.0 and inst2.status == NOT_STARTED:
        # keep track of start time/frame for later
        inst2.tStart = t
        inst2.frameNStart = frameN  # exact frame index
        inst2.setAutoDraw(True)
    
    # *cont2* updates
    if t >= 0.0 and cont2.status == NOT_STARTED:
        # keep track of start time/frame for later
        cont2.tStart = t
        cont2.frameNStart = frameN  # exact frame index
        cont2.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if cont2.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions2"-------
for thisComponent in instructions2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instructions2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=2, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(u'Train/Trials_list.csv'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    # ------Prepare to start Routine "train_display"-------
    t = 0
    train_displayClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(4.500000)
    # update component parameters for each repeat
    image_train1.setImage(img_train)
    label_train1.setText(label1)
    # keep track of which components have finished
    train_displayComponents = [image_train1, label_train1]
    for thisComponent in train_displayComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "train_display"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = train_displayClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_train1* updates
        if t >= 0.0 and image_train1.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_train1.tStart = t
            image_train1.frameNStart = frameN  # exact frame index
            image_train1.setAutoDraw(True)
        frameRemains = 0.0 + 4.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image_train1.status == STARTED and t >= frameRemains:
            image_train1.setAutoDraw(False)
        
        # *label_train1* updates
        if t >= 1.5 and label_train1.status == NOT_STARTED:
            # keep track of start time/frame for later
            label_train1.tStart = t
            label_train1.frameNStart = frameN  # exact frame index
            label_train1.setAutoDraw(True)
        frameRemains = 1.5 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
        if label_train1.status == STARTED and t >= frameRemains:
            label_train1.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in train_displayComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "train_display"-------
    for thisComponent in train_displayComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "train_input"-------
    t = 0
    train_inputClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    theseKeys=""
    shift_flag = False
    retype1.alignHoriz ='left'
    key_resp_3 = event.BuilderKeyResponse()
    # keep track of which components have finished
    train_inputComponents = [retype1, key_resp_3, instr3]
    for thisComponent in train_inputComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "train_input"-------
    while continueRoutine:
        # get current time
        t = train_inputClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        n= len(theseKeys)
        i = 0
        while i < n:
        
            if theseKeys[i] == 'return':
                # pressing RETURN means time to stop
                continueRoutine = False
                break
        
            elif theseKeys[i] == 'backspace':
                inputText = inputText[:-1]  # lose the final character
                i = i + 1
        
            elif theseKeys[i] == 'space':
                inputText += ' '
                i = i + 1
        
            elif theseKeys[i] in ['lshift', 'rshift']:
                shift_flag = True
                i = i + 1
        
            else:
                if len(theseKeys[i]) == 1:
                    # we only have 1 char so should be a normal key, 
                    # otherwise it might be 'ctrl' or similar so ignore it
                    if shift_flag:
                        inputText += chr( ord(theseKeys[i]) - ord(' '))
                        shift_flag = False
                    else:
                        inputText += theseKeys[i]
        
                i = i + 1
        
        
        
        
        
        
        # *retype1* updates
        if t >= 0.0 and retype1.status == NOT_STARTED:
            # keep track of start time/frame for later
            retype1.tStart = t
            retype1.frameNStart = frameN  # exact frame index
            retype1.setAutoDraw(True)
        if retype1.status == STARTED:  # only update if drawing
            retype1.setText((inputText), log=False)
        
        # *key_resp_3* updates
        if t >= 0.0 and key_resp_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_3.tStart = t
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if key_resp_3.status == STARTED:
            theseKeys = event.getKeys()
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
        
        # *instr3* updates
        if t >= 0.0 and instr3.status == NOT_STARTED:
            # keep track of start time/frame for later
            instr3.tStart = t
            instr3.frameNStart = frameN  # exact frame index
            instr3.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in train_inputComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "train_input"-------
    for thisComponent in train_inputComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # let's store the final text string into the results finle...
    thisExp.addData('inputText', inputText)
    inputText=""
    # the Routine "train_input" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "fixation1"-------
    t = 0
    fixation1Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fixation1Components = [fix1]
    for thisComponent in fixation1Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "fixation1"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fixation1Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix1* updates
        if t >= 0.0 and fix1.status == NOT_STARTED:
            # keep track of start time/frame for later
            fix1.tStart = t
            fix1.frameNStart = frameN  # exact frame index
            fix1.setAutoDraw(True)
        frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fix1.status == STARTED and t >= frameRemains:
            fix1.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixation1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fixation1"-------
    for thisComponent in fixation1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed 2 repeats of 'trials'


# ------Prepare to start Routine "test_instructions"-------
t = 0
test_instructionsClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
cont3 = event.BuilderKeyResponse()
# keep track of which components have finished
test_instructionsComponents = [instr4, cont3]
for thisComponent in test_instructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "test_instructions"-------
while continueRoutine:
    # get current time
    t = test_instructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr4* updates
    if t >= 0.0 and instr4.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr4.tStart = t
        instr4.frameNStart = frameN  # exact frame index
        instr4.setAutoDraw(True)
    
    # *cont3* updates
    if t >= 0.0 and cont3.status == NOT_STARTED:
        # keep track of start time/frame for later
        cont3.tStart = t
        cont3.frameNStart = frameN  # exact frame index
        cont3.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if cont3.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in test_instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "test_instructions"-------
for thisComponent in test_instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "test_instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(u'Train/Test_list.csv'),
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2.keys():
        exec(paramName + '= thisTrial_2.' + paramName)

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2.keys():
            exec(paramName + '= thisTrial_2.' + paramName)
    
    # ------Prepare to start Routine "test_input"-------
    t = 0
    test_inputClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    theseKeys=""
    shift_flag = False
    retype_test.alignHoriz ='left'
    img_test1.setImage(img_test)
    key_resp_6 = event.BuilderKeyResponse()
    # keep track of which components have finished
    test_inputComponents = [retype_test, img_test1, key_resp_6, text]
    for thisComponent in test_inputComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "test_input"-------
    while continueRoutine:
        # get current time
        t = test_inputClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        n= len(theseKeys)
        i = 0
        while i < n:
        
            if theseKeys[i] == 'return':
                # pressing RETURN means time to stop
                continueRoutine = False
                break
        
            elif theseKeys[i] == 'backspace':
                testText = testText[:-1]  # lose the final character
                i = i + 1
        
            elif theseKeys[i] == 'space':
                testText += ' '
                i = i + 1
        
            elif theseKeys[i] in ['lshift', 'rshift']:
                shift_flag = True
                i = i + 1
        
            else:
                if len(theseKeys[i]) == 1:
                    # we only have 1 char so should be a normal key, 
                    # otherwise it might be 'ctrl' or similar so ignore it
                    if shift_flag:
                        testText += chr( ord(theseKeys[i]) - ord(' '))
                        shift_flag = False
                    else:
                        testText += theseKeys[i]
        
                i = i + 1
        
        
        
        
        
        # *retype_test* updates
        if t >= 0.0 and retype_test.status == NOT_STARTED:
            # keep track of start time/frame for later
            retype_test.tStart = t
            retype_test.frameNStart = frameN  # exact frame index
            retype_test.setAutoDraw(True)
        if retype_test.status == STARTED:  # only update if drawing
            retype_test.setText((testText), log=False)
        
        # *img_test1* updates
        if t >= 0.0 and img_test1.status == NOT_STARTED:
            # keep track of start time/frame for later
            img_test1.tStart = t
            img_test1.frameNStart = frameN  # exact frame index
            img_test1.setAutoDraw(True)
        
        # *key_resp_6* updates
        if t >= 0.0 and key_resp_6.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_6.tStart = t
            key_resp_6.frameNStart = frameN  # exact frame index
            key_resp_6.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if key_resp_6.status == STARTED:
            theseKeys = event.getKeys()
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
        
        # *text* updates
        if t >= 0.0 and text.status == NOT_STARTED:
            # keep track of start time/frame for later
            text.tStart = t
            text.frameNStart = frameN  # exact frame index
            text.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in test_inputComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "test_input"-------
    for thisComponent in test_inputComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # let's store the final text string into the results finle...
    thisExp.addData('testText', testText)
    testText=""
    # the Routine "test_input" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "fixation1"-------
    t = 0
    fixation1Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fixation1Components = [fix1]
    for thisComponent in fixation1Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "fixation1"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fixation1Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix1* updates
        if t >= 0.0 and fix1.status == NOT_STARTED:
            # keep track of start time/frame for later
            fix1.tStart = t
            fix1.frameNStart = frameN  # exact frame index
            fix1.setAutoDraw(True)
        frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fix1.status == STARTED and t >= frameRemains:
            fix1.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixation1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fixation1"-------
    for thisComponent in fixation1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_2'


# ------Prepare to start Routine "end"-------
t = 0
endClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_4 = event.BuilderKeyResponse()
# keep track of which components have finished
endComponents = [text_2, key_resp_4]
for thisComponent in endComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "end"-------
while continueRoutine:
    # get current time
    t = endClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if t >= 0.0 and text_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_2.tStart = t
        text_2.frameNStart = frameN  # exact frame index
        text_2.setAutoDraw(True)
    
    # *key_resp_4* updates
    if t >= 0.0 and key_resp_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_4.tStart = t
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_4.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_4.keys = theseKeys[-1]  # just the last key pressed
            key_resp_4.rt = key_resp_4.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_4.keys in ['', [], None]:  # No response was made
    key_resp_4.keys=None
thisExp.addData('key_resp_4.keys',key_resp_4.keys)
if key_resp_4.keys != None:  # we had a response
    thisExp.addData('key_resp_4.rt', key_resp_4.rt)
thisExp.nextEntry()
# the Routine "end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()


# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
