# dashboard.py

import streamlit as st
import pandas as pd

st.title("Twitter Bot Interaction Log")

try:
    df = pd.read_csv("replies_log.csv", names=["Tweet ID", "User", "Tweet", "Bot Reply"])
    st.dataframe(df)
except FileNotFoundError:
    st.write("No logs yet. Run the bot first.")
