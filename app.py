import streamlit as st
import pandas as pd

# Load CSV
@st.cache_data
def load_data():
    df = pd.read_csv("calculator.csv")
    # Clean column names (strip extra spaces)
    df.columns = df.columns.str.strip()
    # Drop rows without a valid room number
    df = df.dropna(subset=["Room Number"])
    return df

df = load_data()

st.title("Room → Total Unit Calculator")

# Show preview of data
st.write("### Data Preview")
st.dataframe(df[["Room Number", "Total Unit Number"]])

# Input: number of rooms (N)
num_rooms = st.number_input(
    "Enter number of rooms", 
    min_value=1, 
    max_value=len(df), 
    step=1
)

# Calculate total units for first N rooms
total_units = df["Total Unit Number"].head(num_rooms).sum()

st.metric("Total Units for Selected Rooms", total_units)
