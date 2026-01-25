import streamlit as st
import pandas as pd
import sqlite3
import os

st.set_page_config(page_title="AI Agency Dashboard", layout="wide")

st.title("🚀 AI Business Agency Dashboard")

# Tabs
tab1, tab2 = st.tabs(["🎯 Lead Research (Sales)", "🤖 AI Chat Logs (Operations)"])

# --- Tab 1: Lead Research ---
with tab1:
    st.header("Attack List")
    st.write("Target research tool output. Focus on 'High Potential' leads.")
    
    csv_path = "research_tool/leads.csv"
    if os.path.exists(csv_path):
        df = pd.read_csv(csv_path)
        
        # Color highlighting for scores
        def highlight_score(val):
            color = 'red' if val > 80 else 'orange' if val > 50 else 'black'
            return f'color: {color}; font-weight: bold'

        st.dataframe(df.style.map(highlight_score, subset=['score']))
        
        st.subheader("Action Items")
        for index, row in df.iterrows():
            if row['score'] >= 70:
                with st.expander(f"🔥 Proposal for {row['title']} (Score: {row['score']})"):
                    st.write(f"**URL:** {row['url']}")
                    st.write(f"**Strategy:** {row['strategy']}")
                    st.button(f"Generate Cold Email for {index}", key=f"btn_{index}")
    else:
        st.warning("No leads found. Run the Research Tool first.")

# --- Tab 2: Chat Logs ---
with tab2:
    st.header("AI Consultant Monitor")
    st.write("Real-time logs of AI interactions with clients.")
    
    db_path = "backend/sql_app.db"
    if os.path.exists(db_path):
        conn = sqlite3.connect(db_path)
        logs_df = pd.read_sql_query("SELECT * FROM conversations ORDER BY timestamp DESC", conn)
        conn.close()
        
        st.dataframe(logs_df)
    else:
        st.info("No conversation logs yet.")

# Sidebar
st.sidebar.header("System Status")
st.sidebar.success("Research Tool: Ready")
st.sidebar.success("AI Backend: Ready")
st.sidebar.success("Dashboard: Active")
