from DatabaseManager import excelManager

test_cases = {
    "insertData": {
        "newData": [
            {"testcase": {"NIM": "71231001", "Nama": "Andi"}, "expectedResult": "success"},
            {"testcase": {"NIM": "71231002", "Nama": "Budi"}, "expectedResult": "success"},
            {"testcase": {"NIM": "71231003", "Nama": "Citra"}, "expectedResult": "success"},
            {"testcase": {"NIM": "71231004", "Nama": "Dewi"}, "expectedResult": "success"},
            {"testcase": {"NIM": "71231005", "Nama": "Eka"}, "expectedResult": "success"},
            {"testcase": {"NIM": "71231006", "Nama": "Fajar"}, "expectedResult": "success"},
            {"testcase": {"NIM": "71231007", "Nama": "Gilang"}, "expectedResult": "success"},
            {"testcase": {"NIM": "71231008", "Nama": "Hana"}, "expectedResult": "success"},
            {"testcase": {"NIM": "71231009", "Nama": "Indra"}, "expectedResult": "success"},
            {"testcase": {"NIM": "71231001", "Nama": "Duplikat"}, "expectedResult": "error"}  # duplikat NIM
        ]
    },

    "deleteData": {
        "targetedNim": [
            {"testcase": "71231001", "expectedResult": "success"},
            {"testcase": "71231002", "expectedResult": "success"},
            {"testcase": "71231003", "expectedResult": "success"},
            {"testcase": "71231004", "expectedResult": "success"},
            {"testcase": "71231005", "expectedResult": "success"},
            {"testcase": "99999999", "expectedResult": "error"},
            {"testcase": "00000000", "expectedResult": "error"},
            {"testcase": "abcdef", "expectedResult": "error"},
            {"testcase": "", "expectedResult": "error"},
            {"testcase": "71190510", "expectedResult": "success"}
        ]
    },

    "editData": {
        "cases": [
            {"testcase": {"targetedNim": "71231001", "newData": {"NIM":113, "Nama": "Andi Updated"}}, "expectedResult": "success"},
            {"testcase": {"targetedNim": "71231002", "newData": {"NIM":112, "Nama": "Budi Revised"}}, "expectedResult": "success"},
            {"testcase": {"targetedNim": "71231003", "newData": {"NIM":114, "Nama": "Citra Baru"}}, "expectedResult": "success"},
            {"testcase": {"targetedNim": "71231004", "newData": {"NIM":115, "Nama": "Dewi Edited"}}, "expectedResult": "success"},
            {"testcase": {"targetedNim": "71231005", "newData": {"NIM":116, "Nama": "Eka Updated"}}, "expectedResult": "success"},
            {"testcase": {"targetedNim": "99999999", "newData": {"NIM":113, "Nama": "Ghost"}}, "expectedResult": "error"},
            {"testcase": {"targetedNim": "00000000", "newData": {"NIM":112, "Nama": "Null"}}, "expectedResult": "error"},
            {"testcase": {"targetedNim": "71231006", "newData": {"NIM":117, "Nama": "Fajar Modified"}}, "expectedResult": "success"},
            {"testcase": {"targetedNim": "71231007", "newData": {"NIM":118, "Nama": "Gilang Changed"}}, "expectedResult": "success"},
            {"testcase": {"targetedNim": "71231008", "newData": {"NIM":119, "Nama": "Hana Fixed"}}, "expectedResult": "success"}
        ]
    }
}


nilai = {"benar":0,"salah":0}

df = excelManager("dataExcel.xlsx")
for testCase in test_cases["insertData"]["newData"]:
    output = df.insertData(testCase["testcase"])["status"]
    check = df.getData("NIM",testCase["testcase"]["NIM"])
    if ((check["NIM"],check["Nama"]) == (testCase["testcase"]["NIM"],testCase["testcase"]["Nama"])):
        if (testCase["expectedResult"] == "success"):
            nilai["benar"] += 1
        else:
            nilai["salah"] += 1
    else:
        if (testCase["expectedResult"] == "error"):
            nilai["benar"] += 1
        else:
            nilai["salah"] += 1


        
for testCase in test_cases["editData"]["cases"]:
    output = df.editData(testCase["testcase"]["targetedNim"],testCase["testcase"]["newData"])
    check = df.getData("NIM",str(testCase["testcase"]["newData"]["NIM"]))
    if (check and (check["NIM"],check["Nama"]) == (str(testCase["testcase"]["newData"]["NIM"]),testCase["testcase"]["newData"]["Nama"])):
        if (testCase["expectedResult"] == "success"):
            nilai["benar"] += 1
        else:
            print(testCase, output, "<---")
            nilai["salah"] += 1
    else:
        if (testCase["expectedResult"] == "error"):
            nilai["benar"] += 1
        else:
            print(testCase, output)
            nilai["salah"] += 1

df = excelManager("dataExcel.xlsx")
for testCase in test_cases["insertData"]["newData"]:
    df.insertData(testCase["testcase"])["status"]

for testCase in test_cases["deleteData"]["targetedNim"]:
    if (testCase["expectedResult"] == "success"): beforeDelete = df.getData("NIM",testCase["testcase"]); 
    
    output = df.deleteData(testCase["testcase"])
    
    if beforeDelete and not df.getData("NIM",testCase["testcase"]):
        if(e)
        nilai["benar"] += 1
    else:
        print(testCase,output)
        nilai["salah"] += 1

print(nilai)