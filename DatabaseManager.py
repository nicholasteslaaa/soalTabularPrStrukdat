import pandas

class excelManager:
    def __init__(self,filePath:str,sheetName:str=None):
        self.__filePath = filePath
        self.__sheetName = sheetName
        if sheetName != None:
            self.__data = pandas.read_excel(filePath,sheet_name=sheetName)
        else:
            self.__data = pandas.read_excel(filePath)
            
    
    def insertData(self,newData:list[str]):
        columnn = self.__data.columns
        new_row = {}
        
        checkIfExist = self.getData("NIM",newData[0])
        if (checkIfExist): return "Nim Already Exist"
        
        for col,newValue in zip(columnn,newData):
            new_row.update({col:newValue})
        
        # Append row
        self.__data = pandas.concat([self.__data, pandas.DataFrame([new_row])], ignore_index=True)
        
        self.saveChanges()
        
        return "Inserted"
    
    
    def deleteData(self, targetedNim:str):
        target = self.getData("NIM",targetedNim)
        
        if (not target): return "Nim Not Found"
        
        self.__data.drop(target["Row"], inplace=True)
        self.saveChanges()
        
        return "Deleted"
            
    
    def editData(self, targetedNim:str, newData:list[str]):
        targetData = self.getData("NIM",targetedNim)
        
        if (not targetData): return "Nim Not Found"
        
        for colName,newValue in zip(self.__data.columns,newData):
            self.__data.at[targetData["Row"],colName] = newValue
        
        self.saveChanges()
        
        return "Edited"
    
    def saveChanges(self):
        if (self.__sheetName == None):
            self.__data.to_excel(self.__filePath, index=False)
        else:
            self.__data.to_excel(self.__filePath, sheet_name=self.__sheetName, index=False)                    
        return
        
 
                    
    def getData(self, colName:str, data:str) -> dict:
        collumn = self.__data.columns
        collumnIndex = [i for i in range(len(collumn)) if (collumn[i].lower().strip() == colName.lower().strip())]
        
        # validasi jika input tidak ada pada data excel
        if (len(collumnIndex) != 1): return None
        
        colName = collumn[collumnIndex[0]]
        
        resultDict = dict()
        for i in self.__data.index:
            cellData = str(self.__data.at[i,colName])
            if (cellData == data):
                for col in collumn:
                    resultDict.update({str(col):str(self.__data.at[i,col])})
                resultDict.update({"Row":i})
                return resultDict
        
        return None
    
    def getDataFrame(self):
        return self.__data