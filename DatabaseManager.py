import pandas

class excelManager:
    def __init__(self,filePath:str,sheetName:str=None):
        self.__filePath = filePath
        self.__sheetName = sheetName
        if sheetName != None:
            self.__data = pandas.read_excel(filePath,sheet_name=sheetName)
        else:
            self.__data = pandas.read_excel(filePath)
            
    
    def getAllData(self) -> list[dict]:
        collumn = self.__data.columns
        value = self.__data.at
        
        result = []
        for idx in self.__data.index:
            result.append(self.getData(str(collumn[1]),str(value[idx,collumn[1]])))
        
        return result
    
    def insertData(self,newData:list[str]):
        # New row as a dictionary
        columnn = self.__data.columns
        new_row = {columnn[0]:self.__data.index[-1]+2}
        
        for col,newValue in zip(columnn[1:],newData):
            new_row.update({col:newValue})
        
        # Append row
        self.__data = pandas.concat([self.__data, pandas.DataFrame([new_row])], ignore_index=True)
        
        self.saveChanges()
    
    
    def deleteData(self, targetData:list):
        delData = self.findData(targetData)
        
        if (delData == None): return None
        
        print(delData)
        
        self.__data = self.__data.drop(delData[list(delData.keys())[0]][0])
            
        self.saveChanges()
        print("Deleted")
            
    
    def editData(self, oldData:list[str], newData:list[str]):
        targetData = self.findData(oldData)
        
        if (targetData == None): return None
        
        for old,new in zip(oldData,newData):
            # print(targetData[old],new)
            self.__data.at[targetData[old][0],targetData[old][1]] = str(self.__data.at[targetData[old][0],targetData[old][1]])
            self.__data.at[targetData[old][0],targetData[old][1]] = str(new)
        
        self.saveChanges()
        
        print("Edited")
        
    def saveChanges(self):
        # self.__data["Status"] = "Active"
        if (self.__sheetName == None):
            self.__data.to_excel(self.__filePath, index=False)
        else:
            self.__data.to_excel(self.__filePath, sheet_name=self.__sheetName, index=False)                    
        return
        
    
    def findData(self, targetData:list[str]):
        dataFound = dict()
        for idx in self.__data.index:
            for col in self.__data.columns:
                if (str(self.__data.at[idx,col]) in targetData):
                    dataFound.update({str(self.__data.at[idx,col]) : [idx,col]})
            
            # if (len(dataFound) > 0): return dataFound
            if (set(dataFound.keys()) == set(targetData)): return dataFound
                
        return None
                    
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
                return resultDict
        
        return None
    
    def getDataFrame(self):
        return pandas.DataFrame(self.getAllData())