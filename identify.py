from AllPiece import *

class identify(__pawn__.pawn,__rook__.rook,__bishop__.bishop,__knight__.knight,__queen__.queen,__king__.king):
    def __init__(self):
        return
    def pieceType(self,InfoList,BoardInfo):
        if (str(InfoList[8]) == "B_pawn----|"):
            bpawn=__pawn__.pawn()
            if (bpawn.BlackForward(InfoList,BoardInfo) == True):
                return True
            else:
                return False
        elif (str(InfoList[8]) == "W_pawn----|"):
            wpawn=__pawn__.pawn()
            if (wpawn.WhiteForward(InfoList,BoardInfo) == True):
                return True
            else:
                return False
        elif (str (InfoList[10])== "_rook----|"):
            rook=__rook__.rook()
            if (rook.move(InfoList,BoardInfo) == True):
                return True
            else:
                return False
        elif (str(InfoList[10])== "_bishop--|"):
            bishop=__bishop__.bishop()
            if (bishop.move(InfoList,BoardInfo)== True):
                return True
            else:
                return False
        elif (str(InfoList[10]) == "_knight--|"):
            knight=__knight__.knight()
            if (knight.move(InfoList) == True):
                return True
            else:
                return False
        elif (str(InfoList[10]) == "_queen---|"):
            queen=__queen__.queen()
            if (queen.move(BoardInfo,InfoList) == True):
                return True
            elif (queen.SlantMove(BoardInfo,InfoList) == True):
                return True
            else:
                return False        
        elif (str(InfoList[10]) == "_king----|"):
            king=__king__.king()
            if (king.move(InfoList) == True):
                return True
            else:
                return False
        else:
            return False
"""
BoardInfo=['|w-----------|', '|b-----------|', '|b-----------|']
InfoList=[1, 1, 1, 3, 'w', 'w', 'B', '-', 'B_rook----|', '----------|', '_rook----|', '----------|']
x=identify()
print(x.pieceType(InfoList))
"""
