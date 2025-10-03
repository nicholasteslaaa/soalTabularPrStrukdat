import pandas

# RULES:
# 1. JANGAN GANTI NAMA CLASS ATAU FUNGSI YANG ADA
# 2. JANGAN DELETE FUNGSI YANG ADA
# 3. JANGAN DELETE ATAU MENAMBAH PARAMETER PADA CONSTRUCTOR ATAU FUNGSI
# 4. GANTI NAMA PARAMETER DI PERBOLEHKAN
# 5. PERATURAN DI ATAS BOLEH DILANGGAR JIKA ANDA TAU APA YANG ANDA LAKUKAN (WAJIB BISA JELASKAN)
# 6. FILE EXCEL YANG SUDAH BERANTAKAN BOLEH DI HAPUS DAN DI PERBAIKI DENGAN BACKUP 
# GOODLUCK :)


class excelManager:
    def __init__(self,filePath:str,sheetName:str=None):
        self.__filePath = filePath
        self.__sheetName = sheetName
        if sheetName != None:
            self.__data = pandas.read_excel(filePath,sheet_name=sheetName)
        else:
            self.__data = pandas.read_excel(filePath)
            
    
    def insertData(self,newData:list[str]):
        # masukan jawaban anda disini
        pass
    
    
    def deleteData(self, targetedNim:str):
        # masukan jawaban anda disini
        pass
    
    def editData(self, targetedNim:str, newData:list[str]):
        # masukan jawaban anda disini
        pass
    
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