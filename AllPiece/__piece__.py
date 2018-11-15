class piece():
    def __init__(self):
        return
    def CrossOver(self,BoardInfo):
        TempList=[]
        for item in BoardInfo:
            if (item == "|b-----------|"):
                TempList.append(True)
            elif(item == "|w-----------|"):
                TempList.append(True)
            else:
                TempList.append(False)
        if (all(TempList)== True):
            return True
        else:
            return False
