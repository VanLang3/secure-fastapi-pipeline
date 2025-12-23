import streamlit as st
import pandas as pd
import os
import time
from sqlalchemy import create_engine

# --- CONFIGURATION ---
# Same "Secret Handshake" as the API. 
# We grab the database address from the environment.
DATABASE_URL = os.getenv("DATABASE_URL")

# Connect to the Database
engine = create_engine(DATABASE_URL)

# --- THE DASHBOARD ---
st.set_page_config(page_title="Security Command Center", layout="wide")

st.title("🛡️ Live Security Event Log")

# Auto-refresh every 2 seconds so it feels "Alive"
if st.button('Refresh Data'):
    st.rerun()

# --- DATA LOADING ---
try:
    # ONE LINE OF CODE to load the entire database into a Pandas DataFrame
    query = "SELECT * FROM security_logs ORDER BY timestamp DESC;"
    df = pd.read_sql(query, engine)

    # --- METRICS ROW ---
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Events", len(df))
    col1.metric("Latest Event ID", df['id'].iloc[0] if not df.empty else 0)
    col2.metric("System Status", "ONLINE", delta="Secure")

    # --- THE CHART ---
    st.subheader("Event Traffic Over Time")
    st.line_chart(df.set_index('timestamp')['id'])

    # --- THE DATA TABLE ---
    st.subheader("Raw Security Logs")
    st.dataframe(df, use_container_width=True)

except Exception as e:
    st.error(f"Waiting for Database Connection... ({e})")