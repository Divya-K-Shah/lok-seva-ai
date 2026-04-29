import streamlit as st
import requests
import pandas as pd
import plotly.express as px

API_URL = "http://localhost:3000"


def render():

    # Top buttons
    col1, col2 = st.columns([8,2])

    with col1:
        if st.button("← Back to Home"):
            st.session_state.page = "home"
            st.rerun()

    with col2:
        if st.button("Logout"):
            st.session_state.user = None
            st.session_state.page = "home"
            st.rerun()


    st.markdown("## System Overview")


    try:
        response = requests.get(f"{API_URL}/complaints")

        if response.status_code == 200:
            complaints = response.json()
        else:
            st.error("Failed to fetch complaints")
            return

    except:
        st.error("Backend server not running")
        return


    if not complaints:
        st.warning("No complaints found")
        return


    df = pd.DataFrame(complaints)


    total = len(df)
    pending = len(df[df["status"]=="pending"])
    in_progress = len(df[df["status"]=="in progress"])
    resolved = len(df[df["status"]=="resolved"])
    escalated = len(df[df.get("escalated",False)==True])


    col1,col2,col3,col4,col5 = st.columns(5)

    col1.metric("Total Complaints",total)
    col2.metric("Pending",pending)
    col3.metric("In Progress",in_progress)
    col4.metric("Resolved",resolved)
    col5.metric("Escalated",escalated)


    st.markdown("### Complaints by Department")

    dept_chart = px.bar(
        df,
        x="department",
        title="Complaints by Department"
    )

    st.plotly_chart(dept_chart, use_container_width=True)


    st.markdown("### Complaints by Status")

    status_chart = px.pie(df,names="status")

    st.plotly_chart(status_chart,use_container_width=True)


    if "escalated" in df.columns:

        esc = df[df["escalated"]==True]

        st.markdown("### Recent Escalations")

        if len(esc)>0:
            st.dataframe(esc[["id","complaint_text","department","priority"]])
        else:
            st.info("No escalated complaints")