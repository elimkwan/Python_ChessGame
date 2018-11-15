
from board import *
from AllPiece import *
from identify import *

def nextplayer(player):
    if player == "B":
        return "W"
    else:
        return "B"
def Intro():
    for n in IntroPage:
        print(n)
    text1 = input("")
def Ending():
    for n in EndingPage:
        print(n)
    text2=input("Do you want to start the game again?(please type in 'YES' or 'NO')")
    if (text2 == "NO"):
        return True
    else:
        return False



InfoList=[0,1,2,3,4,5,6,7,8,9,10,11]#place to store the entries
"""
InfoList:
0:org1
1:org2
2:dest1
3:dest2
4:orgTileCol
5:destTileCol
6:orgCol
7:destCol
8:orgPieceWithCol
9:destPieceWithCol
10:orgPiece
11:destPiece
"""
BoardInfo=[]#check if there are any piece between the destination and starting position
player="B"
move=""
gameboard=board()
identify=identify()
gameover= False

#introduction page
Row_0="|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|"
Row_a="|                                   \        / |----  |      |----  |---|    /\  /\     |----                                   |"
Row_b="|                                    \  /\  /  |____  |      |      |   |   /  \/  \    |____                                   |"
Row_c="|                                     \/  \/   |____  |____  |____  |___|  /        \   |____                                   |"
Row_d="|                                                                                                                               |"
Row_e="|                                This is a human to human chess game, where the castling and                                    |"
Row_f="|                                pawn pass by feature do not apply here.                                                        |"
Row_g="|                                Press Enter to start the game.                                                                 |"
Row_h="|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|"
IntroPage=[Row_0,Row_a,Row_b,Row_c,Row_d,Row_e,Row_f,Row_g,Row_h]

#ending page
Row__0="|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|"
Row__a="|                                    \  /   |---|  |   |     \        /  -----  |\  |                                           |"
Row__b="|                                     \/    |   |  |   |      \  /\  /     |    | \ |                                           |"
Row__c="|                                      |    |___|  |___|       \/  \/    __|__  |  \|                                           |"
Row__d="|                                                                                                                               |"
Row__e="|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|"
EndingPage=[Row__0,Row__a,Row__b,Row__c,Row__d,Row__e]
ExitGame=False



while not (ExitGame):

    Intro()
    
    while not (gameover):
        if (player =="B"):
            print("Black turn")
        else:
            print("White turn")

        gameboard.display()
        gameboard.Input(InfoList,BoardInfo) #set coordinate
    
        while not (gameboard.valid(player,InfoList)):
            print("ERROR")
            gameboard.Input(InfoList,BoardInfo)       

        while not (identify.pieceType(InfoList,BoardInfo)):
            print("Invalid Move")
            gameboard.Input(InfoList,BoardInfo)

        gameboard.execute(InfoList)
    
        gameover= gameboard.checkWin(InfoList)

        print("----------------------------------------------------------------------------------------------------------------------------------------------------")
 
        if not gameover:
            player= nextplayer(player)
        else:
            break

    ExitGame=Ending()

print("Exited")
