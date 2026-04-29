import streamlit as st
from utils.auth import login


def render():

    if st.button("← Back to Home"):
        st.session_state.page = "home"
        st.rerun()

    st.markdown("""
    <h2 style='text-align:center;'>🔐 Portal Login</h2>
    <p style='text-align:center;color:gray;'>Select login type to continue</p>
    """, unsafe_allow_html=True)

    st.markdown("---")

    role = st.selectbox(
        "Login As",
        ["User", "Official"]
    )

    st.markdown("---")

    # USER LOGIN
    if role == "User":

        st.info("Citizen access for filing and tracking complaints")

        if st.button("Continue as User"):
            st.session_state.page = "user"
            st.rerun()

    # OFFICIAL LOGIN
    elif role == "Official":

        st.markdown("### Official Credentials")

        email = st.text_input(
            "Email Address",
            placeholder="admin@loksevaai.gov"
        )

        password = st.text_input(
            "Password",
            type="password"
        )

        login_btn = st.button("Login")

        if login_btn:

            if not email or not password:
                st.error("Enter email and password")

            else:

                ok, role = login(email, password)

                if ok:

                    st.success("Login successful")

                    if role == "admin":
                        st.session_state.page = "admin"

                    elif role == "manager":
                        st.session_state.page = "manager"

                    st.rerun()

                else:
                    st.error("Invalid credentials")

    st.markdown("""
    <div style="margin-top:30px;font-size:14px;color:gray;">
    Demo accounts:<br>
    admin@loksevaai.gov / admin123<br>
    manager@loksevaai.gov / manager123
    </div>
    """, unsafe_allow_html=True)