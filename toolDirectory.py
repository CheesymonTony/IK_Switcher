
import maya.cmds as mc

class ToolDict:
    tools = {
        0: {'id': 'AdRaFo', 'controller': 'Ctrl__AdRaFo__Main_01'},
        1: {'id': 'ArNaRe', 'controller': 'Ctrl__ArNaRe__Main_01'},
        2: {'id': 'BackTC', 'controller': 'Ctrl__BackTC__Main_01'},
        3: {'id': 'BBReRe', 'controller': 'Ctrl__BBReRe__Main_01'},
        4: {'id': 'BrAdFo', 'controller': 'Ctrl__BrAdFo__Main_01'},
        5: {'id': 'CriHem', 'controller': 'Ctrl__CriHem__Main_01'},
        6: {'id': 'DebFor', 'controller': 'Ctrl__DebFor__Main_01'},
        7: {'id': 'GauzeS', 'controller': 'Ctrl__GauzeS__Main_01'},
        8: {'id': 'GosRet', 'controller': 'Ctrl__GosRet__Main_01'},
        9: {'id': 'HaMoHe', 'controller': 'Ctrl__HaMoHe__Main_01'},
        10: {'id': 'KelHem', 'controller': 'Ctrl__KelHem__Main_01'},
        11: {'id': 'MayoND', 'controller': 'Ctrl__MayoND__Main_01'},
        12: {'id': 'MaySci', 'controller': 'Ctrl__MaySci__Main_01'},
        13: {'id': 'MayoSS', 'controller': 'Ctrl__MayoSS__Main_01'},
        14: {'id': 'MetSci', 'controller': 'Ctrl__MetSci__Main_01'},
        15: {'id': 'OlHeND', 'controller': 'Ctrl__OlHeND__Main_01'},
        16: {'id': 'PaHaRe', 'controller': 'Ctrl__PaHaRe__Main_01'},
        17: {'id': 'RoCaHe', 'controller': 'Ctrl__RoCaHe__Main_01'},
        18: {'id': 'Scalpl', 'controller': 'Ctrl__Scalpl__Main_01'},
        19: {'id': 'SennRe', 'controller': 'Ctrl__SennRe__Main_01'},
        20: {'id': 'SpaHok', 'controller': 'Ctrl__SpaHok__Main_01'},
        21: {'id': 'SuTNdl', 'controller': 'Ctrl__SuTNdl__Main_01'}
    }

    @staticmethod
    def get_controller(index, side=None):
        if side not in ['Right', 'Left', None]:
            raise ValueError("Side argument must be 'R', 'L', or None")
        
        controller_name = ToolDict.tools[index]['controller']
        if side == 'Right':
            controller_name = controller_name.replace('Ctrl__', 'Ctrl__R_')
        elif side == 'Left':
            controller_name = controller_name.replace('Ctrl__', 'Ctrl__L_')

        return controller_name

    @staticmethod
    def get_id(index):
        return ToolDict.tools[index]['id']