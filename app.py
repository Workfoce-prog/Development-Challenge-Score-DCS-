
import streamlit as st
import pandas as pd

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

import matplotlib.pyplot as plt

st.subheader("📈 Sample Scores")
sample_scores = pd.read_csv("sample_scores.csv")
st.bar_chart(sample_scores.set_index("Dimension"))

st.write("📊 Table View")
st.dataframe(sample_scores)

st.image("score_chart.png", caption="Development Challenge Scores by Dimension")
