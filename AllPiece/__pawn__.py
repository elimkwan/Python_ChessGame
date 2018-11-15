from .__piece__ import piece
from board import *

class pawn(piece):
    #error when pawn reaches the other side and can become any piece
    #error cannot capture the first time pass by chess from another side
    def __init__(self):
        return
    def BlackForward(self,InfoList,BoardInfo):
        x=piece()
        if(InfoList[3]-InfoList[1]==1):
            if (InfoList[2]==InfoList[0]):
                return True
            elif(InfoList[2]-InfoList[0]==1 or InfoList[2]-InfoList[0]==-1):
                if (str(InfoList[9]) != "----------|"):
                    return True
        elif(InfoList[3]-InfoList[1] == 2):
            if (InfoList[1] == 2 and InfoList[2]== InfoList[0]):
                if (x.CrossOver(BoardInfo)== True):
                    return True
        else:
            return False
    def WhiteForward(self,InfoList,BoardInfo):
        x=piece()
        if(InfoList[3]-InfoList[1]==-1):
            if (InfoList[2]==InfoList[0]):
                return True
            elif(InfoList[2]-InfoList[0]==1 or InfoList[2]-InfoList[0]==-1):
                if (str(InfoList[9]) != "----------|"):
                    return True
        elif(InfoList[3]-InfoList[1] == -2):
            if (InfoList[1] == 7 and InfoList[2] == InfoList[0]):
                if (x.CrossOver(BoardInfo)== True):
                    return True
        else:
            return False
