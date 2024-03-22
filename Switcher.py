import maya.cmds as mc
import sys
import os
import json
from pathlib import Path

import toolDirectory
import switchUtils as utils
# Reload the module
import importlib
importlib.reload(toolDirectory)
importlib.reload(utils)


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#Methods
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#Name Collection Function#
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def confirm_prompt():
    """Function to display a confirmation dialog."""
    result = mc.confirmDialog(
        title='Confirm',
        message='Are you sure?',
        button=['Yes','No'],
        defaultButton='Yes',
        cancelButton='No',
        dismissString='No')

    if result == 'Yes':
        fullRigReset()

def fullRigReset():
    #reset the main control of the hand - "Ctrl_Global_Hands_01" 
    # and then each of the main controls in the rig
    mainCtrl = 'Ctrl_Global_Hands_01'
    mc.setAttr(mainCtrl + '.LeftHandTool', 22)
    mc.setAttr(mainCtrl + '.RightHandTool', 22)
    mc.setAttr(mainCtrl + '.Hands', 0)
    mc.setAttr(mainCtrl + '.IK_Arms', 1)
    mc.setAttr(mainCtrl + '.ToolDisplay', 0)

    controlObjs = utils.select_transforms_with_prefix_and_types()

    resetObjects(controlObjs)
    




def getName(nameSpace, path, toolAttr):
    print('in there')
    fromTool = None
    toTool = None
    if "Left" in path:
        #get name of the left tool which will be receiving the mirrored values
        if toolAttr == 1:
            fromTool = "%sCtrl__L_MayoSS__Main_01" %(nameSpace)
            toTool = "%sCtrl__R_MayoSS__Main_01" %(nameSpace)
        elif toolAttr == 2:
            fromTool = "%sCtrl__L_Scalpl__Main_01" %(nameSpace)
            toTool = "%sCtrl__R_Scalpl__Main_01" %(nameSpace)
        elif toolAttr == 3:
            fromTool = "%sCtrl__L_OlHeND__Main_01" %(nameSpace)
            toTool = "%sCtrl__R_OlHeND__Main_01" %(nameSpace)
        elif toolAttr == 4:
            fromTool = "%sCtrl__L_DebFor__Main_01" %(nameSpace)
            toTool = "%sCtrl__R_DebFor__Main_01" %(nameSpace)
        elif toolAttr == 5:
            fromTool = "%sCtrl__L_HaMoHe__Main_01" %(nameSpace)
            toTool = "%sCtrl__R_HaMoHe__Main_01" %(nameSpace)
        elif toolAttr == 6:
            fromTool = "%sCtrl__L_SpaHok__Main_01" %(nameSpace)
            toTool = "%sCtrl__R_SpaHok__Main_01" %(nameSpace)
        elif toolAttr == 7:
            fromTool = "%sCtrl__L_PaHaRe__Main_01" %(nameSpace)
            toTool = "%sCtrl__R_PaHaRe__Main_01" %(nameSpace)
        elif toolAttr == 8:
            fromTool = "%sCtrl__L_RoCaHe__Main_01" %(nameSpace)
            toTool = "%sCtrl__R_RoCaHe__Main_01" %(nameSpace)
        elif toolAttr == 9:
            fromTool = "%sCtrl__L_CriHem__Main_01" %(nameSpace)
            toTool = "%sCtrl__R_CriHem__Main_01" %(nameSpace)
        elif toolAttr == 10:
            fromTool = "%sCtrl__L_KelHem__Main_01" %(nameSpace)
            toTool = "%sCtrl__R_KelHem__Main_01" %(nameSpace)
        elif toolAttr == 11:
            fromTool = "%sCtrl__L_MetSci__Main_01" %(nameSpace)
            toTool = "%sCtrl__R_MetSci__Main_01" %(nameSpace)
        elif toolAttr == 12:
            fromTool = "%sCtrl__L_BackTC__Main_01" %(nameSpace)
            toTool = "%sCtrl__R_BackTC__Main_01" %(nameSpace)
        elif toolAttr == 13:
            fromTool = "%sCtrl__L_MayoND__Main_01" %(nameSpace)
            toTool = "%sCtrl__R_MayoND__Main_01" %(nameSpace)
        elif toolAttr == 14:
            fromTool = "%sCtrl__L_AdRaFo__Main_01" %(nameSpace)
            toTool = "%sCtrl__R_AdRaFo__Main_01" %(nameSpace)
        elif toolAttr == 15:
            fromTool = "%sCtrl__L_BrAdFo__Main_01" %(nameSpace)
            toTool = "%sCtrl__R_BrAdFo__Main_01" %(nameSpace)
        return fromTool, toTool
    else:
        #get name of the right tool which will be receiving the mirrored values
        if toolAttr == 1:
            fromTool = "%sCtrl__R_MayoSS__Main_01" %(nameSpace)
            toTool = "%sCtrl__L_MayoSS__Main_01" %(nameSpace)
        elif toolAttr == 2:
            fromTool = "%sCtrl__R_Scalpl__Main_01" %(nameSpace)
            toTool = "%sCtrl__L_Scalpl__Main_01" %(nameSpace)
        elif toolAttr == 3:
            fromTool = "%sCtrl__R_OlHeND__Main_01" %(nameSpace)
            toTool = "%sCtrl__L_OlHeND__Main_01" %(nameSpace)
        elif toolAttr == 4:
            fromTool = "%sCtrl__R_DebFor__Main_01" %(nameSpace)
            toTool = "%sCtrl__L_DebFor__Main_01" %(nameSpace)
        elif toolAttr == 5:
            fromTool = "%sCtrl__R_HaMoHe__Main_01" %(nameSpace)
            toTool = "%sCtrl__L_HaMoHe__Main_01" %(nameSpace)
        elif toolAttr == 6:
            fromTool = "%sCtrl__R_SpaHok__Main_01" %(nameSpace)
            toTool = "%sCtrl__L_SpaHok__Main_01" %(nameSpace)
        elif toolAttr == 7:
            fromTool = "%sCtrl__R_PaHaRe__Main_01" %(nameSpace)
            toTool = "%sCtrl__L_PaHaRe__Main_01" %(nameSpace)
        elif toolAttr == 8:
            fromTool = "%sCtrl__R_RoCaHe__Main_01" %(nameSpace)
            toTool = "%sCtrl__L_RoCaHe__Main_01" %(nameSpace)
        elif toolAttr == 9:
            fromTool = "%sCtrl__R_CriHem__Main_01" %(nameSpace)
            toTool = "%sCtrl__L_CriHem__Main_01" %(nameSpace)
        elif toolAttr == 10:
            fromTool = "%sCtrl__R_KelHem__Main_01" %(nameSpace)
            toTool = "%sCtrl__L_KelHem__Main_01" %(nameSpace)
        elif toolAttr == 11:
            fromTool = "%sCtrl__R_MetSci__Main_01" %(nameSpace)
            toTool = "%sCtrl__L_MetSci__Main_01" %(nameSpace)
        elif toolAttr == 12:
            fromTool = "%sCtrl__R_BackTC__Main_01" %(nameSpace)
            toTool = "%sCtrl__L_BackTC__Main_01" %(nameSpace)
        elif toolAttr == 13:
            fromTool = "%sCtrl__R_MayoND__Main_01" %(nameSpace)
            toTool = "%sCtrl__L_MayoND__Main_01" %(nameSpace)
        elif toolAttr == 14:
            fromTool = "%sCtrl__R_AdRaFo__Main_01" %(nameSpace)
            toTool = "%sCtrl__L_AdRaFo__Main_01" %(nameSpace)
        elif toolAttr == 15:
            fromTool = "%sCtrl__R_BrAdFo__Main_01" %(nameSpace)
            toTool = "%sCtrl__L_BrAdFo__Main_01" %(nameSpace)
        print('fromTool: ', fromTool, 'toTool: ', toTool)
        return fromTool, toTool




""""""""""""""""""""""""""""""""""""""""""
#Seamless Switch Function#
""""""""""""""""""""""""""""""""""""""""""
#This function is used to seamlessly switch between the FK and IK systems, on whichever fingers are selected

def seamlessSwitch():
    print('seamlessSwitch()')
    #Store selection information
    
    sele = mc.ls(selection=True)
    
    #Store body side, and the finger type in their own variables
    
    for obj in sele:
        if ":" in obj:
            #If ":" is present in the selection name, then it has a namespace. The Namespace and name need to be split.
            nameSpace = obj.split(":")[0]+":"
            sansNameSpace = obj.split(":")[1]
            fingerType = sansNameSpace.split("_")[2]
            bodySide = sansNameSpace.split("_")[1]
            
        else:
            #Otherwise, it has no namespace, and can continue with just the selected object.
            nameSpace = ""
            fingerType = obj.split("_")[2]
            bodySide = obj.split("_")[1]
               
    
        #Determine which hand is being affected and store the name of the controller in a variable
                
        wristCtrl = "%sCtrl_%s_Wrist_01" %(nameSpace, bodySide)
        
        #Using the stored information so far, we now need to gather the state of the ik system for that specific finger
        
        ikState = mc.getAttr(wristCtrl + "." + fingerType)
        
        #If the ikState is 0, then we need to take the proper attribute values from the FK system, and plug them into the IK system.
        #If the ikState is 1, then we need to take the proper attribute values from the IK system, and plug them into the FK system.
        #For this transference of data, I am using locators, placed at each finger joint, with zeroed out values that follow the joints orientation. Then I take this information and plug it into the receiving system(IK or FK). So the path is bone->locator->controller
        if ikState == 0:
            #transfer values from Location Marker to respective IK control
            mc.matchTransform("%sCtrl_%s_%s_IK_01" %(nameSpace, bodySide, fingerType), "%sLoc_%s_%s_LocationMarker_C_01" %(nameSpace, bodySide, fingerType))
            mc.matchTransform("%sCtrl_%s_%s_PoleVector_01" %(nameSpace, bodySide, fingerType), "%sLoc_%s_%s_PoleVector_LocationMarker_01" %(nameSpace, bodySide, fingerType), rot = False, scl = False)
            mc.setAttr(wristCtrl+"."+fingerType, 1)
            mc.select("%sCtrl_%s_%s_IK_01" %(nameSpace, bodySide, fingerType))
           
        else:
            #transfer values from Location Marker to respective Fk control
            mc.matchTransform("%sCtrl_%s_%s_A_01" %(nameSpace, bodySide, fingerType), "%sLoc_%s_%s_LocationMarker_A_01" %(nameSpace, bodySide, fingerType), rot = False, scl = False)
            mc.matchTransform("%sCtrl_%s_%s_B_01" %(nameSpace, bodySide, fingerType), "%sLoc_%s_%s_LocationMarker_B_01" %(nameSpace, bodySide, fingerType), rot = False, scl = False)
            mc.matchTransform("%sCtrl_%s_%s_C_01" %(nameSpace, bodySide, fingerType), "%sLoc_%s_%s_LocationMarker_C_01" %(nameSpace, bodySide, fingerType), rot = False, scl = False)
            mc.setAttr(wristCtrl+"."+fingerType, 0)
            mc.select("%sCtrl_%s_%s_A_01" %(nameSpace, bodySide, fingerType))

""""""""""""""""""""""""""""""""""""""""""
#Standard Switch Function#
""""""""""""""""""""""""""""""""""""""""""
#This function is used to switch between IK and FK system on selected fingers

def standardSwitch():
    print('standardSwitch()')
    
    #Store selection information

    sele = mc.ls(selection=True)
    
    #Store body side, and the finger type in their own variables
    
    for obj in sele:
        if ":" in obj:
            #If ":" is present in the selection name, then it has a namespace. The Namespace and name need to be split.
            nameSpace = obj.split(":")[0]+":"
            sansNameSpace = obj.split(":")[1]
            fingerType = sansNameSpace.split("_")[2]
            bodySide = sansNameSpace.split("_")[1]
            
        else:
            #Otherwise, it has no namespace, and can continue with just the selected object.
            nameSpace = ""
            fingerType = obj.split("_")[2]
            bodySide = obj.split("_")[1]
               
    
        #Determine which hand is being affected and store the name of the controller in a variable
                
        wristCtrl = "%sCtrl_%s_Wrist_01" %(nameSpace, bodySide)
        
        #Using the stored information so far, we now need to gather the state of the ik system for that specific finger
        
        ikState = mc.getAttr(wristCtrl + "." + fingerType)
        
        #If the ikState is 0, then we need to take the proper attribute values from the FK system, and plug them into the IK system.
        #If the ikState is 1, then we need to take the proper attribute values from the IK system, and plug them into the FK system.
        #For this transference of data, I am using locators, placed at each finger joint, with zeroed out values that follow the joints orientation. Then I take this information and plug it into the receiving system(IK or FK). So the path is bone->locator->controller
        if ikState == 0:
            #Switch Selected finger to Ik System and select new controller
            mc.setAttr(wristCtrl+"."+fingerType, 1)
            mc.select("%sCtrl_%s_%s_IK_01" %(nameSpace, bodySide, fingerType))
           
        else:
            #Switch selected finger to FK system and select new controller
            mc.setAttr(wristCtrl+"."+fingerType, 0)
            mc.select("%sCtrl_%s_%s_A_01" %(nameSpace, bodySide, fingerType))
   
""""""""""""""""""""""""""""""""""""""""""
#Finger Reset Function#
""""""""""""""""""""""""""""""""""""""""""
#This function is used to reset the selected finger to the default values of whichever system is currently being used
    
def resetObjects(sele = None):
    
    if sele is None:
        sele = mc.ls(sl=True)

    for obj in sele:
        attributes = ['.tx', '.ty', '.tz', '.rx', '.ry', '.rz']
        for attr in attributes:
            if mc.getAttr(f'{obj}{attr}', k = True) and not mc.getAttr(f'{obj}{attr}', l = True):
                mc.setAttr(f'{obj}{attr}', 0)
    
    
    
    
    
    '''
    #Store selection information
    
    sele = mc.ls(selection=True)
    
    #Store body side, and the finger type in their own variables
    
    for obj in sele:
        if ":" in obj:
            #If ":" is present in the selection name, then it has a namespace. The Namespace and name need to be split.
            nameSpace = obj.split(":")[0]+":"
            sansNameSpace = obj.split(":")[1]
            fingerType = sansNameSpace.split("_")[2]
            bodySide = sansNameSpace.split("_")[1]
            
        else:
            #Otherwise, it has no namespace, and can continue with just the selected object.
            nameSpace = ""
            fingerType = obj.split("_")[2]
            bodySide = obj.split("_")[1]
               
    
        #Determine which hand is being affected and store the name of the controller in a variable
                
        wristCtrl = "%sCtrl_%s_Wrist_01" %(nameSpace, bodySide)
        
        #Using the stored information so far, we now need to gather the state of the ik system for that specific finger
        
        ikState = mc.getAttr(wristCtrl + "." + fingerType)
        
        #If the ikState is 0, then we need to take the proper attribute values from the FK system, and plug them into the IK system.
        #If the ikState is 1, then we need to take the proper attribute values from the IK system, and plug them into the FK system.
        #For this transference of data, I am using locators, placed at each finger joint, with zeroed out values that follow the joints orientation. Then I take this information and plug it into the receiving system(IK or FK). So the path is bone->locator->controller
        if ikState == 0:
            #Reset values for the FK system
            mc.setAttr("%sCtrl_%s_%s_A_01" %(nameSpace, bodySide, fingerType)+"."+"rotate", 0, 0, 0)
            mc.setAttr("%sCtrl_%s_%s_B_01" %(nameSpace, bodySide, fingerType)+"."+"rotate", 0, 0, 0)
            mc.setAttr("%sCtrl_%s_%s_C_01" %(nameSpace, bodySide, fingerType)+"."+"rotate", 0, 0, 0)
           
        else:
            #Reset Values for the IK System
            mc.setAttr("%sCtrl_%s_%s_IK_01" %(nameSpace, bodySide, fingerType)+"."+"translate", 0, 0, 0)
            mc.setAttr("%sCtrl_%s_%s_PoleVector_01" %(nameSpace, bodySide, fingerType)+"."+"translate", 0, 0, 0)
            mc.setAttr("%sCtrl_%s_%s_IK_01" %(nameSpace, bodySide, fingerType)+"."+"rotate", 0, 0, 0)'''
            
            
            
            
""""""""""""""""""""""""""""""""""""""""""
#Mirror Functions#
""""""""""""""""""""""""""""""""""""""""""
#These functions allow the user to mirror the pose of one hand, including the instrument, to the other. Select only the controls you would like to have mirrored. Do no select controls that will receive the mirrored values.


#Mirror from the left to the right#

def mirrorL2R():
    print('mirrorL2R()')
    #Turn on the tool for the right hand and turn off the tool for the left hand
    mc.setAttr('Ctrl_Global_Hands_01.Hands', 1)
    mc.setAttr('Ctrl_Global_Hands_01.ToolDisplay', 1)
    #Store selection information
    
    sele = mc.ls(selection=True)
    
    #create index to use for specifying selection in the list: sele
    index = 0
    
    for obj in sele:
        if "_R_" in obj:
            mc.error("ERROR: Please only select objects from the left hand")
    
    #Loop to run on all of the objects in order to mirror values 
    
    for obj in sele:    
    
        path = str(mc.listRelatives(sele[index], f = True))
        
        if "Instruments" in path:
        
            #store the side that should have it's tool turned on
            if "Right" in path:
                handSide = "Right"
                otherHandSide = "Left"
        
            else:
                handSide = "Left"
                otherHandSide = "Right"
            
            #split the namespace and the object name for objects in selection
            if ":" in obj:
                nameSpace = (obj.split(":")[0] + ':')
                sansNameSpace = obj.split(":")[1]
            else:
                nameSpace = ""
                sansNameSpace = str(obj)
            
            #Turn on the tool on the other side of the rig
            toolAttr = mc.getAttr(nameSpace + 'Ctrl_Global_Hands_01' + ".%sHandTool" %(handSide)) 
            print('toolattr: ', toolAttr)
            mc.setAttr(nameSpace + 'Ctrl_Global_Hands_01' + ".%sHandTool" %(otherHandSide), toolAttr)
            
            #get the tool that will receive the mirrored values and store it in a variable using this function
            fromTool = toolDirectory.ToolDict.get_controller(toolAttr, side=handSide)
            toTool = toolDirectory.ToolDict.get_controller(toolAttr, side=otherHandSide)
           
            #Mirror the values
            locator = mc.spaceLocator()
            locGrp = mc.group(locator)
            mc.matchTransform(locator, fromTool)
            grpAttr = mc.getAttr(locGrp + '.sx')
            mc.setAttr(locGrp + '.sx', (grpAttr * -1))
            mc.parent(locator, w = True)
            mc.matchTransform(toTool, locator)
            rotX = mc.getAttr(toTool + '.rx')
            mc.setAttr(toTool + '.rx', rotX - 180)
            mc.delete(locator)
            mc.delete(locGrp)
            mc.setAttr(nameSpace + 'Ctrl_Global_Hands_01' + ".%sHandTool" %(handSide), 0)
            
            index += 1    
                
        else:        
        
            #Store the values to be mirrored
            if mc.getAttr(obj + '.tx', k = True, l = False):
                tranX = mc.getAttr(sele[index] + '.tx')
            if mc.getAttr(obj + '.ty', k = True, l = False):
                tranY = mc.getAttr(sele[index] + '.ty')
            if mc.getAttr(obj + '.tz', k = True, l = False):
                tranZ = mc.getAttr(sele[index] + '.tz')
            if mc.getAttr(obj + '.rx', k = True, l = False):
                rotX = mc.getAttr(sele[index] + '.rx')
            if mc.getAttr(obj + '.ry', k = True, l = False):
                rotY = mc.getAttr(sele[index] + '.ry')
            if mc.getAttr(obj + '.rz', k = True, l = False):
                rotZ = mc.getAttr(sele[index] + '.rz')
                
            #create variables for identifiers
            r = "_R_"
            l = "_L_"
            
            #split the namespace and the object name for objects in selection
            
            if ":" in obj:
                nameSpace = (obj.split(":")[0] + ':')
                sansNameSpace = obj.split(":")[1]
            else:
                nameSpace = ""
                sansNameSpace = str(obj)
            
            #divide the object names to reuse in mirroring process with identifier variable
            name1 = sansNameSpace.split(l)[0]
            name2 = sansNameSpace.split(l)[1]
            
            #concatenate and store the name of the object that will be receiving the mirrored values
            fullName = nameSpace + ":" + name1 + r + name2
            
            #concatenate the object name with the attribute that will be receiving the mirrored values
            if mc.getAttr(obj + '.tx', k = True, l = False):
                nameTX = fullName + '.tx'
            if mc.getAttr(obj + '.ty', k = True, l = False):
                nameTY = fullName + '.ty'
            if mc.getAttr(obj + '.tz', k = True, l = False):
                nameTZ = fullName + '.tz'
            if mc.getAttr(obj + '.rx', k = True, l = False):
                nameRX = fullName + '.rx'
            if mc.getAttr(obj + '.ry', k = True, l = False):
                nameRY = fullName + '.ry'
            if mc.getAttr(obj + '.rz', k = True, l = False):
                nameRZ = fullName + '.rz'
            
            #determine the type of controller that's being assigned, in order to determine how to mirror values
            if "ForeArm" in fullName:
                multTX = -1
                multTY = 1
                multTZ = 1
                multRX = 1
                multRY = -1
                multRZ = -1
                
            elif "Wrist" in fullName:
                multTX = -1
                multTY = 1
                multTZ = 1
                multRX = 1
                multRY = -1
                multRZ = -1
                
            elif "Carpal_A" in fullName:
                multTX = 1
                multTY = -1
                multTZ = 1
                multRX = -1
                multRY = 1
                multRZ = -1
            
            elif "Carpal_B" in fullName:
                multTX = 1
                multTY = 1
                multTZ = -1
                multRX = -1
                multRY = -1
                multRZ = 1
                
            elif "Carpal_C" in fullName:
                multTX = 1
                multTY = 1
                multTZ = -1
                multRX = -1
                multRY = -1
                multRZ = 1
                
            elif "Thumb" in fullName:
                multRX = -1
                multRY = 1
                multRZ = -1
                
            else:
                multRX = -1
                multRY = -1
                multRZ = 1
                 
            
            #set the mirrored values to the receiving objects
            if mc.getAttr(obj + '.tx', k = True, l = False):
                mc.setAttr(nameTX, (tranX * multTX))
            if mc.getAttr(obj + '.ty', k = True, l = False):
                mc.setAttr(nameTY, (tranY * multTY))
            if mc.getAttr(obj + '.tz', k = True, l = False):
                mc.setAttr(nameTZ, (tranZ * multTZ))
            if mc.getAttr(obj + '.rx', k = True, l = False):
                mc.setAttr(nameRX, (rotX * multRX))
            if mc.getAttr(obj + '.ry', k = True, l = False):
                mc.setAttr(nameRY, (rotY * multRY))
            if mc.getAttr(obj + '.rz', k = True, l = False):
                mc.setAttr(nameRZ, (rotZ * multRZ))
                
            index += 1



#Mirror from the right to the left#

def mirrorR2L():

    #turn off Right hand objects and turn on Left hand objects
    mc.setAttr('Ctrl_Global_Hands_01.Hands', 2)
    mc.setAttr('Ctrl_Global_Hands_01.ToolDisplay', 2)


    print('mirrorR2L()')
    #Store selection information
    
    sele = mc.ls(selection=True)
    
    #create index to use for specifying selection in the list: sele
    index = 0
    
    for obj in sele:
        if "_L_" in obj:
            mc.error("ERROR: Please only select objects from the right hand")
    
    #Loop to run on all of the objects in order to mirror values 
    
    for obj in sele:    
    
        path = str(mc.listRelatives(sele[index], f = True))
        print('path: ', path)
        if "Instruments" in path:

            #store the side that should have it's tool turned on
            if "Right" in path:
                handSide = "Right"
                otherHandSide = "Left"
        
            else:
                handSide = "Left"
                otherHandSide = "Right"
            
            #split the namespace and the object name for objects in selection
            if ":" in obj:
                nameSpace = (obj.split(":")[0] + ':')
                sansNameSpace = obj.split(":")[1]
            else:
                nameSpace = ""
                sansNameSpace = obj[0]
            
            #Turn on the tool on the other side of the rig
            toolAttr = mc.getAttr(nameSpace + 'Ctrl_Global_Hands_01' + ".%sHandTool" %(handSide)) 
            print('toolattr: ', toolAttr)
            toolCtrl = toolDirectory.ToolDict.get_controller(toolAttr)
            print('toolCtrl: ', toolCtrl)
            mc.setAttr(nameSpace + 'Ctrl_Global_Hands_01' + ".%sHandTool" %(otherHandSide), toolAttr)
            
            print(handSide)
            #get the tool that will receive the mirrored values and store it in a variable using this function
            fromTool = toolDirectory.ToolDict.get_controller(toolAttr, side=handSide)
            toTool = toolDirectory.ToolDict.get_controller(toolAttr, side=otherHandSide)
           
            #Mirror the values
            locator = mc.spaceLocator()
            locGrp = mc.group(locator)
            mc.matchTransform(locator, fromTool)
            grpAttr = mc.getAttr(locGrp + '.sx')
            mc.setAttr(locGrp + '.sx', (grpAttr * -1))
            mc.parent(locator, w = True)
            mc.matchTransform(toTool, locator)
            rotX = mc.getAttr(toTool + '.rx')
            mc.setAttr(toTool + '.rx', rotX - 180)
            mc.delete(locator)
            mc.delete(locGrp)
            mc.setAttr(nameSpace + 'Ctrl_Global_Hands_01' + ".%sHandTool" %(handSide), 0)
            if mc.getAttr(toTool + '.sx') <= 0:
                mc.setAttr(toTool + '.sx', 1)
            if mc.getAttr(toTool + '.sy') <= 0:
                mc.setAttr(toTool + '.sy', 1)
            if mc.getAttr(toTool + '.sz') <= 0:
                mc.setAttr(toTool + '.sz', 1)
            index += 1    
                
        else:        
            
            #Store the values to be mirrored
            if mc.getAttr(obj + '.tx', k = True, l = False):
                tranX = mc.getAttr(sele[index] + '.tx')
            if mc.getAttr(obj + '.ty', k = True, l = False):
                tranY = mc.getAttr(sele[index] + '.ty')
            if mc.getAttr(obj + '.tz', k = True, l = False):
                tranZ = mc.getAttr(sele[index] + '.tz')
            if mc.getAttr(obj + '.rx', k = True, l = False):
                rotX = mc.getAttr(sele[index] + '.rx')
            if mc.getAttr(obj + '.ry', k = True, l = False):
                rotY = mc.getAttr(sele[index] + '.ry')
            if mc.getAttr(obj + '.rz', k = True, l = False):
                rotZ = mc.getAttr(sele[index] + '.rz')
            
            #create variables for identifiers
            r = "_R_"
            l = "_L_"
            
            #split the namespace and the object name for objects in selection
            if ":" in obj:
                nameSpace = (obj.split(":")[0] + ':')
                sansNameSpace = obj.split(":")[1]
            else:
                nameSpace = ""
                sansNameSpace = str(obj)
            #divide the object names to reuse in mirroring process with identifier variable
            name1 = sansNameSpace.split(r)[0]
            name2 = sansNameSpace.split(r)[1]
            
            #concatenate and store the name of the object that will be receiving the mirrored values
            fullName = nameSpace + ":" + name1 + l + name2
            
            #concatenate the object name with the attribute that will be receiving the mirrored values
            if mc.getAttr(obj + '.tx', k = True, l = False):
                nameTX = fullName + '.tx'
            if mc.getAttr(obj + '.ty', k = True, l = False):
                nameTY = fullName + '.ty'
            if mc.getAttr(obj + '.tz', k = True, l = False):
                nameTZ = fullName + '.tz'
            if mc.getAttr(obj + '.rx', k = True, l = False):
                nameRX = fullName + '.rx'
            if mc.getAttr(obj + '.ry', k = True, l = False):
                nameRY = fullName + '.ry'
            if mc.getAttr(obj + '.rz', k = True, l = False):
                nameRZ = fullName + '.rz'
            
            #determine the type of controller that's being assigned, in order to determine how to mirror values
            if "ForeArm" in fullName:
                multTX = -1
                multTY = 1
                multTZ = 1
                multRX = 1
                multRY = -1
                multRZ = -1
                
            elif "Wrist" in fullName:
                multRX = 1
                multRY = -1
                multRZ = -1
                
            elif "Carpal_A" in fullName:
                multTX = 1
                multTY = -1
                multTZ = 1
                multRX = -1
                multRY = 1
                multRZ = -1
            
            elif "Carpal_B" in fullName:
                multTX = 1
                multTY = 1
                multTZ = -1
                multRX = -1
                multRY = -1
                multRZ = 1
                
            elif "Carpal_C" in fullName:
                multTX = 1
                multTY = 1
                multTZ = -1
                multRX = -1
                multRY = -1
                multRZ = 1
                
            elif "Thumb" in fullName:
                multRX = -1
                multRY = 1
                multRZ = -1
                
            else:
                multRX = -1
                multRY = -1
                multRZ = 1
                 
            
            #set the mirrored values to the receiving objects
            if mc.getAttr(obj + '.tx', k = True, l = False):
                mc.setAttr(nameTX, (tranX * multTX))
            if mc.getAttr(obj + '.ty', k = True, l = False):
                mc.setAttr(nameTY, (tranY * multTY))
            if mc.getAttr(obj + '.tz', k = True, l = False):
                mc.setAttr(nameTZ, (tranZ * multTZ))
            if mc.getAttr(obj + '.rx', k = True, l = False):
                mc.setAttr(nameRX, (rotX * multRX))
            if mc.getAttr(obj + '.ry', k = True, l = False):
                mc.setAttr(nameRY, (rotY * multRY))
            if mc.getAttr(obj + '.rz', k = True, l = False):
                mc.setAttr(nameRZ, (rotZ * multRZ))
            
            
                
            index += 1