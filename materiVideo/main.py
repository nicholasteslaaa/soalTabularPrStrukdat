import pandas as pd
from datetime import datetime
import numpy as np

class excelManager:
    def __init__(self,path:str,sheetName:str = "Sheet1",primaryKey = "ID"):
        self.path = path
        self.sheetName = sheetName
        self.df = pd.read_excel(path)
        self.primaryKey = None
        for i in self.df.columns:
            if (i.strip().lower() == primaryKey.strip().lower()):
                self.primaryKey = i
            
    def insertData(self,newData:dict):
        new_row = {}
        checkIfExist = self.getData(self.primaryKey,newData[self.primaryKey])
        
        if (checkIfExist): return None
        for newValue in newData:
            for col in self.df.columns:
                if (str(newValue).lower() == str(col).lower()):
                    new_row.update({col:newData[newValue]})
                    break
        # Append row
        self.df = pd.concat([self.df, pd.DataFrame([new_row])], ignore_index=True)        
    
    def deleteData(self,targetedID):
        isExist = self.getData(self.primaryKey,targetedID)
        if (not isExist): return None
        
        self.df.drop(isExist["row"], inplace=True)
        
    def editData(self,targetedId:str, newData:dict) -> dict:
        isExist = self.getData(self.primaryKey,targetedId)
        if (not isExist): return None
        
        for key in newData:
            self.df.at[isExist["row"],key] = newData[key]

    def getData(self,colName:str, data) -> dict:
        data = str(data)
        for row in self.df.index:
            temp = {}
            for col in self.df.columns:
                temp.update({col:self.df.at[row,col]})
            temp.update({"row":row})
            if (str(temp[colName]).lower().strip() == data):
                return {"result":temp,"row":row}
            
    
    def saveChange(self):
        self.df.to_excel(self.path, sheet_name=self.sheetName, index=False)


dataBarang = excelManager("materiVideo/dataBarangMinimarket.xlsx",primaryKey="ID")
dataPenjualan = excelManager("materiVideo/dataPenjualanMinimarket.xlsx",primaryKey="IDPejualan")

def jual(idBarang,jumlahBarang):
    data = dataBarang.getData("ID",idBarang)["result"]

    if (data == None): return f"ID: {idBarang} tidak di temukan"
    if (int(data["Stok"])-jumlahBarang < 0): return "jumlah barang melebihi stok barang"

    dataPenjualan.insertData({"IDPejualan":str(datetime.now().strftime("%Y%m%d%H%M%S%f")),"ID" : data["ID"],"Kategori":data["Kategori"],"Harga":data["Harga"],"Waktu":datetime.now(),"Jumlah barang":jumlahBarang,"Total":float(data["Harga"])*jumlahBarang})
    dataPenjualan.saveChange()
    dataBarang.editData(idBarang,{"ID":data["ID"],"Nama":data["Nama"],"Perusahaan Asal":data["Perusahaan Asal"],"Kategori":data["Kategori"],"Harga":data["Harga"],"Stok":data["Stok"]-jumlahBarang})

def restock():
    pass

def barangPalingLaku():
    pass


jual(8885193814391,139)
print(dataPenjualan.df.head(10)) 
print(dataBarang.df.head())