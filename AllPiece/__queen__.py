from .__piece__ import piece
from board import *

class queen(piece):
    def __init__(self):
        return
    def SlantMove(self,BoardInfo,InfoList):
        x=piece()
        TempList=[]
        if (x.CrossOver(BoardInfo)== True):
            if (InfoList[4]==InfoList[5]):
                for item in BoardInfo:
                    if (item[1] == InfoList[4]):
                        TempList.append(True)
                    else:
                        TempList.append(False)
                if (all(TempList) == True):
                    return True
        else:
            return False
    def move(self,BoardInfo,InfoList):
        x=piece()
        if (x.CrossOver(BoardInfo)== True):
            if (InfoList[1]==InfoList[3]):
                return True
            elif (InfoList[0]==InfoList[2]):
                return True
        else:
            return False
        
