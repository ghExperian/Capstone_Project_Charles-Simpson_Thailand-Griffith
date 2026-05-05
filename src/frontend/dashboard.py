import pandas as pd
import requests
import streamlit as st

API_URL = "http://localhost:8000/data"
API_KEY = "thailand&charlesdeserveagoodgrade"

st.set_page_config(page_title="Climate Dashboard", layout="wide")

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

st.sidebar.subheader("Login")

username = st.sidebar.text_input("Username")
password = st.sidebar.text_input("Password", type="password")

if st.sidebar.button("Login"):
    if username == "Dr.Ali" and password == "IsTheBest":
        st.session_state.authenticated = True
    else:
        st.sidebar.error("Invalid credentials")

if st.sidebar.button("Logout"):
    st.session_state.authenticated = False
    st.rerun()

if not st.session_state.authenticated:
    st.warning("Please log in to access the dashboard")
    st.stop()

st.title("Climate Change Dashboard")
st.markdown("### Analyze global climate trends and environmental impacts")

try:
    headers = {"x-api-key": API_KEY}
    response = requests.get(API_URL, headers=headers, timeout=10)
    response.raise_for_status()
    df = pd.DataFrame(response.json())

    st.sidebar.header("Dashboard Filters")

    timeline = st.sidebar.slider(
        "Select Time Frame",
        int(df["year"].min()),
        int(df["year"].max()),
        (int(df["year"].min()), int(df["year"].max())),
    )

    element = st.sidebar.selectbox(
        "Select Climate Element",
        ["All"] + sorted(df["element"].unique()),
    )

    graph_country = st.sidebar.selectbox(
        "Select Country for Main Graphs",
        ["All"] + sorted(df["country"].unique()),
    )

    monthly_countries = st.sidebar.multiselect(
        "Select Countries for Monthly Pattern",
        sorted(df["country"].unique()),
        default=sorted(df["country"].unique())[:3],
    )

    filtered_df = df[
        (df["year"] >= timeline[0]) &
        (df["year"] <= timeline[1])
    ]

    if element != "All":
        filtered_df = filtered_df[filtered_df["element"] == element]

    graph_df = filtered_df.copy()

    if graph_country != "All":
        graph_df = graph_df[graph_df["country"] == graph_country]

    st.subheader("Filtered Climate Data")
    st.dataframe(graph_df, use_container_width=True)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Climate Trend Over Time")
        line_data = graph_df.groupby("year")["value"].mean()
        st.line_chart(line_data)

    with col2:
        st.subheader("Top 10 Affected Countries")
        country_data = (
            filtered_df.groupby("country")["value"]
            .mean()
            .sort_values(ascending=False)
            .head(10)
        )
        st.bar_chart(country_data)

    st.subheader("Climate Element Summary")

    element_summary = (
        graph_df.groupby("element")["value"]
        .agg(["mean", "min", "max", "count"])
        .reset_index()
    )

    element_summary.columns = [
        "Climate Element",
        "Average Value",
        "Lowest Value",
        "Highest Value",
        "Records",
    ]

    st.dataframe(element_summary, use_container_width=True)

    st.subheader("Average Climate Value by Element")

    element_chart = (
        graph_df.groupby("element")["value"]
        .mean()
        .sort_values()
    )

    st.area_chart(element_chart)

    st.subheader("Monthly Climate Patterns by Country")

    monthly_df = filtered_df.copy()

    if monthly_countries:
        monthly_df = monthly_df[
            monthly_df["country"].isin(monthly_countries)
        ]

    monthly_data = (
        monthly_df.groupby(["month", "country"])["value"]
        .mean()
        .reset_index()
        .pivot(index="month", columns="country", values="value")
    )

    st.line_chart(monthly_data)

except requests.RequestException as e:
    st.error(f"Failed to connect to the backend API: {e}")

except KeyError as e:
    st.error(f"Missing expected column from API data: {e}")
