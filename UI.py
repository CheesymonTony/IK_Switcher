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
    axisRotateLayout = mc.rowColumnLayout(nc = 3, parent = mainLayout, cw = [(1,100), (2,100), (3,100)])
    mc.text(l='X-axis', parent = axisRotateLayout)
    mc.text(l = 'Y-axis', parent = axisRotateLayout)
    mc.text(l = 'Y-axis', parent = axisRotateLayout)
    xAxisLayout = mc.rowColumnLayout(nc = 3, parent = axisRotateLayout, cw = [(1,40), (2,10), (3,40)])
    mc.button(l='+90', c="Switcher.rotateObjectByAmount(90, 'X')", parent = xAxisLayout)
    mc.text(l = '')
    mc.button(l='-90', c="Switcher.rotateObjectByAmount(-90, 'X')", parent = xAxisLayout)

    YAxisLayout = mc.rowColumnLayout(nc = 3, parent = axisRotateLayout, cw = [(1,40), (2,10), (3,40)])
    mc.button(l='+90', c="Switcher.rotateObjectByAmount(90, 'Y')", parent = YAxisLayout)
    mc.text(l = '', parent = YAxisLayout)
    mc.button(l='-90', c="Switcher.rotateObjectByAmount(-90, 'Y')", parent = YAxisLayout)

    zAxisLayout = mc.rowColumnLayout(nc = 3, parent = axisRotateLayout, cw = [(1,40), (2,10), (3,40)])
    mc.button(l='+90', c="Switcher.rotateObjectByAmount(90, 'Z')", parent = zAxisLayout)
    mc.text(l = '', parent = zAxisLayout)
    mc.button(l='-90', c="Switcher.rotateObjectByAmount(-90, 'Z')", parent = zAxisLayout)

    mc.setParent(mainLayout)
    mc.button(l = "Left -> Right", c = "Switcher.mirrorL2R()")
    mc.button(l = "Right -> Left", c = "Switcher.mirrorR2L()")