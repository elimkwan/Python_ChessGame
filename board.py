class board():
    "define game board"
    whitespace="|w-----------|"
    blackspace="|b-----------|"
    Row0=["0","|------A-----|","|------B-----|","|------C-----|","|------D-----|","|------E-----|","|------F-----|","|------G-----|","|------H-----|"]
    Row1=["1","|w-B_rook----|","|b-B_knight--|","|w-B_bishop--|","|b-B_queen---|","|w-B_king----|","|b-B_bishop--|","|w-B_knight--|","|b-B_rook----|"]
    Row2=["2","|b-B_pawn----|","|w-B_pawn----|","|b-B_pawn----|","|w-B_pawn----|","|b-B_pawn----|","|w-B_pawn----|","|b-B_pawn----|","|w-B_pawn----|"]
    Row3=["3",whitespace,blackspace,whitespace,blackspace,whitespace,blackspace,whitespace,blackspace]
    Row4=["4",blackspace,whitespace,blackspace,whitespace,blackspace,whitespace,blackspace,whitespace]
    Row5=["5",whitespace,blackspace,whitespace,blackspace,whitespace,blackspace,whitespace,blackspace]
    Row6=["6",blackspace,whitespace,blackspace,whitespace,blackspace,whitespace,blackspace,whitespace]
    Row7=["7","|w-W_pawn----|","|b-W_pawn----|","|w-W_pawn----|","|b-W_pawn----|","|w-W_pawn----|","|b-W_pawn----|","|w-W_pawn----|","|b-W_pawn----|"]
    Row8=["8","|b-W_rook----|","|w-W_knight--|","|b-W_bishop--|","|w-W_queen---|","|b-W_king----|","|w-W_bishop--|","|b-W_knight--|","|w-W_rook----|"]
    Board=[Row0,Row1,Row2,Row3,Row4,Row5,Row6,Row7,Row8]
    orgPieceWithColWithTil=""
    destPieceWithColWithTil=""
    def __init__ (self):
        return
    def display(self):
        for n in self.Board:
            print(n)
        return
    def Input(self,InfoList,BoardInfo):
        self.org=input("Enter starting position")
        self.dest=input("Enter destination")
        Column={"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8}
        InfoList[0]=int(Column.get(self.org[0])) #*0 1 is Row;2 is Column
        InfoList[1]=int(self.org[1])#*1
        InfoList[2]=int(Column.get(self.dest[0]))#*2
        InfoList[3]=int(self.dest[1])#*3
        InfoList[4]= self.Board[InfoList[1]][InfoList[0]][1]#*4 get til colour
        InfoList[5]=self.Board[InfoList[3]][InfoList[2]][1]#*5
        InfoList[6]= self.Board[InfoList[1]][InfoList[0]][3]#*6 get colour of origin piece
        InfoList[7] = self.Board[InfoList[3]][InfoList[2]][3]#*7 get colour of destination

        self.orgPieceWithColWithTil=self.Board[InfoList[1]][InfoList[0]]
        self.destPieceWithColWithTil=self.Board[InfoList[3]][InfoList[2]]
        
        InfoList[8]=self.Board[InfoList[1]][InfoList[0]].replace("|b-","",1).replace("|w-","",1)#getting piece with known colour, but remove Til Colour
        InfoList[9]=self.Board[InfoList[3]][InfoList[2]].replace("|b-","",1).replace("|w-","",1)

        InfoList[10]=self.Board[InfoList[1]][InfoList[0]].replace("B","",1).replace("W","",1).replace("|b-","",1).replace("|w-","",1)
        InfoList[11]=self.Board[InfoList[3]][InfoList[2]].replace("B","",1).replace("W","",1).replace("|b-","",1).replace("|w-","",1)#get piece

        if (len(BoardInfo)>0):
            BoardInfo.pop()

        a=1
            
        if (InfoList[1]==InfoList[3] and InfoList[0] != InfoList[2]):
            if (InfoList[2]>InfoList[0]):
                for x in range (abs(InfoList[2]-InfoList[0])-1):#for horizontal move, same row
                    x=InfoList[0]+a
                    BoardInfo.append(self.Board[InfoList[1]][x]) 
                    a=a+1
            elif (InfoList[2]<InfoList[0]):
                for x in range (abs(InfoList[2]-InfoList[0])-1):#for horizontal move
                    x=InfoList[0]-a
                    BoardInfo.append(self.Board[InfoList[1]][x]) 
                    a=a+1                
        elif (InfoList[0]==InfoList[2] and InfoList[1]!=InfoList[3]):
            if (InfoList[3]>InfoList[1]):
                for y in range (abs(InfoList[3]-InfoList[1])-1):#for vertical move
                    y=InfoList[1]+a
                    BoardInfo.append(self.Board[y][InfoList[0]]) 
                    a=a+1
            if (InfoList[3]<InfoList[1]):
                for y in range (abs(InfoList[3]-InfoList[1])-1):#for vertical move
                    y=InfoList[1]-a
                    BoardInfo.append(self.Board[y][InfoList[0]]) 
                    a=a+1
        else:#for slant move
            if(InfoList[1]>InfoList[3] and InfoList[2]>InfoList[0]): #NE dir
                for z in range (abs (InfoList[2]-InfoList[0]) -1):
                    u=InfoList[0]+a
                    v=InfoList[1]-a
                    BoardInfo.append(self.Board[v][u])
                    a=a+1
            elif (InfoList[1]>InfoList[3] and InfoList[0]>InfoList[2]): #NW dir
                for z in range (abs (InfoList[2]-InfoList[0]) -1):
                    u=InfoList[0]-a #column
                    v=InfoList[1]-a #row
                    BoardInfo.append(self.Board[v][u])
                    a=a+1
            elif (InfoList[2]>InfoList[0] and InfoList[3]>InfoList[1]): #SE dir
                for z in range (abs (InfoList[2]-InfoList[0]) -1):
                    u=InfoList[0]+1
                    v=InfoList[1]+1
                    BoardInfo.append(self.Board[v][u])
                    a=a+1
            elif (InfoList[3]>InfoList[1] and InfoList[2]<InfoList[0]):#SW
                for z in range (abs (InfoList[2]-InfoList[0]) -1):
                    u=InfoList[0]-1
                    v=InfoList[1]+1
                    BoardInfo.append(self.Board[v][u])
                    a=a+1
            
#B7 E4: 2 7 5 4
#want C6,D5: 3 6 4 5 
#C7 A5: 3 7 1 5
#C2 A4: 3 2 1 4
                   
        
    def valid(self,player,InfoList):
        if (player != InfoList[6]): #check running own colour
            return False
        elif (InfoList[6]==InfoList[7]): #check running onto own piece
            return False
        else:
            return True
        #check piece property
        #check order of piece
    def execute(self,InfoList):
        if (InfoList[5]=="b"):
            self.Board[InfoList[3]][InfoList[2]]=self.orgPieceWithColWithTil.replace("|w","|b",1).replace("|b","|b",1)#new coordinate=old coordinate
        else:
            self.Board[InfoList[3]][InfoList[2]]=self.orgPieceWithColWithTil.replace("|b","|w",1).replace("|w","|w",1)#new coordinate=old coordinate
        if (InfoList[4]=="b"):
            self.Board[InfoList[1]][InfoList[0]]=self.blackspace#things on old coordinate become space
        else:
            self.Board[InfoList[1]][InfoList[0]]=self.whitespace#things on old coordinate become space
        return True
    def checkWin(self, InfoList):#check win or not
        if (InfoList[11]=="_king----|"):
            print("You Win")
            return True
        else:
            return False

