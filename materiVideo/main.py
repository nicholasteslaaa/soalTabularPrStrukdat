import pandas as pd
from datetime import datetime

class excelManager:
    def __init__(self,path:str,sheetName:str = "Sheet1",primaryKey = "ID"):
        self.path = path
        self.sheetName = sheetName
        self.primaryKey = primaryKey
        self.df = pd.read_excel(path)
        
    def insertData(self,newData:dict):
        collumn = self.df.columns
        new_row = {}
        
        checkIfExist = self.getData(self.primaryKey,newData[self.primaryKey])
        if (checkIfExist): return {"status":"error","message":"Nim already exist"}
            
        for newValue in newData:
            for col in collumn:
                if (str(newValue).lower() == str(col).lower()):
                    new_row.update({col:newData[newValue]})
                    break
        
        # Append row
        self.df = pd.concat([self.df, pd.DataFrame([new_row])], ignore_index=True)
        
        return {"status":"success","message":"inserted"}
        
        
    def deleteData(self,targetedID:str):
        target = self.getData(self.primaryKey,targetedID)
        
        if (not target): return {"status":"error","message":"Nim Not Found"}
        
        self.df.drop(target["Row"], inplace=True)
        
        return {"status":"success","message":"Deleted"}
                
        
    def editData(self,targetedId:str, newData:dict) -> dict:
        targetData = self.getData(self.primaryKey,targetedId)
        
        if (not targetData): return {"status":"error","message":"Nim Not Found"}

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
    
    def saveChange(self):
        self.df.to_excel(self.path, sheet_name=self.sheetName , index=False)


dataBarang = excelManager("materiVideo/dataBarangMinimarket.xlsx")
dataPenjualan = excelManager("materiVideo/dataPenjualanMinimarket.xlsx",primaryKey="IDPejualan")

def jual(idBarang,jumlahBarang):
    data = dataBarang.getData("ID",idBarang)
    print(data)
    
    if (data == None): return f"ID: {idBarang} tidak di temukan"
    if (int(data["Stok"])-jumlahBarang < 0): return "jumlah barang melebihi stok barang"
        
    dataPenjualan.insertData({"IDPejualan":str(datetime.now().strftime("%Y%m%d%H%M%S%f")),"ID" : data["ID"],"Kategori":data["Kategori"],"Harga":data["Harga"],"Waktu":datetime.now(),"Jumlah barang":jumlahBarang,"Total":float(data["Harga"])*jumlahBarang})
    dataPenjualan.saveChange()
    dataBarang.editData(idBarang,{"ID":data["ID"],"Nama":data["Nama"],"Perusahaan Asal":data["Perusahaan Asal"],"Kategori":data["Kategori"],"Harga":data["Harga"],"Stok":int(data["Stok"])-jumlahBarang})

def restock():
    pass

def barangPalingLaku():
    pass


jual("8885193814391",139)
print(dataPenjualan.df.head(10)) 
print(dataBarang.df.head())