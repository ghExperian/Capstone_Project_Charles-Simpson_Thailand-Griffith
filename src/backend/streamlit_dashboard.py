import streamlit as st
from streamlit.web import cli
import pandas as pd
import requests
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import Patient, get_db

st.title('Dashboard - Climate Change')
st.markdown("## Analyze climate changes and environmental effects.")
df = pd.read_csv('./climate.csv', encoding = 'latin-1')
st.write("Recorded Data")
st.dataframe(df)


# In case we wanted to specify a specific local host location.
#if __name__ == '__main__':
#    cli.main_run(["streamlit_dashboard.py","--server.port", "8501"])


st.subheader('Overall Temperature Increase')
avg_temp_rise = df["Y2019"].value_counts()
st.line_chart(avg_temp_rise)

st.subheader("USA Temperature Increase")
timeline = st.slider(label = "Select Time Frame", min_value = 1961, max_value = 2019, value = (1961,2019))
filtered_df = df[(df["Y1980"] >= timeline[-2]) & (df["Y1999"] <= timeline[1])]
st.dataframe(filtered_df)


condition = st.selectbox(
    label = "Select a Country",
    options = ["All"] + list(df["Area"].unique())
)
if condition != "All":
    filtered_df = filtered_df[filtered_df["Area"] == condition]
    st.dataframe(filtered_df)





app = FastAPI(title="Climate Effects from API")

class ClimateData(BaseModel):
    country: str
    month: str
    element: str
    year: int
    value: float

@app.get("/patients/", response_model=list[ClimateData])
def get_patients(db: Session = Depends(get_db)):
    return db.query(Patient).all()

st.subheader("Climate Effects from API")

try:
    response = requests.get("https://urban-space-cod-v6jrqwj6g49vfwpx6-8501.app.github.dev/")
    #resp = requests.get("https://urban-space-cod-v6jrqwj6g49vfwpx6-8000.app.github.dev/docs#/")
    resp.raise_for_status()
    api_df = pd.DataFrame(resp.json())
    st.dataframe(api_df)
except requests.RequestException as e:
    st.error("Failed to connect to API")