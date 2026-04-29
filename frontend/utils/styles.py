import streamlit as st

def inject_global_styles():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Rajdhani:wght@400;500;600;700&family=Noto+Sans:ital,wght@0,300;0,400;0,600;1,300&display=swap');

    /* ── ROOT VARIABLES ── */
    :root {
        --navy:   #0a0f1e;
        --ink:    #0d1630;
        --card:   #111b35;
        --border: #1e2f55;
        --accent: #2563eb;
        --gold:   #f59e0b;
        --teal:   #06b6d4;
        --green:  #10b981;
        --red:    #ef4444;
        --muted:  #64748b;
        --text:   #e2e8f0;
        --soft:   #94a3b8;
    }

    /* ── BASE ── */
    html, body, [data-testid="stAppViewContainer"] {
        background: var(--navy) !important;
        color: var(--text) !important;
        font-family: 'Noto Sans', sans-serif !important;
    }
    [data-testid="stHeader"] { background: transparent !important; }
    [data-testid="stSidebar"] { background: var(--ink) !important; border-right: 1px solid var(--border); }
    .block-container { padding: 1.5rem 2rem !important; max-width: 1400px; }

    /* ── HEADINGS ── */
    h1, h2, h3, h4 { font-family: 'Rajdhani', sans-serif !important; color: var(--text) !important; letter-spacing: .03em; }

    /* ── BUTTONS ── */
    .stButton > button {
        background: var(--accent) !important;
        color: white !important;
        border: none !important;
        border-radius: 6px !important;
        font-family: 'Rajdhani', sans-serif !important;
        font-size: 1rem !important;
        font-weight: 600 !important;
        letter-spacing: .06em !important;
        padding: .55rem 1.4rem !important;
        transition: background .2s, transform .15s !important;
    }
    .stButton > button:hover { background: #1d4ed8 !important; transform: translateY(-1px) !important; }

    /* ── INPUTS ── */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea,
    .stSelectbox > div > div {
        background: var(--card) !important;
        color: var(--text) !important;
        border: 1px solid var(--border) !important;
        border-radius: 6px !important;
    }
    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus { border-color: var(--accent) !important; box-shadow: 0 0 0 2px rgba(37,99,235,.25) !important; }

    /* ── CARDS ── */
    .lk-card {
        background: var(--card);
        border: 1px solid var(--border);
        border-radius: 12px;
        padding: 1.4rem 1.6rem;
        margin-bottom: 1rem;
        transition: border-color .2s;
    }
    .lk-card:hover { border-color: var(--accent); }

    /* ── STAT TILES ── */
    .stat-tile {
        background: var(--card);
        border: 1px solid var(--border);
        border-radius: 10px;
        padding: 1.2rem 1.4rem;
        text-align: center;
    }
    .stat-tile .num { font-family:'Rajdhani',sans-serif; font-size:2.2rem; font-weight:700; color:var(--accent); line-height:1; }
    .stat-tile .lbl { font-size:.78rem; color:var(--soft); letter-spacing:.06em; text-transform:uppercase; margin-top:.3rem; }

    /* ── BADGE STATUS ── */
    .badge { display:inline-block; padding:.2rem .65rem; border-radius:99px; font-size:.72rem; font-weight:600; letter-spacing:.05em; }
    .badge-pending  { background:#422006; color:#fbbf24; }
    .badge-progress { background:#0c2a4a; color:#38bdf8; }
    .badge-resolved { background:#052e16; color:#4ade80; }
    .badge-escalate { background:#3b0764; color:#e879f9; }

    /* ── NAV TABS ── */
    .lk-nav { display:flex; gap:.6rem; margin-bottom:1.6rem; flex-wrap:wrap; }
    .lk-tab {
        background:var(--card); border:1px solid var(--border);
        color:var(--soft); border-radius:8px; padding:.5rem 1.1rem;
        cursor:pointer; font-family:'Rajdhani',sans-serif;
        font-size:.95rem; font-weight:600; letter-spacing:.05em;
        transition: all .2s; text-decoration:none; display:inline-block;
    }
    .lk-tab.active { background:var(--accent); border-color:var(--accent); color:#fff; }

    /* ── HERO ── */
    .hero-wrap {
        background: linear-gradient(135deg, #0a1628 0%, #0d2050 50%, #091428 100%);
        border: 1px solid var(--border);
        border-radius: 16px;
        padding: 3rem 2.5rem;
        margin-bottom: 2rem;
        position: relative;
        overflow: hidden;
    }
    .hero-wrap::before {
        content:'';
        position:absolute; top:-60px; right:-60px;
        width:260px; height:260px;
        background: radial-gradient(circle, rgba(37,99,235,.18) 0%, transparent 70%);
        pointer-events:none;
    }
    .hero-tag { font-size:.72rem; letter-spacing:.18em; text-transform:uppercase; color:var(--teal); margin-bottom:.6rem; font-weight:600; }
    .hero-title { font-family:'Rajdhani',sans-serif; font-size:2.8rem; font-weight:700; line-height:1.15; color:#fff; margin-bottom:.8rem; }
    .hero-title span { color:var(--gold); }
    .hero-sub { color:var(--soft); font-size:1rem; max-width:560px; line-height:1.65; }

    /* ── TABLE ── */
    .lk-table { width:100%; border-collapse:collapse; font-size:.88rem; }
    .lk-table th { background:var(--ink); color:var(--soft); text-transform:uppercase; font-size:.72rem; letter-spacing:.09em; padding:.7rem 1rem; border-bottom:1px solid var(--border); text-align:left; }
    .lk-table td { padding:.75rem 1rem; border-bottom:1px solid var(--border); color:var(--text); vertical-align:middle; }
    .lk-table tr:last-child td { border-bottom:none; }
    .lk-table tr:hover td { background:rgba(37,99,235,.06); }

    /* ── COMPLAINT ID ── */
    .complaint-id { font-family:'Rajdhani',sans-serif; font-size:2rem; font-weight:700; color:var(--gold); letter-spacing:.12em; }

    /* ── MISC ── */
    .divider { height:1px; background:var(--border); margin:1.5rem 0; }
    .muted { color:var(--muted); font-size:.85rem; }
    hr { border-color: var(--border) !important; }
    [data-testid="stMetricValue"] { color: var(--accent) !important; font-family:'Rajdhani',sans-serif !important; }
    </style>
    """, unsafe_allow_html=True)
