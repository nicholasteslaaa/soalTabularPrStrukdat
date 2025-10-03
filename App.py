import streamlit as st
from DatabaseManager import excelManager


# === DO NOT CHANGE ANY OF THIS CODE ===
em = excelManager("dataExcel.xlsx")
options = ["Choose Action","Insert", "Edit", "Delete"]
choice = st.selectbox("Choose an action:", options)

if choice in ("Edit", "Delete"):
    nim = st.text_input("Enter targeted NIM:", key="targetNim")
    if (choice == "Delete"):
        if st.button("Delete"):
            st.success(em.deleteData(nim))


if (choice in ("Insert","Edit")):
    newNim = st.text_input("Enter New NIM:",key="newNim")
    newName = st.text_input("Enter New Name:",key="newName")

    if (choice == "Edit"):
        if st.button("Edit"):
            st.success(em.editData(str(nim),{"NIM":str(newNim),"Nama":str(newName)}))

    if (choice == "Insert"):    
        if (st.button("Insert")):
            st.success(em.insertData({"NIM":str(newNim),"Nama":str(newName)}))
        
st.table(em.getDataFrame())