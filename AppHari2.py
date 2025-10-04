import streamlit as st
from DatabaseManager import excelManager


# === DO NOT CHANGE ANY OF THIS CODE ===
em = excelManager("dataExcel.xlsx")
options = ["Choose Action","Insert", "Edit", "Delete"]
choice = st.selectbox("Choose an action:", options)
saveChange = st.checkbox("SaveChanges",value=False)

if choice in ("Edit", "Delete"):
    nim = st.text_input("Enter targeted NIM:", key="targetNim")
    if (choice == "Delete"):
        if st.button("Delete"):
            status = em.deleteData(nim,saveChange)
            if (status["status"] == "success"):
                st.success(status["message"])
            elif (status["status"] == "error"):
                st.error(status["message"])


if (choice in ("Insert","Edit")):
    newNim = st.text_input("Enter New NIM:",key="newNim")
    newName = st.text_input("Enter New Name:",key="newName")
    newGrade = st.text_input("Enter New Grade :", key="targetNim")

    if (choice == "Edit"):
        if st.button("Edit"):
            if (sum([1 for i in newNim if str(i).isalpha()]) > 0): st.error("Input nim harus angka semua")
            elif (sum([1 for i in newName if str(i).isdigit()]) > 0): st.error("Input nama harus Alphabet semua")
            elif (sum([1 for i in newGrade if str(i).isalpha()]) > 0): st.error("Input nilai harus angka semua")
            else:
                status = em.editData(str(nim),{"NIM":str(newNim).strip(),"Nama":str(newName).strip(),"Nilai":int(newGrade.strip())},saveChange)
                if (status["status"] == "success"):
                    st.success(status["message"])
                elif (status["status"] == "error"):
                    st.error(status["message"])

    if (choice == "Insert"):    
        if (st.button("Insert")):
            if (sum([1 for i in newNim if str(i).isalpha()]) > 0): st.error("Input nim harus angka semua")
            elif (sum([1 for i in newName if str(i).isdigit()]) > 0): st.error("Input nama harus Alphabet semua")
            elif (sum([1 for i in newGrade if str(i).isalpha()]) > 0): st.error("Input nilai harus angka semua")
            else:
                status = em.insertData({"NIM":str(newNim).strip(),"Nama":str(newName).strip(),"Nilai":int(newGrade.strip())},saveChange)
                if (status["status"] == "success"):
                    st.success(status["message"])
                elif (status["status"] == "error"):
                    st.error(status["message"])
            
# TODO: buatkan pilihan sort data tabel berdasarkan kolom
sortOption = ["Default"]
sortOption.extend(em.getDataFrame().columns)

choice = st.selectbox("Sort Table By",sortOption )
if (choice == "Default"):
    st.table(em.getDataFrame())
else:
    ascending = st.checkbox("Sort Ascending", value=True)
    st.table(em.getDataFrame().sort_values(choice,ascending=ascending))
