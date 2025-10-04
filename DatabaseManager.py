import pandas

# RULES:
# 1. JANGAN GANTI NAMA CLASS ATAU FUNGSI YANG ADA
# 2. JANGAN DELETE FUNGSI YANG ADA
# 3. JANGAN DELETE ATAU MENAMBAH PARAMETER PADA CONSTRUCTOR ATAU FUNGSI
# 4. GANTI NAMA PARAMETER DI PERBOLEHKAN
# 5. LARANGAN DI ATAS BOLEH DILANGGAR JIKA ANDA TAU APA YANG ANDA LAKUKAN (WAJIB BISA JELASKAN)
# GOODLUCK :)

class excelManager:
    def __init__(self,filePath:str,sheetName:str="Sheet1"):
        self.__data = pandas.read_excel(filePath,sheet_name=sheetName)
            
    
    def insertData(self,newData:dict): 
        columnn = self.__data.columns
        new_row = {}
        
        checkIfExist = self.getData("NIM",newData["NIM"])
        if (checkIfExist): return {"status":"error","message":"Nim already exist"}
            
        for newValue in newData:
            for col in columnn:
                if (str(newValue).lower() == str(col).lower()):
                    new_row.update({col:newData[newValue]})
                    break
        
        # Append row
        self.__data = pandas.concat([self.__data, pandas.DataFrame([new_row])], ignore_index=True)
        
        return {"status":"success","message":"inserted"}
    
    
    def deleteData(self, targetedNim:str):
        target = self.getData("NIM",targetedNim)
        
        if (not target): return {"status":"error","message":"Nim Not Found"}
        
        self.__data.drop(target["Row"], inplace=True)
        
        return {"status":"success","message":"Deleted"}
            
    
    def editData(self, targetedNim:str, newData:dict) -> dict:
        targetData = self.getData("NIM",targetedNim)
        checkNewNim = self.getData("NIM",newData["NIM"])
        
        if (not targetData): return {"status":"error","message":"Nim Not Found"}
        if (checkNewNim): return {"status":"error","message":f"Nim {newData['NIM']} already exist"}
    
        for inputKey in newData:
            for colName in self.__data.columns:
                if (str(inputKey).lower() == str(colName).lower()):
                    self.__data.at[targetData["Row"],colName] = newData[inputKey]
                    break
        
        return {"status":"success","message":"edited"}
    
                    
    def getData(self, colName:str, data:str) -> dict:
        collumn = self.__data.columns # mendapatkan list dari nama kolom tabel
        
        # cari index dari nama kolom dan menjaganya dari typo atau spasi berlebih
        collumnIndex = [i for i in range(len(collumn)) if (collumn[i].lower().strip() == colName.lower().strip())] 
        
        # validasi jika input kolom tidak ada pada data excel
        if (len(collumnIndex) != 1): return None
        
        # nama kolom yang sudah pasti benar dan ada
        colName = collumn[collumnIndex[0]]
        
        
        resultDict = dict() # tempat untuk hasil
        
        for i in self.__data.index: # perulangan ke baris tabel
            cellData = str(self.__data.at[i,colName]) # isi tabel yand dijadikan str
            if (cellData == data): # jika data cell sama dengan data input
                for col in collumn: # perulangan ke nama-nama kolom
                    resultDict.update({str(col):str(self.__data.at[i,col])}) # masukan data {namaKolom : data pada cell} ke resultDict
                resultDict.update({"Row":i}) # tambahkan row nya pada resultDict
                return resultDict # kembalikan resultDict
        
        return None
    
    def getDataFrame(self):
        return self.__data