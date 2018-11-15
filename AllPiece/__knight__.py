from .__piece__ import piece
from board import *

class knight(piece):
    def __init__(self):
        return
    def move(self,InfoList):
        if (InfoList[2]-InfoList[0]== -1):
            InfoList[3]-InfoList[1]== 2 or -2
            return True
        elif (InfoList[2]-InfoList[0]== 1):
            InfoList[3]-InfoList[1]== 2 or -2
            return True
        elif (InfoList[2]-InfoList[0]== -2):
            InfoList[3]-InfoList[1]== 1 or -1
            return True
        elif (InfoList[2]-InfoList[0]== 2):
            InfoList[3]-InfoList[1]== 1 or -1
            return True
        else:
            return False
