#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.1.5),
    on febrero 10, 2020, at 14:01
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
expInfo = {'participant': '', 'session': '001', 'edad': '', 'sexo': '', 'ocupacion': ''}
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
    originPath='C:\\Users\\Diego Ramírez\\Desktop\\emociones\\test_emocion_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

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

# Initialize components for Routine "Instrucciones"
InstruccionesClock = core.Clock()
instrucciones = visual.TextStim(win=win, name='instrucciones',
    text="Se te mostrarán rostros de 45 personas distintas haciendo varias expresiones emocionales. \n\nDeberás seleccionar si el rostro expresa Alegría, Enojo, Miedo, Neutralidad, Tristeza, Asco, Sorpresa o Calma, o seleccionar 'Ninguna Opción' si las otras respuestas no parecen apropiadas. También deberás de responder si el rostro de la persona parece el de alguien de la comunidad en la que vives. Esto te tomará alrededor 15 minutos.\n\nPara responder, haz click con tu mouse sobre los recuadros que contengan la respuesta que quieres dar. ",
    font='Arial',
    pos=(0, .1), height=0.05, wrapWidth=1.5, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
c_iniciar = visual.Rect(
    win=win, name='c_iniciar',
    width=(0.32, 0.125)[0], height=(0.32, 0.125)[1],
    ori=0, pos=(0, -.4),
    lineWidth=2, lineColor=[1.000,1.000,1.000], lineColorSpace='rgb',
    fillColor=None, fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
mouse_3 = event.Mouse(win=win)
x, y = [None, None]
mouse_3.mouseClock = core.Clock()
t_iniciar = visual.TextStim(win=win, name='t_iniciar',
    text='¡Click para\nIniciar!',
    font='Arial',
    pos=(0, -.4), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "siguiente"
siguienteClock = core.Clock()
t_siguiente = visual.TextStim(win=win, name='t_siguiente',
    text='¡Siguiente!',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

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
    image='sin', mask=None,
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
    opacity=1, depth=-17.0, interpolate=True)
t_ninguna = visual.TextStim(win=win, name='t_ninguna',
    text='Ninguna\nOpción',
    font='Arial',
    pos=(.6, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-18.0);
pregunta = visual.TextStim(win=win, name='pregunta',
    text='¿Qué emoción muestra \neste rostro?',
    font='Arial',
    pos=(-.6, .4), height=0.05, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-19.0);
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()

# Initialize components for Routine "pregunta1"
pregunta1Clock = core.Clock()
image = visual.ImageStim(
    win=win,
    name='image', 
    image='sin', mask=None,
    ori=0, pos=(0, .12), size=(.85, .75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
p1 = visual.TextStim(win=win, name='p1',
    text='¿Podría ser este rostro de un \nmiembro de tu comunidad?',
    font='Arial',
    pos=(0, -.35), height=0.075, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
c_si = visual.Rect(
    win=win, name='c_si',
    width=(0.2, 0.125)[0], height=(0.2, 0.125)[1],
    ori=0, pos=(-.65, -.35),
    lineWidth=2, lineColor=[1.000,1.000,1.000], lineColorSpace='rgb',
    fillColor=[-1.000,-1.000,-1.000], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
t_si = visual.TextStim(win=win, name='t_si',
    text='Sí',
    font='Arial',
    pos=(-.65, -.35), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
c_no = visual.Rect(
    win=win, name='c_no',
    width=(0.2, 0.125)[0], height=(0.2, 0.125)[1],
    ori=0, pos=(.65, -.35),
    lineWidth=2, lineColor=[1.000,1.000,1.000], lineColorSpace='rgb',
    fillColor=[-1.000,-1.000,-1.000], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
t_no = visual.TextStim(win=win, name='t_no',
    text='No',
    font='Arial',
    pos=(.65, -.35), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
mouse_2 = event.Mouse(win=win)
x, y = [None, None]
mouse_2.mouseClock = core.Clock()

# Initialize components for Routine "Gracias"
GraciasClock = core.Clock()
fin = visual.TextStim(win=win, name='fin',
    text='Fin\n\n¡Gracias por Participar!',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Instrucciones"-------
t = 0
InstruccionesClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_3
mouse_3.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
InstruccionesComponents = [instrucciones, c_iniciar, mouse_3, t_iniciar]
for thisComponent in InstruccionesComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Instrucciones"-------
while continueRoutine:
    # get current time
    t = InstruccionesClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instrucciones* updates
    if t >= 0.0 and instrucciones.status == NOT_STARTED:
        # keep track of start time/frame for later
        instrucciones.tStart = t  # not accounting for scr refresh
        instrucciones.frameNStart = frameN  # exact frame index
        win.timeOnFlip(instrucciones, 'tStartRefresh')  # time at next scr refresh
        instrucciones.setAutoDraw(True)
    
    # *c_iniciar* updates
    if t >= .5 and c_iniciar.status == NOT_STARTED:
        # keep track of start time/frame for later
        c_iniciar.tStart = t  # not accounting for scr refresh
        c_iniciar.frameNStart = frameN  # exact frame index
        win.timeOnFlip(c_iniciar, 'tStartRefresh')  # time at next scr refresh
        c_iniciar.setAutoDraw(True)
    # *mouse_3* updates
    if t >= .5 and mouse_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        mouse_3.tStart = t  # not accounting for scr refresh
        mouse_3.frameNStart = frameN  # exact frame index
        win.timeOnFlip(mouse_3, 'tStartRefresh')  # time at next scr refresh
        mouse_3.status = STARTED
        mouse_3.mouseClock.reset()
        prevButtonState = mouse_3.getPressed()  # if button is down already this ISN'T a new click
    if mouse_3.status == STARTED:  # only update if started and not finished!
        buttons = mouse_3.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                for obj in [c_iniciar]:
                    if obj.contains(mouse_3):
                        gotValidClick = True
                        mouse_3.clicked_name.append(obj.name)
                if gotValidClick:  # abort routine on response
                    continueRoutine = False
    
    # *t_iniciar* updates
    if t >= .5 and t_iniciar.status == NOT_STARTED:
        # keep track of start time/frame for later
        t_iniciar.tStart = t  # not accounting for scr refresh
        t_iniciar.frameNStart = frameN  # exact frame index
        win.timeOnFlip(t_iniciar, 'tStartRefresh')  # time at next scr refresh
        t_iniciar.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstruccionesComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instrucciones"-------
for thisComponent in InstruccionesComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
# the Routine "Instrucciones" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
bloques = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('g1_bloques.xlsx'),
    seed=None, name='bloques')
thisExp.addLoop(bloques)  # add the loop to the experiment
thisBloque = bloques.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBloque.rgb)
if thisBloque != None:
    for paramName in thisBloque:
        exec('{} = thisBloque[paramName]'.format(paramName))

for thisBloque in bloques:
    currentLoop = bloques
    # abbreviate parameter names if possible (e.g. rgb = thisBloque.rgb)
    if thisBloque != None:
        for paramName in thisBloque:
            exec('{} = thisBloque[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "siguiente"-------
    t = 0
    siguienteClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    siguienteComponents = [t_siguiente]
    for thisComponent in siguienteComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "siguiente"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = siguienteClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *t_siguiente* updates
        if t >= 0.0 and t_siguiente.status == NOT_STARTED:
            # keep track of start time/frame for later
            t_siguiente.tStart = t  # not accounting for scr refresh
            t_siguiente.frameNStart = frameN  # exact frame index
            win.timeOnFlip(t_siguiente, 'tStartRefresh')  # time at next scr refresh
            t_siguiente.setAutoDraw(True)
        frameRemains = 0.0 + .5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if t_siguiente.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            t_siguiente.tStop = t  # not accounting for scr refresh
            t_siguiente.frameNStop = frameN  # exact frame index
            win.timeOnFlip(t_siguiente, 'tStopRefresh')  # time at next scr refresh
            t_siguiente.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in siguienteComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "siguiente"-------
    for thisComponent in siguienteComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('trials_emo.xlsx'),
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    for thisTrial in trials:
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                exec('{} = thisTrial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "trial"-------
        t = 0
        trialClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        rostro.setImage(direccion_rostro + emo_direccion)
        # setup some python lists for storing info about the mouse
        mouse.clicked_name = []
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        trialComponents = [c_alegria, t_alegria, c_tristeza, t_tristeza, c_enojo, t_enojo, c_asco, t_asco, c_miedo, t_miedo, c_sorpresa, t_sorpresa, c_neutral, t_neutral, c_calma, t_calma, rostro, c_ninguna, t_ninguna, pregunta, mouse]
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
            if t >= .5 and c_alegria.status == NOT_STARTED:
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
            if t >= .5 and c_tristeza.status == NOT_STARTED:
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
            if t >= .5 and c_enojo.status == NOT_STARTED:
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
            if t >= .5 and c_asco.status == NOT_STARTED:
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
            if t >= .5 and c_miedo.status == NOT_STARTED:
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
            if t >= .5 and c_sorpresa.status == NOT_STARTED:
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
            if t >= .5 and c_neutral.status == NOT_STARTED:
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
            if t >= .5 and c_calma.status == NOT_STARTED:
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
            if t >= .5 and c_ninguna.status == NOT_STARTED:
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
            # *mouse* updates
            if t >= .5 and mouse.status == NOT_STARTED:
                # keep track of start time/frame for later
                mouse.tStart = t  # not accounting for scr refresh
                mouse.frameNStart = frameN  # exact frame index
                win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
                mouse.status = STARTED
                mouse.mouseClock.reset()
                prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
            if mouse.status == STARTED:  # only update if started and not finished!
                buttons = mouse.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        for obj in [c_alegria, c_tristeza, c_enojo, c_asco, c_miedo, c_sorpresa, c_neutral, c_calma, c_ninguna]:
                            if obj.contains(mouse):
                                gotValidClick = True
                                mouse.clicked_name.append(obj.name)
                        if gotValidClick:  # abort routine on response
                            continueRoutine = False
            
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
        trials.addData('pregunta.started', pregunta.tStartRefresh)
        trials.addData('pregunta.stopped', pregunta.tStopRefresh)
        # store data for trials (TrialHandler)
        x, y = mouse.getPos()
        buttons = mouse.getPressed()
        if sum(buttons):
            # check if the mouse was inside our 'clickable' objects
            gotValidClick = False
            for obj in [c_alegria, c_tristeza, c_enojo, c_asco, c_miedo, c_sorpresa, c_neutral, c_calma, c_ninguna]:
                if obj.contains(mouse):
                    gotValidClick = True
                    mouse.clicked_name.append(obj.name)
        trials.addData('mouse.x', x)
        trials.addData('mouse.y', y)
        trials.addData('mouse.leftButton', buttons[0])
        trials.addData('mouse.midButton', buttons[1])
        trials.addData('mouse.rightButton', buttons[2])
        if len(mouse.clicked_name):
            trials.addData('mouse.clicked_name', mouse.clicked_name[0])
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trials'
    
    
    # ------Prepare to start Routine "pregunta1"-------
    t = 0
    pregunta1Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    image.setImage(direccion_collage)
    # setup some python lists for storing info about the mouse_2
    mouse_2.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    pregunta1Components = [image, p1, c_si, t_si, c_no, t_no, mouse_2]
    for thisComponent in pregunta1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "pregunta1"-------
    while continueRoutine:
        # get current time
        t = pregunta1Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image* updates
        if t >= 0.0 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t  # not accounting for scr refresh
            image.frameNStart = frameN  # exact frame index
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            image.setAutoDraw(True)
        
        # *p1* updates
        if t >= 0.0 and p1.status == NOT_STARTED:
            # keep track of start time/frame for later
            p1.tStart = t  # not accounting for scr refresh
            p1.frameNStart = frameN  # exact frame index
            win.timeOnFlip(p1, 'tStartRefresh')  # time at next scr refresh
            p1.setAutoDraw(True)
        
        # *c_si* updates
        if t >= .5 and c_si.status == NOT_STARTED:
            # keep track of start time/frame for later
            c_si.tStart = t  # not accounting for scr refresh
            c_si.frameNStart = frameN  # exact frame index
            win.timeOnFlip(c_si, 'tStartRefresh')  # time at next scr refresh
            c_si.setAutoDraw(True)
        
        # *t_si* updates
        if t >= 0.0 and t_si.status == NOT_STARTED:
            # keep track of start time/frame for later
            t_si.tStart = t  # not accounting for scr refresh
            t_si.frameNStart = frameN  # exact frame index
            win.timeOnFlip(t_si, 'tStartRefresh')  # time at next scr refresh
            t_si.setAutoDraw(True)
        
        # *c_no* updates
        if t >= .5 and c_no.status == NOT_STARTED:
            # keep track of start time/frame for later
            c_no.tStart = t  # not accounting for scr refresh
            c_no.frameNStart = frameN  # exact frame index
            win.timeOnFlip(c_no, 'tStartRefresh')  # time at next scr refresh
            c_no.setAutoDraw(True)
        
        # *t_no* updates
        if t >= 0.0 and t_no.status == NOT_STARTED:
            # keep track of start time/frame for later
            t_no.tStart = t  # not accounting for scr refresh
            t_no.frameNStart = frameN  # exact frame index
            win.timeOnFlip(t_no, 'tStartRefresh')  # time at next scr refresh
            t_no.setAutoDraw(True)
        # *mouse_2* updates
        if t >= .5 and mouse_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            mouse_2.tStart = t  # not accounting for scr refresh
            mouse_2.frameNStart = frameN  # exact frame index
            win.timeOnFlip(mouse_2, 'tStartRefresh')  # time at next scr refresh
            mouse_2.status = STARTED
            mouse_2.mouseClock.reset()
            prevButtonState = mouse_2.getPressed()  # if button is down already this ISN'T a new click
        if mouse_2.status == STARTED:  # only update if started and not finished!
            buttons = mouse_2.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    for obj in [c_si, c_no]:
                        if obj.contains(mouse_2):
                            gotValidClick = True
                            mouse_2.clicked_name.append(obj.name)
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pregunta1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "pregunta1"-------
    for thisComponent in pregunta1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for bloques (TrialHandler)
    x, y = mouse_2.getPos()
    buttons = mouse_2.getPressed()
    if sum(buttons):
        # check if the mouse was inside our 'clickable' objects
        gotValidClick = False
        for obj in [c_si, c_no]:
            if obj.contains(mouse_2):
                gotValidClick = True
                mouse_2.clicked_name.append(obj.name)
    bloques.addData('mouse_2.x', x)
    bloques.addData('mouse_2.y', y)
    bloques.addData('mouse_2.leftButton', buttons[0])
    bloques.addData('mouse_2.midButton', buttons[1])
    bloques.addData('mouse_2.rightButton', buttons[2])
    if len(mouse_2.clicked_name):
        bloques.addData('mouse_2.clicked_name', mouse_2.clicked_name[0])
    # the Routine "pregunta1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1 repeats of 'bloques'


# ------Prepare to start Routine "Gracias"-------
t = 0
GraciasClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
GraciasComponents = [fin]
for thisComponent in GraciasComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Gracias"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = GraciasClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *fin* updates
    if t >= .5 and fin.status == NOT_STARTED:
        # keep track of start time/frame for later
        fin.tStart = t  # not accounting for scr refresh
        fin.frameNStart = frameN  # exact frame index
        win.timeOnFlip(fin, 'tStartRefresh')  # time at next scr refresh
        fin.setAutoDraw(True)
    frameRemains = .5 + 2.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if fin.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        fin.tStop = t  # not accounting for scr refresh
        fin.frameNStop = frameN  # exact frame index
        win.timeOnFlip(fin, 'tStopRefresh')  # time at next scr refresh
        fin.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in GraciasComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Gracias"-------
for thisComponent in GraciasComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

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
