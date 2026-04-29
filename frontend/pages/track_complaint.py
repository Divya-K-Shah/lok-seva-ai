import streamlit as st
import requests

API_URL = "http://localhost:3000"


def status_badge(status):

    if status == "pending":
        return "🟡 Pending"

    if status == "in progress":
        return "🔵 In Progress"

    if status == "resolved":
        return "🟢 Resolved"

    if status == "escalated":
        return "🔴 Escalated"

    return status


def render():

    if st.button("← Back to Home"):
        st.session_state.page = "home"
        st.rerun()

    st.markdown("""
    <div class="hero-wrap">
        <div class="hero-tag">Track Complaint</div>
        <div class="hero-title">Check Complaint Status</div>
        <p class="hero-sub">Enter your complaint ID to view real-time progress.</p>
    </div>
    """, unsafe_allow_html=True)

    col1,col2 = st.columns([4,1])

    with col1:
        cid = st.text_input("Complaint ID")

    with col2:
        search = st.button("Search")

    if search and cid:

        try:

            r = requests.get(f"{API_URL}/complaints/{cid}")

            if r.status_code != 200:
                st.error("Complaint not found")
                return

            data = r.json()

        except:
            st.error("Backend server not running")
            return

        st.success("Complaint Found")

        st.markdown("---")

        badge = status_badge(data["status"])

        st.markdown(f"""
        ### 🆔 Complaint ID: `{data["id"]}`

        **Department:** {data["department"]}  
        **Priority:** {data["priority"]}  
        **Status:** {badge}

        """)

        st.markdown("### Complaint Description")

        st.write(data["complaint_text"])