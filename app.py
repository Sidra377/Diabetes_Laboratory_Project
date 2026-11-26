import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Diabetes EDA Dashboard", layout="wide")

@st.cache_data
def load_data():
    return pd.read_csv("diabetes_prediction_dataset.csv")

df = load_data()

st.title("Diabetes Prediction Dashboard")
st.write("Exploratory Data Analysis of Diabetes Dataset")

st.sidebar.header("Filters")

gender = st.sidebar.multiselect(
    "Select Gender",
    df["gender"].unique(),
    default=df["gender"].unique()
)

smoking = st.sidebar.multiselect(
    "Smoking History",
    df["smoking_history"].unique(),
    default=df["smoking_history"].unique()
)

filtered_df = df[
    (df["gender"].isin(gender)) &
    (df["smoking_history"].isin(smoking))
]

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Patients", len(filtered_df))
col2.metric("Diabetes Cases", int(filtered_df["diabetes"].sum()))
col3.metric("Average Age", round(filtered_df["age"].mean(), 1))
col4.metric("Average BMI", round(filtered_df["bmi"].mean(), 1))

st.subheader("Diabetes Distribution")
fig1 = px.pie(filtered_df, names="diabetes", title="Diabetes vs Non-Diabetes")
st.plotly_chart(fig1, use_container_width=True)

st.subheader("Patients by Gender")
fig2 = px.histogram(filtered_df, x="gender", color="diabetes", barmode="group")
st.plotly_chart(fig2, use_container_width=True)

st.subheader("Age Distribution")
fig3 = px.histogram(filtered_df, x="age", color="diabetes")
st.plotly_chart(fig3, use_container_width=True)

st.subheader("BMI Distribution")
fig4 = px.histogram(filtered_df, x="bmi", color="diabetes")
st.plotly_chart(fig4, use_container_width=True)

st.subheader("Blood Glucose Levels")
fig5 = px.histogram(filtered_df, x="blood_glucose_level", color="diabetes")
st.plotly_chart(fig5, use_container_width=True)

st.subheader("HbA1c vs Blood Glucose")
fig6 = px.scatter(
    filtered_df,
    x="HbA1c_level",
    y="blood_glucose_level",
    color="diabetes"
)
st.plotly_chart(fig6, use_container_width=True)

if st.checkbox("Show Raw Data"):
    st.dataframe(filtered_df)

st.subheader("Key Findings")
st.write("- Diabetes cases show higher average glucose levels.")
st.write("- Age and BMI vary across patients.")
st.write("- HbA1c and blood glucose help explore diabetes patterns.")
