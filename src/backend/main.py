from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.backend.database import get_connection, create_table
import streamlit as st
import requests
import pandas as pd

st.subheader("Climate Effects from API")

try:
    resp = requests.get("https://urban-space-cod-v6jrqwj6g49vfwpx6-8000.app.github.dev/docs#/")
    resp.raise_for_status()
    api_df = pd.DataFrame(resp.json())
    st.dataframe(api_df)
except requests.RequestException as e:
    st.error(e)

app = FastAPI()

create_table()


class ClimateData(BaseModel):
    country: str
    month: str
    element: str
    year: int
    value: float


@app.get("/")
def home():
    return {"message": "Climate Change API is running"}


@app.get("/data")
def get_all_data():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, country, month, element, year, value
        FROM climate_data
        LIMIT 100
    """)

    rows = cursor.fetchall()
    conn.close()

    return [
        {
            "id": row[0],
            "country": row[1],
            "month": row[2],
            "element": row[3],
            "year": row[4],
            "value": row[5],
        }
        for row in rows
    ]


@app.get("/data/{country}")
def get_data_by_country(country: str):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, country, month, element, year, value
        FROM climate_data
        WHERE country = ?
        LIMIT 100
    """, (country,))

    rows = cursor.fetchall()
    conn.close()

    if not rows:
        raise HTTPException(status_code=404, detail="Country not found")

    return [
        {
            "id": row[0],
            "country": row[1],
            "month": row[2],
            "element": row[3],
            "year": row[4],
            "value": row[5],
        }
        for row in rows
    ]


@app.post("/data")
def add_data(data: ClimateData):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO climate_data
        (country, month, element, year, value)
        VALUES (?, ?, ?, ?, ?)
    """, (
        data.country,
        data.month,
        data.element,
        data.year,
        data.value
    ))

    conn.commit()
    conn.close()

    return {"message": "Data added successfully"}


@app.delete("/data/{data_id}")
def delete_data(data_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM climate_data WHERE id = ?", (data_id,))
    conn.commit()

    deleted = cursor.rowcount
    conn.close()

    if deleted == 0:
        raise HTTPException(status_code=404, detail="Data not found")

    return {"message": "Data deleted successfully"}