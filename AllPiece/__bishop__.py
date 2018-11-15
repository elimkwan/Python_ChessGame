from .__piece__ import piece
from board import *
#error for E3 F6
class bishop(piece):
    def __init__(self):
        return
    def move(self,InfoList,BoardInfo):
        x=piece()
        TempList=[]
        if (x.CrossOver(BoardInfo)== True):
            if (InfoList[4]==InfoList[5]):
                if (InfoList[1]-InfoList[3] == InfoList[2]-InfoList[0]):
                    return True
                elif (InfoList[1]-InfoList[3] == InfoList[0]-InfoList[2]):
                    return True
                elif (InfoList[2]-InfoList[0] == InfoList[3]-InfoList[1]):
                    return True
                elif (InfoList[3]-InfoList[1] == InfoList[0]-InfoList[2]):
                    return True
        else:
            return False

"""InfoList=[5, 3, 5, 6, 'w', 'b', 'B', '-', 'B_bishop--|', '----------|', '_bishop--|', '----------|']
BoardInfo=['|b-----------|', '|w-----------|']
a=bishop()
print(a.move(InfoList,BoardInfo))"""

#start from B7
#NE 2 7 -> 3 6 -> 4 5
#NW 2 7 1 6
#SE 2 7 3 8
#SW 2 7 1 8
