from .__piece__ import piece
from board import *

class king(piece):
    #error when checkmate
    #castle function not yet built
    def __init__(self):
        return
    def move(self,InfoList):
        x=piece()
        if (abs(InfoList[1]-InfoList[3])==1):
            return True
        elif (abs(InfoList[0]-InfoList[2])==1):
            return True
        else:
            return False

