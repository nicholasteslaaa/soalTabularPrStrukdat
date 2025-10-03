import pandas

# RULES:
# 1. JANGAN GANTI NAMA CLASS ATAU FUNGSI YANG ADA
# 2. JANGAN DELETE FUNGSI YANG ADA
# 3. JANGAN DELETE ATAU MENAMBAH PARAMETER PADA CONSTRUCTOR ATAU FUNGSI
# 4. GANTI NAMA PARAMETER DI PERBOLEHKAN
# 5. PERATURAN DI ATAS BOLEH DILANGGAR JIKA ANDA TAU APA YANG ANDA LAKUKAN (WAJIB BISA JELASKAN)
# 6. FILE EXCEL YANG SUDAH BERANTAKAN BOLEH DI HAPUS DAN DI PERBAIKI DENGAN BACKUP 
# 7. AI FRIENDLY (WAJIB BISA JELASKAN)
# GOODLUCK :)

class excelManager:
    def __init__(self,filePath:str,sheetName:str="Sheet1"):
        self.__filePath = filePath
        self.__sheetName = sheetName
        self.__data = pandas.read_excel(filePath,sheet_name=sheetName)
            
    
    def insertData(self,newData:dict):
        columnn = self.__data.columns
        new_row = {}
        
        checkIfExist = self.getData("NIM",newData["NIM"])
        if (checkIfExist): return "Nim Already Exist"
        
        # for col,newValue in zip(columnn,newData):
        #     new_row.update({col:newValue})
            
        for newValue in newData:
            for col in columnn:
                print(newValue,col)
                if (newValue == col):
                    new_row.update({col:newData[newValue]})
                    break
        
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
            
    
    def editData(self, targetedNim:str, newData:dict):
        targetData = self.getData("NIM",targetedNim)
        
        
        if (not targetData): return "Nim Not Found"
        
        # for colName,inputKey in zip(self.__data.columns,newData):
        #     if (colName == inputKey):
        #         self.__data.at[targetData["Row"],colName] = newData[inputKey]
        
        for inputKey in newData:
            for colName in self.__data.columns:
                print(inputKey,colName)
                if (inputKey == colName):
                    self.__data.at[targetData["Row"],colName] = newData[inputKey]
                    break
            
        self.saveChanges()
        
        return "Edited"
    
    def saveChanges(self):
        self.__data.to_excel(self.__filePath, sheet_name=self.__sheetName, index=False)                    
        return
        
 
                    
    def getData(self, colName:str, data:str) -> dict:
        collumn = self.__data.columns
        collumnIndex = [i for i in range(len(collumn)) if (collumn[i].lower().strip() == colName.lower().strip())]
        print(collumnIndex)
        
        # validasi jika input kolom tidak ada pada data excel
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
    
if __name__ == "__main__":
    excelReader = excelManager("dataExcel.xlsx")
    # excelReader.editData("71231014",{"NIM":3,"Nama":"3"})
    excelReader.insertData({"NIM":7,"Nama":"7"})
    print(excelReader.getDataFrame().head(100))
    