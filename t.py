from DatabaseManager import excelManager

em = excelManager("dataExcel.xlsx")
# print(em.deleteData(["71190510.0","Joshua Benevan Wisnuwardhana"]))
print(em.getAllData())

# print("71190510.0" in["71190510.0",] )

# dct = em.findData(["71190510.0","Joshua Benevan Wisnuwardhana"])
# print(dct)
# em.deleteData(["71190510.0","Joshua Benevan Wisnuwardhana"])

print(em.editData(["71241071.0","Fidelo"],["71241071","Fidel"]))
# print(em.getAllData())
