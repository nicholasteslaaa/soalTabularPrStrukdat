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

    if (choice == "Edit"):
        if st.button("Edit"):
            status = em.editData(str(nim),{"NIM":str(newNim).strip(),"Nama":str(newName).strip()},saveChange)
            if (status["status"] == "success"):
                st.success(status["message"])
            elif (status["status"] == "error"):
                st.error(status["message"])

    if (choice == "Insert"):    
        if (st.button("Insert")):
            status = em.insertData({"NIM":str(newNim).strip(),"Nama":str(newName).strip()},saveChange)
            if (status["status"] == "success"):
                st.success(status["message"])
            elif (status["status"] == "error"):
                st.error(status["message"])
            
# TODO: buatkan pilihan sort data tabel berdasarkan kolom
sortOption = ["Default"].extend(em.getDataFrame().columns)
choice = st.selectbox("Sort Table By",sortOption )

if (choice == "Default"):
    st.table(em.getDataFrame())
else:
    ascending = st.checkbox("Sort Ascending", value=True)
    st.table(em.getDataFrame().sort_values(choice,ascending=ascending))

# === show the sorted table here ===
