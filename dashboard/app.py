import streamlit as st
import pandas as pd
import sqlite3
import os
import sys

# Add workspace root to path to allow imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from research_tool.analyzer import TargetAnalyzer

st.set_page_config(page_title="AI Agency Dashboard", layout="wide")

st.title("🚀 AI Business Agency Dashboard")

# Tabs
tab1, tab2 = st.tabs(["🎯 Lead Research (Sales)", "🤖 AI Chat Logs (Operations)"])

# --- Tab 1: Lead Research ---
with tab1:
    st.header("Attack List Generator")
    st.write("Enter URLs of potential clients (Competitor Ads, Coaching LPs) to analyze.")

    # Input form for new URLs
    with st.form("research_form"):
        new_urls = st.text_area("Target URLs (one per line)", height=150, placeholder="https://example.com\nhttps://another-coach.com")
        submit_button = st.form_submit_button("Analyze & Update List")

    if submit_button and new_urls:
        urls_to_process = [url.strip() for url in new_urls.split('\n') if url.strip()]
        
        with st.spinner(f"Analyzing {len(urls_to_process)} URLs..."):
            analyzer = TargetAnalyzer()
            new_results = analyzer.process_list(urls_to_process)
            
            # Load existing if available
            csv_path = "research_tool/leads.csv"
            if os.path.exists(csv_path):
                existing_df = pd.read_csv(csv_path)
                combined_df = pd.concat([existing_df, new_results]).drop_duplicates(subset='url', keep='last')
            else:
                combined_df = new_results
            
            # Save
            combined_df.sort_values('score', ascending=False, inplace=True)
            combined_df.to_csv(csv_path, index=False)
            st.success("Analysis complete! List updated.")

    st.divider()

    st.header("Priority Attack List")
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
            if row['score'] >= 50:
                with st.expander(f"{'🔥' if row['score'] > 70 else '⚠️'} Proposal for {row['title']} (Score: {row['score']})"):
                    st.write(f"**URL:** {row['url']}")
                    st.info(f"**Strategy:** {row['strategy']}")
                    if st.button(f"Generate Cold Email", key=f"btn_{index}"):
                        st.text_area("Draft Email", value=f"""
件名: {row['title']}のご担当者様へ：集客の取りこぼしを防ぐAI活用のご提案

突然のご連絡失礼いたします。
AIビジネスアーキテクトの[あなたの名前]と申します。

貴社のWebサイト（{row['url']}）を拝見し、素晴らしいサービスを展開されていることに感銘を受けました。
一方で、Meta広告（Pixel検出済）からの流入に対して、LINEへの誘導設計（{'未検出' if not row['has_line'] else '既存'}）にさらに改善の余地があるのではないかと推察いたしました。

具体的には、{row['strategy']}

現在、初期費用を抑えた「成果直結型AIファネル構築」のモニター企業様を募集しております。
もしご興味があれば、現状の課題診断だけでもさせていただけないでしょうか？

ご返信お待ちしております。
                        """, height=300)

    else:
        st.warning("No leads found. Enter URLs above to start.")

# --- Tab 2: Chat Logs ---
with tab2:
    st.header("AI Consultant Monitor")
    st.write("Real-time logs of AI interactions with clients.")
    
    if st.button("Refresh Logs"):
        st.rerun()

    db_path = "backend/sql_app.db"
    if os.path.exists(db_path):
        conn = sqlite3.connect(db_path)
        try:
            logs_df = pd.read_sql_query("SELECT * FROM conversations ORDER BY timestamp DESC", conn)
            st.dataframe(logs_df)
        except Exception as e:
            st.error(f"Error reading DB: {e}")
        finally:
            conn.close()
    else:
        st.info("No conversation logs yet.")

# Sidebar
st.sidebar.header("System Status")
st.sidebar.success("Research Tool: Ready")
st.sidebar.success("AI Backend: Ready")
st.sidebar.success("Dashboard: Active")
