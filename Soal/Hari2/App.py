import streamlit as st
from DatabaseManager import excelManager


em = excelManager("dataExcel.xlsx")
options = ["Choose Action","Insert", "Edit", "Delete"]
choice = st.selectbox("Choose an action:", options)
saveChange = st.checkbox("SaveChanges",value=False)

if choice in ("Edit", "Delete"):
    nim = st.text_input("Enter targeted NIM:", key="targetNim")
    if (choice == "Delete"):
        if (sum([1 for i in nim if str(i).isalpha()]) > 0): st.error("Input nim harus angka semua")
        elif st.button("Delete"):
            if (not em.getData("NIM",nim)): st.error("nim not found")
            else:
                em.deleteData(nim,saveChange)
                if (not em.getData("NIM",nim)): st.success("deleted")
            

if (choice in ("Insert","Edit")):
    newNim = st.text_input("Enter New NIM:",key="newNim")
    newName = st.text_input("Enter New Name:",key="newName")
    newGrade = st.text_input("Enter New Grade :", key="newGrade")

    if (choice == "Edit"):
        if st.button("Edit"):
            if (sum([1 for i in newNim if str(i).isalpha()]) > 0): st.error("Input nim harus angka semua")
            elif (sum([1 for i in newName if str(i).isdigit()]) > 0): st.error("Input nama harus Alphabet semua")
            elif (sum([1 for i in newGrade if str(i).isalpha()]) > 0): st.error("Input nilai harus angka semua")
            else:
                if (not em.getData("NIM",nim)): st.success("Nim not found")
                else:
                    result = em.editData(str(nim),{"NIM":str(newNim).strip(),"Nama":str(newName).strip(),"Nilai":int(newGrade.strip())},saveChange)
                    if (em.getData("NIM",newNim)): st.success("edited")
                    else: st.error("edit failed")

    if (choice == "Insert"):    
        if (st.button("Insert")):
            if (sum([1 for i in newNim if str(i).isalpha()]) > 0): st.error("Input nim harus angka semua")
            elif (sum([1 for i in newName if str(i).isdigit()]) > 0): st.error("Input nama harus Alphabet semua")
            elif (sum([1 for i in newGrade if str(i).isalpha()]) > 0): st.error("Input nilai harus angka semua")
            else:
                if (em.getData("NIM",newNim)): st.error("Nim already exist")
                else:
                    em.insertData({"NIM":str(newNim).strip(),"Nama":str(newName).strip(),"Nilai":int(newGrade.strip())},saveChange)
                    if (em.getData("NIM",newNim)): st.success("inserted")
                    else: st.error("insert fail")                
                    
                
# TODO: buatkan pilihan sort data tabel berdasarkan kolom
sortOption = ["Default"].extend(em.getDataFrame().columns) # ini opsinya
choice = st.selectbox("Sort Table By",sortOption ) # ini selectbox nya

if (choice == "Default"):
    st.table(em.getDataFrame())
else:
    ascending = st.checkbox("Sort Ascending", value=True)
    # TODO: tampilkan tabel berdasarkan pilihan di selectbox dan gunakan checkbox apakah ascending atau tidak
    # clue: cara sort ada di modul


