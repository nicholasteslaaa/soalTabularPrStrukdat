import pandas as pd

class minimarket:
    def __init__(self):
        self.df = pd.read_excel("materiVideo/dataBarangMinimarket.xlsx")
        
    def insertData(self,newData:dict):
        collumn = self.df.columns
        new_row = {}
        
        checkIfExist = self.getData("ID",newData["ID"])
        if (checkIfExist): return {"status":"error","message":"Nim already exist"}
            
        for newValue in newData:
            for col in collumn:
                if (str(newValue).lower() == str(col).lower()):
                    new_row.update({col:newData[newValue]})
                    break
        
        # Append row
        self.df = pd.concat([self.df, pd.DataFrame([new_row])], ignore_index=True)
        
        return {"status":"success","message":"inserted"}
        
        
    def deleteData(self,targetedNim:str):
        target = self.getData("NIM",targetedNim)
        
        if (not target): return {"status":"error","message":"Nim Not Found"}
        
        self.df.drop(target["Row"], inplace=True)
        
        return {"status":"success","message":"Deleted"}
                
        
    def editData(self,targetedId:str, newData:dict) -> dict:
        targetData = self.getData("ID",targetedId)
        checkNewNim = self.getData("ID",newData["ID"])
        
        if (not targetData): return {"status":"error","message":"Nim Not Found"}
        if (checkNewNim): return {"status":"error","message":f"Nim {newData['NIM']} already exist"}

        for inputKey in newData:
            for colName in self.df.columns:
                if (str(inputKey).lower() == str(colName).lower()):
                    self.df.at[targetData["Row"],colName] = newData[inputKey]
                    break
        
        return {"status":"success","message":"edited"}

    def getData(self,colName:str, data:str) -> dict:
        collumn = self.df.columns # mendapatkan list dari nama kolom tabel
        
        # cari index dari nama kolom dan menjaganya dari typo atau spasi berlebih
        collumnIndex = [i for i in range(len(collumn)) if (collumn[i].lower().strip() == colName.lower().strip())] 
        
        # validasi jika input kolom tidak ada pada data excel
        if (len(collumnIndex) != 1): return None
        
        # nama kolom yang sudah pasti benar dan ada
        colName = collumn[collumnIndex[0]]
        
        
        resultDict = dict() # tempat untuk hasil
        
        for i in self.df.index: # perulangan ke baris tabel
            cellData = str(self.df.at[i,colName]) # isi tabel yand dijadikan str
            if (cellData == data): # jika data cell sama dengan data input
                for col in collumn: # perulangan ke nama-nama kolom
                    resultDict.update({str(col):str(self.df.at[i,col])}) # masukan data {namaKolom : data pada cell} ke resultDict
                resultDict.update({"Row":i}) # tambahkan row nya pada resultDict
                return resultDict # kembalikan resultDict
        
        return None



m = minimarket()
m.insertData({'ID': '101', 'Nama': 'Saori Saus Tiram', 'Perusahaan Asal': 'Wings', 'Kategori': 'Bumbu Dapur', 'Harga': 40020, 'Row': 0})
# print(getData("ID","101"))
m.df.sort_values(by="Harga",ascending=False)
print(m.df.head(200))