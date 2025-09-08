import streamlit as st
from DatabaseManager import excelManager



# # Title
# st.title("Hello Streamlit 👋")

# # Text
# st.write("This is my first Streamlit app!")
em = excelManager("dataExcel.xlsx")

# # Input
nim = st.text_input("Enter NIM:")
name = st.text_input("Enter Name:")


col1, col2= st.columns([0.01, 0.01])  # very small gaps   
# Button
with col1:
    if st.button("Delete"):
        st.success(em.deleteData([str(nim),str(name)]))

with col2:
    if (st.button("Insert")):
        st.success(em.insertData([str(nim),str(name)]))
        
newNim = st.text_input("Enter new NIM:")
newName = st.text_input("Enter new Name:")
if st.button("Edit"):
    st.success(em.editData([str(nim),str(name)],[str(newNim),str(newName)]))

st.table(em.getDataFrame())