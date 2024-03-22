import maya.cmds as mc

import Switcher

import importlib

importlib.reload(Switcher)

def createUI():
    IKFKWindowID = "IKFKWindow"
    if mc.window(IKFKWindowID, exists = True):
        mc.deleteUI(IKFKWindowID)
    mc.window   (IKFKWindowID, t = "Hand Controller")
    mc.showWindow(IKFKWindowID)

    fullLayout = mc.columnLayout()
    mainLayout = mc.frameLayout(l = "IKFK Switch & Reset", w = 300, li = 93)
    mc.separator(style = 'in')
    transferLayout = mc.rowColumnLayout(nc = 3, parent = mainLayout, cw = [(1,100), (2,100), (3,100)])


    mc.button(l = "Seamless Switcher", c = "Switcher.seamlessSwitch()")
    mc.button(l = "Switcher", c = "Switcher.standardSwitch()")
    mc.button(l = "Reset Selected", c = "Switcher.resetObjects()")
    mc.separator( style='none', h=20)
    mc.setParent(mainLayout)
    mc.button(l = "Reset Full Rig", c = "Switcher.confirm_prompt()")



    mainLayout = mc.frameLayout(l = "Mirror", w = 300, li = 125)
    mc.separator(style='in')
    mc.button(l = "Left -> Right", c = "Switcher.mirrorL2R()")
    mc.button(l = "Right -> Left", c = "Switcher.mirrorR2L()")