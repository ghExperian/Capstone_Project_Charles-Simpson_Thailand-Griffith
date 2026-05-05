from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel

from src.backend.database import create_table, get_connection

app = FastAPI()

create_table()

API_KEY = "thailand&charlesdeserveagoodgrade"


def verify_api_key(x_api_key: str = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")


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
def get_all_data(x_api_key: str = Header(None)):
    verify_api_key(x_api_key)

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, country, month, element, year, value
        FROM climate_data
        LIMIT 10000
    """)

    rows = cursor.fetchall()
    conn.close()

    return format_rows(rows)


@app.get("/data/{country}")
def get_data_by_country(country: str, x_api_key: str = Header(None)):
    verify_api_key(x_api_key)

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, country, month, element, year, value
        FROM climate_data
        WHERE country = ?
        LIMIT 10000
    """, (country,))

    rows = cursor.fetchall()
    conn.close()

    if not rows:
        raise HTTPException(status_code=404, detail="Country not found")

    return format_rows(rows)


@app.post("/data")
def add_data(data: ClimateData, x_api_key: str = Header(None)):
    verify_api_key(x_api_key)

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
        data.value,
    ))

    conn.commit()
    conn.close()

    return {"message": "Data added successfully"}


@app.delete("/data/{data_id}")
def delete_data(data_id: int, x_api_key: str = Header(None)):
    verify_api_key(x_api_key)

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM climate_data WHERE id = ?", (data_id,))
    conn.commit()

    deleted = cursor.rowcount
    conn.close()

    if deleted == 0:
        raise HTTPException(status_code=404, detail="Data not found")

    return {"message": "Data deleted successfully"}


def format_rows(rows):
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
