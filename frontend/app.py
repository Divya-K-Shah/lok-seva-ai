import streamlit as st
from utils.auth import check_auth, logout
from utils.styles import inject_global_styles

st.set_page_config(
    page_title="LoksevaAI – Smart Governance",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

inject_global_styles()

# Route to correct page
if "page" not in st.session_state:
    st.session_state.page = "home"

page = st.session_state.page


if page == "home":
    from pages.home import render
    render()

elif page == "login":
    from pages.login import render
    render()

elif page == "user":
    from pages.user_portal import render
    render()

elif page == "track":
    from pages.track_complaint import render
    render()

elif page == "official":
    from pages.official_dashboard import render
    render()

elif page == "admin":
    from pages.admin_dashboard import render
    render()

elif page == "manager":
    from pages.manager_dashboard import render
    render()