import streamlit as st
import requests
import pandas as pd
import plotly.express as px

API_URL = "http://localhost:3000"


def render():

    st.markdown("""
    <h1 style='text-align:center;'>🏛 Official Overview</h1>
    <p style='text-align:center;color:gray;'>System analytics for government officials</p>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # Navigation buttons
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("Admin Dashboard"):
            st.session_state.page = "admin"
            st.rerun()

    with col2:
        if st.button("Manager Dashboard"):
            st.session_state.page = "manager"
            st.rerun()

    with col3:
        if st.button("Logout"):
            st.session_state.page = "home"
            st.rerun()

    st.markdown("---")

    # Load complaints
    try:
        r = requests.get(f"{API_URL}/complaints")

        if r.status_code != 200:
            st.warning("No complaint data found.")
            return

        complaints = r.json()
        df = pd.DataFrame(complaints)

    except:
        st.error("Backend server not running")
        return

    if df.empty:
        st.info("No complaints submitted yet.")
        return

    # Metrics
    total = len(df)
    pending = len(df[df["status"] == "pending"])
    progress = len(df[df["status"] == "in progress"])
    resolved = len(df[df["status"] == "resolved"])

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Total Complaints", total)
    c2.metric("Pending", pending)
    c3.metric("In Progress", progress)
    c4.metric("Resolved", resolved)

    st.markdown("---")

    # SLA alert
    if pending > 5:
        st.warning("🚨 High number of pending complaints. Review required.")

    # Charts
    col1, col2 = st.columns(2)

    with col1:

        st.markdown("### 📊 Complaints by Department")

        dept_chart = px.bar(
            df,
            x="department",
            title="Department Distribution"
        )

        st.plotly_chart(dept_chart, use_container_width=True)

    with col2:

        st.markdown("### 📈 Complaint Status")

        status_chart = px.pie(
            df,
            names="status",
            title="Status Breakdown"
        )

        st.plotly_chart(status_chart, use_container_width=True)