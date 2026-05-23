import pandas as pd
import streamlit as st

# --- Page Title & Description ---
# --- عنوان الصفحة والوصف ---
st.title("📊 Data Analysis Tool (CSV & JSON)")
st.write("Upload your CSV or JSON file from any device for an instant data analysis!")

# --- File Uploader Widget (Supports both CSV and JSON) ---
# --- أداة رفع الملفات (تدعم ملفات CSV و JSON) ---
uploaded_file = st.file_uploader(
    "Choose Data File", type=["csv", "json"]
)

# --- Check if a file has been uploaded ---
# --- التحقق مما إذا كان قد تم رفع ملف بنجاح ---
if uploaded_file is not None:
    try:
        # --- Detect file type based on extension and read accordingly ---
        # --- معرفة نوع الملف بناءً على الامتداد وقراءته بالشكل المناسب ---
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith(".json"):
            df = pd.read_json(uploaded_file)

        # --- Display success message ---
        # --- عرض رسالة نجاح القراءة ---
        st.success("File uploaded and read successfully!")

        # --- Data Summary Section (Rows & Columns Metrics) ---
        # --- قسم ملخص البيانات (مؤشرات عدد الأسطر والأعمدة) ---
        st.subheader("📋 Data Summary")

        col1, col2 = st.columns(2)
        with col1:
            st.metric(label="Total Rows", value=df.shape[0])
        with col2:
            st.metric(label="Total Columns", value=df.shape[1])

        # --- Preview first 5 rows of the dataframe ---
        # --- عرض عينة من البيانات المرفوعة (أول 5 أسطر) ---
        st.subheader("👀 Data Preview (First 5 Rows)")
        st.dataframe(df.head())

        # --- Missing Values Analysis Section ---
        # --- قسم تحليل القيم المفقودة في كل عمود ---
        st.subheader("🔍 Missing Values per Column")
        
        # --- Calculate missing values and convert result into a clean dataframe ---
        # --- حساب القيم المفقودة وتحويل النتيجة إلى جدول منظم ---
        missing_data = df.isnull().sum().reset_index()
        missing_data.columns = ["Column Name", "Missing Count"]
        st.dataframe(missing_data)

    except Exception as e:
        # --- Error handling for corrupted or wrongly formatted files ---
        # --- التعامل مع الأخطاء في حال كان الملف تالفاً أو بتنسيق خاطئ ---
        st.error(f"Error reading file. Please ensure a valid format. Details: {e}")
