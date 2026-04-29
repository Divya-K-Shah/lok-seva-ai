import streamlit as st

MOCK_USERS = {
    "admin@loksevaai.gov": {"password": "admin123", "role": "admin", "name": "Dept. Admin – KDMC", "dept": "General"},
    "manager@loksevaai.gov": {"password": "manager123", "role": "manager", "name": "District Manager", "dept": "All"},
    "roads@loksevaai.gov": {"password": "roads123", "role": "admin", "name": "Roads Dept Admin", "dept": "Roads"},
    "water@loksevaai.gov": {"password": "water123", "role": "admin", "name": "Water Dept Admin", "dept": "Water Supply"},
}

def check_auth(required_role: str) -> bool:
    user = st.session_state.get("user")
    if not user:
        return False
    if required_role == "admin":
        return user["role"] in ("admin", "manager")
    return user["role"] == required_role

def login(email: str, password: str):
    u = MOCK_USERS.get(email.lower().strip())
    if u and u["password"] == password:
        st.session_state.user = {"email": email, "role": u["role"], "name": u["name"], "dept": u["dept"]}
        return True, u["role"]
    return False, None

def logout():
    st.session_state.user = None
    st.session_state.page = "home"
