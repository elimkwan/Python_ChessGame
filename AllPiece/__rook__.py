from .__piece__ import piece
from board import *

class rook(piece):
    def __init__(self):
        return
    def move(self,InfoList,BoardInfo):
        x=piece()
        if (x.CrossOver(BoardInfo)== True):
            if (InfoList[1]==InfoList[3]):
                return True
            elif (InfoList[0]==InfoList[2]):
                return True
        else:
            return False

"""BoardInfo=['|b-----------|', '|w-----------|','|b-B_pawn----|', '|w-----------|']
x=rook()
print(x.CrossOver(BoardInfo))"""


