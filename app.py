
import os
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Development Challenge Score", layout="centered")
st.title("🌍 Development Challenge Score Calculator")

st.markdown("""
Upload your CSV file with columns like:
- Youth_Unemployment, Informal_Employment, GDP_Growth, Credit_Access,
- Enrollment_Rate, Literacy_Rate, Pupil_Teacher_Ratio, Digital_Access,
- Maternal_Mortality, Sanitation_Access, Infant_Mortality, Doctors_per_1000,
- CPI, Gov_Effectiveness, Rule_of_Law, Civic_Engagement,
- Electricity_Access, Internet_Penetration, Road_Quality, Mobile_Phone_Access,
- Deforestation, CO2_per_Capita, Disaster_Preparedness, Water_Management,
- Gini, Gender_Equity, Justice_Access, Youth_Disenfranchisement
""")

uploaded_file = st.file_uploader("Upload your data (CSV)", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("📊 Data Preview")
    st.dataframe(df)

    st.subheader("✅ Score Summary")
    score_summary = df.describe()
    st.write(score_summary)

    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Download Results", csv, "results.csv", "text/csv")

# Use safe paths for bundled files
BASE_DIR = os.path.dirname(__file__)
sample_score_path = os.path.join(BASE_DIR, "sample_scores.csv")
chart_path = os.path.join(BASE_DIR, "score_chart.png")

if os.path.exists(sample_score_path):
    st.subheader("📈 Sample Scores")
    sample_scores = pd.read_csv(sample_score_path)
    st.bar_chart(sample_scores.set_index("Dimension"))

    st.write("📊 Table View")
    st.dataframe(sample_scores)

if os.path.exists(chart_path):
    st.image(chart_path, caption="Development Challenge Scores by Dimension")
