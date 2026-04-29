import streamlit as st
import requests
import datetime

API_URL = "http://localhost:3000"

from utils.data import classify_complaint, DEPARTMENTS


def render():

    col1,col2 = st.columns([6,1])

    with col1:
        if st.button("← Back to Home"):
            st.session_state.page = "home"
            st.rerun()

    with col2:
        if st.button("🔎 Track Complaint"):
            st.session_state.page = "track"
            st.rerun()

    st.markdown("""
    <div class="hero-wrap">
        <div class="hero-tag">Citizen Portal</div>
        <div class="hero-title">File a Complaint</div>
        <p class="hero-sub">
        Describe your issue below. Our AI automatically routes complaints to the correct department.
        </p>
    </div>
    """, unsafe_allow_html=True)

    left, right = st.columns([3, 2], gap="large")

    with left:

        st.markdown("### Complaint Details")

        name = st.text_input("Your Name *")
        phone = st.text_input("Mobile Number *")
        location = st.text_input("Location / Area *")

        complaint_text = st.text_area(
            "Describe your complaint *",
            height=150
        )

        uploaded_image = st.file_uploader(
            "Attach Photo (optional)",
            type=["jpg","jpeg","png"]
        )

        if uploaded_image:
            st.image(uploaded_image,width=240)

        predicted_dept = None

        if complaint_text and len(complaint_text.strip()) > 10:
            predicted_dept = classify_complaint(complaint_text)

            st.success(f"🤖 AI Prediction: {predicted_dept}")

        submit = st.button("Submit Complaint →",use_container_width=True)

        if submit:

            if not name or not phone or not location or not complaint_text:
                st.error("Please fill all required fields")
                return

            payload = {
                "complaint": complaint_text
            }

            try:

                response = requests.post(
                    f"{API_URL}/complaints",
                    json=payload
                )

                if response.status_code == 201:

                    data = response.json()

                    c = data["data"]

                    st.session_state["last_complaint"] = c

                    st.success("✅ Complaint Submitted Successfully")

                    st.markdown("---")

                    st.markdown(f"""
                    **Complaint ID:** `{c["id"]}`  

                    **Department:** {c["department"]}  

                    **Status:** 🟡 Pending
                    """)

                    colA,colB = st.columns(2)

                    with colA:
                        if st.button("🔎 Track Complaint"):
                            st.session_state.page = "track"
                            st.rerun()

                    with colB:
                        if st.button("➕ Submit Another"):
                            st.rerun()

                else:
                    st.error(f"Server Error: {response.text}")

            except Exception as e:
                st.error(f"Backend connection failed: {e}")

    with right:

        st.markdown("### Tips for a Good Complaint")

        tips = [
            "Mention exact location",
            "Explain issue clearly",
            "Attach image if possible",
            "Submit one issue per complaint",
            "Save your Complaint ID"
        ]

        for t in tips:
            st.write("•",t)

        st.markdown("---")

        st.markdown("### Departments")

        for d in DEPARTMENTS:
            st.write("•",d)