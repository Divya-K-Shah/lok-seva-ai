import streamlit as st
import time

def render():

    st.markdown("""
    <style>

    .hero{
        text-align:center;
        padding:60px 20px;
        animation: fadeIn 1.5s ease-in;
    }

    @keyframes fadeIn{
        from{opacity:0; transform:translateY(20px);}
        to{opacity:1; transform:translateY(0);}
    }

    .enter-btn{
        display:flex;
        justify-content:center;
        margin-top:30px;
    }

    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="hero">

    <h1 style="font-size:48px;">🏛 LokSevaAI</h1>

    <p style="font-size:18px;color:gray;">
    Smart Civic Complaint Redressal System
    </p>

    <p style="font-size:15px;color:#9aa0a6;">
    AI powered platform for faster grievance resolution
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    col1,col2,col3 = st.columns([1,1,1])

    with col2:
        if st.button("🚪 Enter Portal"):
            st.session_state.page = "login"
            st.rerun()

    st.markdown("---")

    # Interactive cards
    c1,c2,c3 = st.columns(3)

    with c1:
        st.markdown("""
        ### 🤖 AI Routing
        Automatically routes complaints to the correct department.
        """)

    with c2:
        st.markdown("""
        ### ⚡ Faster Resolution
        SLA tracking ensures quicker complaint handling.
        """)

    with c3:
        st.markdown("""
        ### 📊 Transparency
        Citizens can track complaint status anytime.
        """)