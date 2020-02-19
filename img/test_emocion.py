#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.1.5),
    on febrero 09, 2020, at 00:56
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.1.5'
expName = 'test_emocion'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Diego Ramírez\\Desktop\\emociones\\test_emocion.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1366, 768], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[-1.000,-1.000,-1.000], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
c_alegria = visual.Rect(
    win=win, name='c_alegria',
    width=(0.32, 0.125)[0], height=(0.32, 0.125)[1],
    ori=0, pos=(-.6, -.2),
    lineWidth=2, lineColor=[1.000,1.000,1.000], lineColorSpace='rgb',
    fillColor=[-1.000,-1.000,-1.000], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
t_alegria = visual.TextStim(win=win, name='t_alegria',
    text='Alegría',
    font='Arial',
    pos=(-.6, -.2), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
c_tristeza = visual.Rect(
    win=win, name='c_tristeza',
    width=(0.32, 0.125)[0], height=(0.32, 0.125)[1],
    ori=0, pos=(-.6, -.38),
    lineWidth=2, lineColor=[1.000,1.000,1.000], lineColorSpace='rgb',
    fillColor=[-1.000,-1.000,-1.000], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
t_tristeza = visual.TextStim(win=win, name='t_tristeza',
    text='Tristeza',
    font='Arial',
    pos=(-.6, -.38), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
c_enojo = visual.Rect(
    win=win, name='c_enojo',
    width=(0.32, 0.125)[0], height=(0.32, 0.125)[1],
    ori=0, pos=(-.2, -.2),
    lineWidth=2, lineColor=[1.000,1.000,1.000], lineColorSpace='rgb',
    fillColor=[-1.000,-1.000,-1.000], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
t_enojo = visual.TextStim(win=win, name='t_enojo',
    text='Enojo',
    font='Arial',
    pos=(-.2, -.2), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
c_asco = visual.Rect(
    win=win, name='c_asco',
    width=(0.32, 0.125)[0], height=(0.32, 0.125)[1],
    ori=0, pos=(-.2, -.38),
    lineWidth=2, lineColor=[1.000,1.000,1.000], lineColorSpace='rgb',
    fillColor=[-1.000,-1.000,-1.000], fillColorSpace='rgb',
    opacity=1, depth=-6.0, interpolate=True)
t_asco = visual.TextStim(win=win, name='t_asco',
    text='Asco',
    font='Arial',
    pos=(-.2, -.38), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
c_miedo = visual.Rect(
    win=win, name='c_miedo',
    width=(0.32, 0.125)[0], height=(0.32, 0.125)[1],
    ori=0, pos=(.2, -.2),
    lineWidth=2, lineColor=[1.000,1.000,1.000], lineColorSpace='rgb',
    fillColor=[-1.000,-1.000,-1.000], fillColorSpace='rgb',
    opacity=1, depth=-8.0, interpolate=True)
t_miedo = visual.TextStim(win=win, name='t_miedo',
    text='Miedo',
    font='Arial',
    pos=(.2, -.2), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
c_sorpresa = visual.Rect(
    win=win, name='c_sorpresa',
    width=(0.32, 0.125)[0], height=(0.32, 0.125)[1],
    ori=0, pos=(.2, -.38),
    lineWidth=2, lineColor=[1.000,1.000,1.000], lineColorSpace='rgb',
    fillColor=[-1.000,-1.000,-1.000], fillColorSpace='rgb',
    opacity=1, depth=-10.0, interpolate=True)
t_sorpresa = visual.TextStim(win=win, name='t_sorpresa',
    text='Sorpresa',
    font='Arial',
    pos=(.2, -.38), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-11.0);
c_neutral = visual.Rect(
    win=win, name='c_neutral',
    width=(0.32, 0.125)[0], height=(0.32, 0.125)[1],
    ori=0, pos=(.6, -.2),
    lineWidth=2, lineColor=[1.000,1.000,1.000], lineColorSpace='rgb',
    fillColor=[-1.000,-1.000,-1.000], fillColorSpace='rgb',
    opacity=1, depth=-12.0, interpolate=True)
t_neutral = visual.TextStim(win=win, name='t_neutral',
    text='Neutral',
    font='Arial',
    pos=(.6, -.2), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-13.0);
c_calma = visual.Rect(
    win=win, name='c_calma',
    width=(0.32, 0.125)[0], height=(0.32, 0.125)[1],
    ori=0, pos=(.6, -.38),
    lineWidth=2, lineColor=[1.000,1.000,1.000], lineColorSpace='rgb',
    fillColor=[-1.000,-1.000,-1.000], fillColorSpace='rgb',
    opacity=1, depth=-14.0, interpolate=True)
t_calma = visual.TextStim(win=win, name='t_calma',
    text='Calma',
    font='Arial',
    pos=(.6, -.38), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-15.0);
rostro = visual.ImageStim(
    win=win,
    name='rostro', 
    image='./HM02_FO', mask=None,
    ori=0, pos=(0, .2), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-16.0)
c_ninguna = visual.Rect(
    win=win, name='c_ninguna',
    width=(0.32, 0.125)[0], height=(0.32, 0.125)[1],
    ori=0, pos=(.6, 0),
    lineWidth=2, lineColor=[1.000,1.000,1.000], lineColorSpace='rgb',
    fillColor=[-1.000,-1.000,-1.000], fillColorSpace='rgb',
    opacity=1, depth=-12.0, interpolate=True)
t_ninguna = visual.TextStim(win=win, name='t_ninguna',
    text='Ninguna\nOpción',
    font='Arial',
    pos=(.6, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-13.0);
pregunta = visual.TextStim(win=win, name='pregunta',
    text='¿Qué emoción \nmuestra\neste rostro?',
    font='Arial',
    pos=(-.6, 0), height=0.05, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-19.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "trial"-------
t = 0
trialClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
trialComponents = [c_alegria, t_alegria, c_tristeza, t_tristeza, c_enojo, t_enojo, c_asco, t_asco, c_miedo, t_miedo, c_sorpresa, t_sorpresa, c_neutral, t_neutral, c_calma, t_calma, rostro, c_ninguna, t_ninguna, pregunta]
for thisComponent in trialComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "trial"-------
while continueRoutine:
    # get current time
    t = trialClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *c_alegria* updates
    if t >= 0.0 and c_alegria.status == NOT_STARTED:
        # keep track of start time/frame for later
        c_alegria.tStart = t  # not accounting for scr refresh
        c_alegria.frameNStart = frameN  # exact frame index
        win.timeOnFlip(c_alegria, 'tStartRefresh')  # time at next scr refresh
        c_alegria.setAutoDraw(True)
    
    # *t_alegria* updates
    if t >= 0.0 and t_alegria.status == NOT_STARTED:
        # keep track of start time/frame for later
        t_alegria.tStart = t  # not accounting for scr refresh
        t_alegria.frameNStart = frameN  # exact frame index
        win.timeOnFlip(t_alegria, 'tStartRefresh')  # time at next scr refresh
        t_alegria.setAutoDraw(True)
    
    # *c_tristeza* updates
    if t >= 0.0 and c_tristeza.status == NOT_STARTED:
        # keep track of start time/frame for later
        c_tristeza.tStart = t  # not accounting for scr refresh
        c_tristeza.frameNStart = frameN  # exact frame index
        win.timeOnFlip(c_tristeza, 'tStartRefresh')  # time at next scr refresh
        c_tristeza.setAutoDraw(True)
    
    # *t_tristeza* updates
    if t >= 0.0 and t_tristeza.status == NOT_STARTED:
        # keep track of start time/frame for later
        t_tristeza.tStart = t  # not accounting for scr refresh
        t_tristeza.frameNStart = frameN  # exact frame index
        win.timeOnFlip(t_tristeza, 'tStartRefresh')  # time at next scr refresh
        t_tristeza.setAutoDraw(True)
    
    # *c_enojo* updates
    if t >= 0.0 and c_enojo.status == NOT_STARTED:
        # keep track of start time/frame for later
        c_enojo.tStart = t  # not accounting for scr refresh
        c_enojo.frameNStart = frameN  # exact frame index
        win.timeOnFlip(c_enojo, 'tStartRefresh')  # time at next scr refresh
        c_enojo.setAutoDraw(True)
    
    # *t_enojo* updates
    if t >= 0.0 and t_enojo.status == NOT_STARTED:
        # keep track of start time/frame for later
        t_enojo.tStart = t  # not accounting for scr refresh
        t_enojo.frameNStart = frameN  # exact frame index
        win.timeOnFlip(t_enojo, 'tStartRefresh')  # time at next scr refresh
        t_enojo.setAutoDraw(True)
    
    # *c_asco* updates
    if t >= 0.0 and c_asco.status == NOT_STARTED:
        # keep track of start time/frame for later
        c_asco.tStart = t  # not accounting for scr refresh
        c_asco.frameNStart = frameN  # exact frame index
        win.timeOnFlip(c_asco, 'tStartRefresh')  # time at next scr refresh
        c_asco.setAutoDraw(True)
    
    # *t_asco* updates
    if t >= 0.0 and t_asco.status == NOT_STARTED:
        # keep track of start time/frame for later
        t_asco.tStart = t  # not accounting for scr refresh
        t_asco.frameNStart = frameN  # exact frame index
        win.timeOnFlip(t_asco, 'tStartRefresh')  # time at next scr refresh
        t_asco.setAutoDraw(True)
    
    # *c_miedo* updates
    if t >= 0.0 and c_miedo.status == NOT_STARTED:
        # keep track of start time/frame for later
        c_miedo.tStart = t  # not accounting for scr refresh
        c_miedo.frameNStart = frameN  # exact frame index
        win.timeOnFlip(c_miedo, 'tStartRefresh')  # time at next scr refresh
        c_miedo.setAutoDraw(True)
    
    # *t_miedo* updates
    if t >= 0.0 and t_miedo.status == NOT_STARTED:
        # keep track of start time/frame for later
        t_miedo.tStart = t  # not accounting for scr refresh
        t_miedo.frameNStart = frameN  # exact frame index
        win.timeOnFlip(t_miedo, 'tStartRefresh')  # time at next scr refresh
        t_miedo.setAutoDraw(True)
    
    # *c_sorpresa* updates
    if t >= 0.0 and c_sorpresa.status == NOT_STARTED:
        # keep track of start time/frame for later
        c_sorpresa.tStart = t  # not accounting for scr refresh
        c_sorpresa.frameNStart = frameN  # exact frame index
        win.timeOnFlip(c_sorpresa, 'tStartRefresh')  # time at next scr refresh
        c_sorpresa.setAutoDraw(True)
    
    # *t_sorpresa* updates
    if t >= 0.0 and t_sorpresa.status == NOT_STARTED:
        # keep track of start time/frame for later
        t_sorpresa.tStart = t  # not accounting for scr refresh
        t_sorpresa.frameNStart = frameN  # exact frame index
        win.timeOnFlip(t_sorpresa, 'tStartRefresh')  # time at next scr refresh
        t_sorpresa.setAutoDraw(True)
    
    # *c_neutral* updates
    if t >= 0.0 and c_neutral.status == NOT_STARTED:
        # keep track of start time/frame for later
        c_neutral.tStart = t  # not accounting for scr refresh
        c_neutral.frameNStart = frameN  # exact frame index
        win.timeOnFlip(c_neutral, 'tStartRefresh')  # time at next scr refresh
        c_neutral.setAutoDraw(True)
    
    # *t_neutral* updates
    if t >= 0.0 and t_neutral.status == NOT_STARTED:
        # keep track of start time/frame for later
        t_neutral.tStart = t  # not accounting for scr refresh
        t_neutral.frameNStart = frameN  # exact frame index
        win.timeOnFlip(t_neutral, 'tStartRefresh')  # time at next scr refresh
        t_neutral.setAutoDraw(True)
    
    # *c_calma* updates
    if t >= 0.0 and c_calma.status == NOT_STARTED:
        # keep track of start time/frame for later
        c_calma.tStart = t  # not accounting for scr refresh
        c_calma.frameNStart = frameN  # exact frame index
        win.timeOnFlip(c_calma, 'tStartRefresh')  # time at next scr refresh
        c_calma.setAutoDraw(True)
    
    # *t_calma* updates
    if t >= 0.0 and t_calma.status == NOT_STARTED:
        # keep track of start time/frame for later
        t_calma.tStart = t  # not accounting for scr refresh
        t_calma.frameNStart = frameN  # exact frame index
        win.timeOnFlip(t_calma, 'tStartRefresh')  # time at next scr refresh
        t_calma.setAutoDraw(True)
    
    # *rostro* updates
    if t >= 0.0 and rostro.status == NOT_STARTED:
        # keep track of start time/frame for later
        rostro.tStart = t  # not accounting for scr refresh
        rostro.frameNStart = frameN  # exact frame index
        win.timeOnFlip(rostro, 'tStartRefresh')  # time at next scr refresh
        rostro.setAutoDraw(True)
    
    # *c_ninguna* updates
    if t >= 0.0 and c_ninguna.status == NOT_STARTED:
        # keep track of start time/frame for later
        c_ninguna.tStart = t  # not accounting for scr refresh
        c_ninguna.frameNStart = frameN  # exact frame index
        win.timeOnFlip(c_ninguna, 'tStartRefresh')  # time at next scr refresh
        c_ninguna.setAutoDraw(True)
    
    # *t_ninguna* updates
    if t >= 0.0 and t_ninguna.status == NOT_STARTED:
        # keep track of start time/frame for later
        t_ninguna.tStart = t  # not accounting for scr refresh
        t_ninguna.frameNStart = frameN  # exact frame index
        win.timeOnFlip(t_ninguna, 'tStartRefresh')  # time at next scr refresh
        t_ninguna.setAutoDraw(True)
    
    # *pregunta* updates
    if t >= 0.0 and pregunta.status == NOT_STARTED:
        # keep track of start time/frame for later
        pregunta.tStart = t  # not accounting for scr refresh
        pregunta.frameNStart = frameN  # exact frame index
        win.timeOnFlip(pregunta, 'tStartRefresh')  # time at next scr refresh
        pregunta.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial"-------
for thisComponent in trialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('c_alegria.started', c_alegria.tStartRefresh)
thisExp.addData('c_alegria.stopped', c_alegria.tStopRefresh)
thisExp.addData('t_alegria.started', t_alegria.tStartRefresh)
thisExp.addData('t_alegria.stopped', t_alegria.tStopRefresh)
thisExp.addData('c_tristeza.started', c_tristeza.tStartRefresh)
thisExp.addData('c_tristeza.stopped', c_tristeza.tStopRefresh)
thisExp.addData('t_tristeza.started', t_tristeza.tStartRefresh)
thisExp.addData('t_tristeza.stopped', t_tristeza.tStopRefresh)
thisExp.addData('c_enojo.started', c_enojo.tStartRefresh)
thisExp.addData('c_enojo.stopped', c_enojo.tStopRefresh)
thisExp.addData('t_enojo.started', t_enojo.tStartRefresh)
thisExp.addData('t_enojo.stopped', t_enojo.tStopRefresh)
thisExp.addData('c_asco.started', c_asco.tStartRefresh)
thisExp.addData('c_asco.stopped', c_asco.tStopRefresh)
thisExp.addData('t_asco.started', t_asco.tStartRefresh)
thisExp.addData('t_asco.stopped', t_asco.tStopRefresh)
thisExp.addData('c_miedo.started', c_miedo.tStartRefresh)
thisExp.addData('c_miedo.stopped', c_miedo.tStopRefresh)
thisExp.addData('t_miedo.started', t_miedo.tStartRefresh)
thisExp.addData('t_miedo.stopped', t_miedo.tStopRefresh)
thisExp.addData('c_sorpresa.started', c_sorpresa.tStartRefresh)
thisExp.addData('c_sorpresa.stopped', c_sorpresa.tStopRefresh)
thisExp.addData('t_sorpresa.started', t_sorpresa.tStartRefresh)
thisExp.addData('t_sorpresa.stopped', t_sorpresa.tStopRefresh)
thisExp.addData('c_neutral.started', c_neutral.tStartRefresh)
thisExp.addData('c_neutral.stopped', c_neutral.tStopRefresh)
thisExp.addData('t_neutral.started', t_neutral.tStartRefresh)
thisExp.addData('t_neutral.stopped', t_neutral.tStopRefresh)
thisExp.addData('c_calma.started', c_calma.tStartRefresh)
thisExp.addData('c_calma.stopped', c_calma.tStopRefresh)
thisExp.addData('t_calma.started', t_calma.tStartRefresh)
thisExp.addData('t_calma.stopped', t_calma.tStopRefresh)
thisExp.addData('rostro.started', rostro.tStartRefresh)
thisExp.addData('rostro.stopped', rostro.tStopRefresh)
thisExp.addData('c_ninguna.started', c_ninguna.tStartRefresh)
thisExp.addData('c_ninguna.stopped', c_ninguna.tStopRefresh)
thisExp.addData('t_ninguna.started', t_ninguna.tStartRefresh)
thisExp.addData('t_ninguna.stopped', t_ninguna.tStopRefresh)
thisExp.addData('pregunta.started', pregunta.tStartRefresh)
thisExp.addData('pregunta.stopped', pregunta.tStopRefresh)
# the Routine "trial" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
