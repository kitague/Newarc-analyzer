import streamlit as st
from parser import extract_text_from_pdf, extract_text_from_docx

st.title("📄 ARC Analyzer – Compliance Document Uploader")

uploaded_file = st.file_uploader("Upload a compliance document", type=["pdf", "docx"])

if uploaded_file:
    file_type = uploaded_file.name.split('.')[-1].lower()
    
    with st.spinner("Extracting text..."):
        if file_type == "pdf":
            text = extract_text_from_pdf(uploaded_file)
        elif file_type == "docx":
            text = extract_text_from_docx(uploaded_file)
        else:
            st.error("Unsupported file type.")
            text = ""
    
    if text:
        st.success("Text extraction complete!")
        st.subheader("Extracted Text Preview")
        st.text_area("Raw Extracted Text", text[:5000], height=400)
