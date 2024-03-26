import sys
import os
import json
from pathlib import Path

#setup path for script to use dependencies
homeDir = Path(os.getenv('USERPROFILE', os.getenv('HOME', '')))
if not homeDir:
    print('Error: Unable to determine home directory.')
    sys.exit(1)

sansOneDrive = homeDir / 'Documents'
oneDriveDir = homeDir / 'OneDrive' / 'Documents'

if (oneDriveDir / 'maya' / 'scripts' / 'IK_Switcher').exists():
    documentsDir = oneDriveDir
else:
    documentsDir = sansOneDrive


scriptLocation = documentsDir / 'maya' / 'scripts' / 'IK_Switcher'
sys.path.append(str(scriptLocation))

import UI
import Switcher

import importlib

importlib.reload(UI)
importlib.reload(Switcher)

UI.createUI()