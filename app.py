import os
import streamlit as st
import pandas as pd
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

st.set_page_config(page_title="NeuralBank Analytics", page_icon="🧠", layout="wide")

# ── FUTURISTIC CSS ──
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Rajdhani:wght@300;400;600&family=Share+Tech+Mono&display=swap');

/* ── GLOBAL ── */
html, body, [class*="css"] {
    background-color: #020c1b !important;
    color: #a8d8ea !important;
    font-family: 'Rajdhani', sans-serif !important;
}

.stApp {
    background: #020c1b !important;
    background-image:
        radial-gradient(ellipse at 20% 50%, rgba(0, 255, 255, 0.03) 0%, transparent 50%),
        radial-gradient(ellipse at 80% 20%, rgba(0, 100, 255, 0.05) 0%, transparent 50%),
        linear-gradient(180deg, #020c1b 0%, #030d20 100%) !important;
}

/* Scanline overlay */
.stApp::before {
    content: '';
    position: fixed;
    top: 0; left: 0; right: 0; bottom: 0;
    background: repeating-linear-gradient(
        0deg,
        transparent,
        transparent 2px,
        rgba(0, 255, 255, 0.01) 2px,
        rgba(0, 255, 255, 0.01) 4px
    );
    pointer-events: none;
    z-index: 9999;
}

/* ── HEADER ── */
.neural-header {
    text-align: center;
    padding: 0.5rem 0 0.3rem 0;
    position: relative;
}

.neural-title {
    font-family: 'Orbitron', monospace !important;
    font-size: 1.8rem !important;
    font-weight: 900 !important;
    background: linear-gradient(90deg, #00fff2, #0080ff, #00fff2);
    background-size: 200% auto;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: shine 3s linear infinite;
    letter-spacing: 0.15em;
    margin: 0 !important;
}

.neural-subtitle {
    font-family: 'Share Tech Mono', monospace;
    color: #00fff2 !important;
    font-size: 0.75rem;
    letter-spacing: 0.3em;
    opacity: 0.6;
    margin-top: 0.3rem;
}

@keyframes shine {
    to { background-position: 200% center; }
}

/* Glowing divider */
.glow-divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, #00fff2, #0080ff, #00fff2, transparent);
    margin: 1rem 0;
    position: relative;
    animation: pulse-line 2s ease-in-out infinite;
}

@keyframes pulse-line {
    0%, 100% { opacity: 0.4; }
    50% { opacity: 1; }
}

/* ── METRIC CARDS ── */
.metric-card {
    background: linear-gradient(135deg, rgba(0,255,242,0.05), rgba(0,128,255,0.08));
    border: 1px solid rgba(0, 255, 242, 0.2);
    border-radius: 4px;
    padding: 0.5rem 0.4rem;
    text-align: center;
    position: relative;
    overflow: hidden;
    transition: all 0.3s ease;
}

.metric-card::before {
    content: '';
    position: absolute;
    top: 0; left: -100%;
    width: 100%; height: 100%;
    background: linear-gradient(90deg, transparent, rgba(0,255,242,0.05), transparent);
    animation: card-scan 4s ease-in-out infinite;
}

@keyframes card-scan {
    0% { left: -100%; }
    50%, 100% { left: 100%; }
}

.metric-card:hover {
    border-color: rgba(0, 255, 242, 0.6);
    box-shadow: 0 0 12px rgba(0, 255, 242, 0.15);
    transform: translateY(-1px);
}

.metric-value {
    font-family: 'Orbitron', monospace;
    font-size: 1.1rem;
    font-weight: 700;
    color: #00fff2 !important;
    text-shadow: 0 0 8px rgba(0,255,242,0.5);
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

.metric-label {
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.55rem;
    color: #6b9fb8 !important;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    margin-top: 0.2rem;
    white-space: nowrap;
}

/* ── SECTION HEADERS ── */
.section-header {
    font-family: 'Orbitron', monospace;
    font-size: 0.75rem;
    letter-spacing: 0.2em;
    color: #00fff2 !important;
    text-transform: uppercase;
    padding: 0.3rem 0;
    border-left: 3px solid #00fff2;
    padding-left: 0.8rem;
    margin: 0.8rem 0 0.5rem 0;
    text-shadow: 0 0 8px rgba(0,255,242,0.4);
}

/* ── CHATBOT ── */
.chat-container {
    background: rgba(0, 20, 40, 0.8);
    border: 1px solid rgba(0, 255, 242, 0.15);
    border-radius: 4px;
    padding: 1.5rem;
    margin-bottom: 1rem;
    position: relative;
}

.chat-container::after {
    content: '[ NEURAL LINK ACTIVE ]';
    position: absolute;
    top: -10px; right: 20px;
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.6rem;
    color: #00fff2;
    background: #020c1b;
    padding: 0 8px;
    letter-spacing: 0.15em;
    animation: blink 1.5s step-end infinite;
}

@keyframes blink {
    0%, 100% { opacity: 1; }
    50% { opacity: 0; }
}

.user-bubble {
    background: rgba(0, 128, 255, 0.1);
    border: 1px solid rgba(0, 128, 255, 0.3);
    border-radius: 4px 4px 4px 0;
    padding: 0.8rem 1rem;
    margin: 0.5rem 0;
    font-family: 'Rajdhani', sans-serif;
    font-size: 1rem;
    color: #a8d8ea !important;
    position: relative;
}

.user-bubble::before {
    content: '▶ USER';
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.55rem;
    color: #0080ff;
    letter-spacing: 0.15em;
    display: block;
    margin-bottom: 0.3rem;
}

.ai-bubble {
    background: rgba(0, 255, 242, 0.04);
    border: 1px solid rgba(0, 255, 242, 0.2);
    border-radius: 4px 4px 0 4px;
    padding: 1rem 1.2rem;
    margin: 0.5rem 0;
    font-family: 'Rajdhani', sans-serif;
    font-size: 1rem;
    line-height: 1.7;
    color: #c8e8f0 !important;
    animation: fadeInUp 0.4s ease;
}

.ai-bubble::before {
    content: '◀ NEURAL ANALYST';
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.55rem;
    color: #00fff2;
    letter-spacing: 0.15em;
    display: block;
    margin-bottom: 0.5rem;
    text-shadow: 0 0 6px rgba(0,255,242,0.5);
}

@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
}

/* ── INPUT ── */
.stTextInput > div > div > input {
    background: rgba(0, 20, 40, 0.9) !important;
    border: 1px solid rgba(0, 255, 242, 0.3) !important;
    border-radius: 2px !important;
    color: #00fff2 !important;
    font-family: 'Share Tech Mono', monospace !important;
    font-size: 0.9rem !important;
    padding: 0.8rem 1rem !important;
    caret-color: #00fff2;
}

.stTextInput > div > div > input:focus {
    border-color: #00fff2 !important;
    box-shadow: 0 0 15px rgba(0, 255, 242, 0.2) !important;
    outline: none !important;
}

.stTextInput > div > div > input::placeholder {
    color: rgba(0, 255, 242, 0.3) !important;
}



/* ── CHARTS ── */
.stVegaLiteChart, [data-testid="stArrowVegaLiteChart"] {
    background: rgba(0, 20, 40, 0.6) !important;
    border: 1px solid rgba(0, 255, 242, 0.1) !important;
    border-radius: 4px !important;
    padding: 0.5rem !important;
}

/* ── SIDEBAR ── */
[data-testid="stSidebar"] {
    background: rgba(2, 10, 25, 0.95) !important;
    border-right: 1px solid rgba(0, 255, 242, 0.1) !important;
}

[data-testid="stSidebar"] * {
    color: #a8d8ea !important;
}

.sidebar-title {
    font-family: 'Orbitron', monospace;
    font-size: 0.7rem;
    letter-spacing: 0.2em;
    color: #00fff2 !important;
    text-transform: uppercase;
    margin-bottom: 1rem;
}

/* ── MULTISELECT ── */
.stMultiSelect > div > div {
    background: rgba(0, 20, 40, 0.9) !important;
    border: 1px solid rgba(0, 255, 242, 0.2) !important;
    border-radius: 2px !important;
}

.stMultiSelect label {
    color: #00fff2 !important;
    font-family: 'Share Tech Mono', monospace !important;
    font-size: 0.75rem !important;
    letter-spacing: 0.15em !important;
    text-transform: uppercase !important;
}

/* Selected tags */
.stMultiSelect [data-baseweb="tag"] {
    background: #00fff2 !important;
    border: 1px solid #00fff2 !important;
}

.stMultiSelect [data-baseweb="tag"] span,
.stMultiSelect [data-baseweb="tag"] span * {
    color: #020c1b !important;
    font-family: 'Share Tech Mono', monospace !important;
    font-size: 0.7rem !important;
    font-weight: 700 !important;
    -webkit-text-fill-color: #020c1b !important;
}

/* Dropdown container */
[data-baseweb="popover"],
[data-baseweb="menu"],
ul[role="listbox"] {
    background: #020c1b !important;
    border: 1px solid rgba(0,255,242,0.2) !important;
}

/* ALL dropdown list items */
[data-baseweb="popover"] li,
[data-baseweb="menu"] li,
ul[role="listbox"] li,
[role="option"] {
    background: #020c1b !important;
    color: #e0f4ff !important;
    font-family: 'Share Tech Mono', monospace !important;
    font-size: 0.75rem !important;
}

/* Highlighted/selected item in dropdown */
[data-baseweb="popover"] li[aria-selected="true"],
[role="option"][aria-selected="true"],
[data-baseweb="menu"] [aria-selected="true"] {
    background: rgba(0,255,242,0.15) !important;
    color: #00fff2 !important;
}

/* Hovered item */
[data-baseweb="popover"] li:hover,
[role="option"]:hover {
    background: rgba(0,255,242,0.1) !important;
    color: #00fff2 !important;
}

/* Dropdown input text */
.stMultiSelect input {
    color: #e0f4ff !important;
    caret-color: #00fff2 !important;
}

/* ── SPINNER ── */
.stSpinner > div {
    border-top-color: #00fff2 !important;
}

/* ── SCROLLBAR ── */
::-webkit-scrollbar { width: 4px; }
::-webkit-scrollbar-track { background: #020c1b; }
::-webkit-scrollbar-thumb { background: rgba(0, 255, 242, 0.3); border-radius: 2px; }
::-webkit-scrollbar-thumb:hover { background: #00fff2; }

/* ── BUTTONS — equal size ── */
.stButton > button {
    background: transparent !important;
    border: 1px solid rgba(0, 255, 242, 0.5) !important;
    color: #00fff2 !important;
    font-family: 'Orbitron', monospace !important;
    font-size: 0.65rem !important;
    letter-spacing: 0.15em !important;
    padding: 0.5rem 0 !important;
    width: 100% !important;
    min-width: 0 !important;
    border-radius: 2px !important;
    transition: all 0.2s ease !important;
    text-transform: uppercase !important;
    white-space: nowrap !important;
}

.stButton > button:hover {
    background: rgba(0, 255, 242, 0.1) !important;
    border-color: #00fff2 !important;
    box-shadow: 0 0 15px rgba(0, 255, 242, 0.3) !important;
    transform: translateY(-1px) !important;
}

.stButton > button[kind="primary"] {
    background: rgba(0, 255, 242, 0.08) !important;
    border-color: #00fff2 !important;
}

/* ── TEXT CONTRAST FIXES ── */
p, li, span, div, label {
    color: #e0f4ff !important;
}

h1, h2, h3, h4, h5, h6 {
    color: #ffffff !important;
}

.stMarkdown p {
    color: #e0f4ff !important;
    font-size: 1rem !important;
}

/* Chart axis labels and ticks */
.vega-embed text, canvas {
    fill: #e0f4ff !important;
    color: #e0f4ff !important;
}

/* Multiselect labels */
.stMultiSelect label, .stTextInput label {
    color: #e0f4ff !important;
    font-family: 'Share Tech Mono', monospace !important;
    font-size: 0.75rem !important;
    letter-spacing: 0.1em !important;
}

/* Sidebar text */
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] span,
[data-testid="stSidebar"] label,
[data-testid="stSidebar"] div {
    color: #e0f4ff !important;
}

/* ── SIDEBAR TOGGLE — always visible ── */
[data-testid="collapsedControl"] {
    display: flex !important;
    visibility: visible !important;
    opacity: 1 !important;
    position: fixed !important;
    top: 50vh !important;
    left: 0 !important;
    z-index: 999999 !important;
    background: #020c1b !important;
    border: 1px solid #00fff2 !important;
    border-left: none !important;
    border-radius: 0 6px 6px 0 !important;
    width: 24px !important;
    height: 48px !important;
    align-items: center !important;
    justify-content: center !important;
    cursor: pointer !important;
    box-shadow: 4px 0 15px rgba(0,255,242,0.25) !important;
    transition: all 0.2s ease !important;
}

[data-testid="collapsedControl"]:hover {
    background: rgba(0,255,242,0.15) !important;
    box-shadow: 4px 0 25px rgba(0,255,242,0.5) !important;
    width: 30px !important;
}

[data-testid="collapsedControl"] svg {
    fill: #00fff2 !important;
    width: 14px !important;
    height: 14px !important;
}

/* ── EXPANDER ── */
.streamlit-expanderHeader {
    background: rgba(0, 20, 40, 0.8) !important;
    border: 1px solid rgba(0, 255, 242, 0.2) !important;
    border-radius: 4px !important;
    color: #00fff2 !important;
    font-family: 'Share Tech Mono', monospace !important;
    font-size: 0.75rem !important;
    letter-spacing: 0.15em !important;
}

.streamlit-expanderContent {
    background: rgba(0, 10, 25, 0.9) !important;
    border: 1px solid rgba(0, 255, 242, 0.1) !important;
    border-top: none !important;
    padding: 1rem !important;
}

/* ── HIDE STREAMLIT BRANDING ── */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 0.3rem !important; padding-bottom: 0.5rem !important; }
</style>
""", unsafe_allow_html=True)

# ── HEADER ──
st.markdown("""
<div class="neural-header">
    <div class="neural-title">NEURALBANK ANALYTICS</div>
    <div class="neural-subtitle">▸ BANK MARKETING INTELLIGENCE SYSTEM ▸ RAG-POWERED ▸ BUILT BY DURGESH CHOUBEY</div>
</div>
<div class="glow-divider"></div>
""", unsafe_allow_html=True)

# ── Load Data ──
@st.cache_data
def load_data():
    df = pd.read_csv("bank-full.csv", sep=";")
    return df

df = load_data()

# ── LLM Setup ──
llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.3-70b-versatile",
    temperature=0.2
)

prompt = PromptTemplate(
    input_variables=["data_summary", "question"],
    template="""
You are a senior marketing data scientist at a major financial services company similar to American Express.
You are analyzing a bank's direct marketing campaign dataset (45,000+ customer records).

Here is the full analytics summary of the dataset:
{data_summary}

A business stakeholder asks: {question}

Respond like a senior data scientist presenting to a marketing executive. Structure your answer as:

**Direct Answer:** (1-2 sentences with specific numbers)

**Key Insight:** (What does this mean for the business?)

**Recommended Action:** (What should the marketing team do next?)
"""
)

chain = prompt | llm | StrOutputParser()

# ── Data Summary Builder ──
def build_data_summary(df):
    total = len(df)
    converted = (df['y'] == 'yes').sum()
    conv_rate = round(converted / total * 100, 2) if total > 0 else 0
    df = df.copy()
    df['converted'] = (df['y'] == 'yes').astype(int)
    channel_conv = df.groupby('contact')['converted'].mean().mul(100).round(2)
    job_conv = df.groupby('job')['converted'].mean().mul(100).round(2).sort_values(ascending=False)
    month_order = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
    month_conv = df.groupby('month')['converted'].sum().reindex(month_order).fillna(0)
    age_stats = df.groupby('y')['age'].mean().round(1)
    duration_stats = df.groupby('y')['duration'].mean().round(1)
    edu_conv = df.groupby('education')['converted'].mean().mul(100).round(2)
    return f"""
Dataset: Bank Marketing Campaign (UCI) | {total:,} customers | {converted:,} conversions | {conv_rate}% conversion rate
Conversion by channel: {channel_conv.to_dict()}
Conversion by job (top): {job_conv.head(5).to_dict()}
Conversions by month: {month_conv.to_dict()}
Avg age converted={age_stats.get('yes','N/A')} not={age_stats.get('no','N/A')}
Avg call duration converted={duration_stats.get('yes','N/A')}s not={duration_stats.get('no','N/A')}s
Conversion by education: {edu_conv.to_dict()}
"""

import plotly.graph_objects as go

all_jobs = list(df['job'].unique())
all_contacts = list(df['contact'].unique())

# ── CHART HELPER ──
def make_chart(x, y, color, height=220):
    fig = go.Figure(go.Bar(
        x=x, y=y,
        marker=dict(color=color, opacity=0.85, line=dict(color="rgba(0,255,242,0.3)", width=1))
    ))
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Share Tech Mono", color="#e0f4ff", size=10),
        margin=dict(l=5, r=5, t=5, b=5),
        xaxis=dict(tickfont=dict(color="#e0f4ff", size=10), gridcolor="rgba(0,255,242,0.06)", linecolor="rgba(0,255,242,0.15)"),
        yaxis=dict(tickfont=dict(color="#e0f4ff", size=10), gridcolor="rgba(0,255,242,0.06)", linecolor="rgba(0,255,242,0.15)"),
        hoverlabel=dict(bgcolor="#020c1b", font_color="#00fff2", bordercolor="#00fff2"),
        height=height,
    )
    return fig

# ══════════════════════════════════════════════
# TWO-COLUMN LAYOUT
# ══════════════════════════════════════════════
left_col, right_col = st.columns([10, 10], gap="small")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# LEFT — Filters + Chatbot
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
with left_col:
    st.markdown('<div class="section-header">◈ System Filters</div>', unsafe_allow_html=True)
    selected_job2 = st.multiselect("Job Segment", options=all_jobs, default=[], key="job_filter2",
        placeholder="All segments...")
    selected_contact2 = st.multiselect("Contact Channel", options=all_contacts, default=[], key="contact_filter2",
        placeholder="All channels...")

    jobs2 = selected_job2 if selected_job2 else all_jobs
    contacts2 = selected_contact2 if selected_contact2 else all_contacts
    filtered_df = df[df['job'].isin(jobs2) & df['contact'].isin(contacts2)].copy()
    filtered_df['converted'] = (filtered_df['y'] == 'yes').astype(int)
    total = len(filtered_df)
    converted = filtered_df['converted'].sum()
    conversion_rate = round(converted / total * 100, 2) if total > 0 else 0
    avg_duration = round(filtered_df['duration'].mean(), 1) if total > 0 else 0

    st.markdown('<div class="glow-divider"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-header">◈ Neural Query Interface</div>', unsafe_allow_html=True)
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)

    question = st.text_input(
        "",
        placeholder="ENTER QUERY › e.g. Which job segment converts best?",
        label_visibility="collapsed"
    )

    col_btn1, col_btn2, col_spacer = st.columns([2, 2, 4])
    with col_btn1:
        ask_btn = st.button("▶ Execute", type="primary")
    with col_btn2:
        clear_btn = st.button("✕ Clear")

    if clear_btn:
        st.session_state.current_question = None
        st.session_state.current_answer = None

    if ask_btn and question:
        with st.spinner("Processing neural query..."):
            data_summary = build_data_summary(df)
            response = chain.invoke({"data_summary": data_summary, "question": question})
            # Strip markdown bold markers
            import re
            response = re.sub(r'\*\*(.*?)\*\*', r'\1', response)
            st.session_state.current_question = question
            st.session_state.current_answer = response

    if st.session_state.get("current_answer"):
        st.markdown(f'<div class="user-bubble">{st.session_state.current_question}</div>', unsafe_allow_html=True)
        answer_html = st.session_state.current_answer.replace('\n', '<br>')
        st.markdown(f'<div class="ai-bubble">{answer_html}</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("""
    <div style="font-family: Share Tech Mono; font-size: 0.6rem; color: rgba(0,255,242,0.3); margin-top:1rem; line-height:2;">
    ◈ Which job segment converts best?<br>
    ◈ Best contact channel?<br>
    ◈ How does age affect conversion?<br>
    ◈ Which month had highest success?<br>
    ◈ Avg call duration for converted?
    </div>
    """, unsafe_allow_html=True)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# RIGHT — KPIs + Charts (2x2 grid)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
with right_col:
    st.markdown('<div class="section-header">◈ Mission Control</div>', unsafe_allow_html=True)

    k1, k2, k3, k4 = st.columns(4)
    with k1:
        st.markdown(f'<div class="metric-card"><div class="metric-value">{total:,}</div><div class="metric-label">Customers</div></div>', unsafe_allow_html=True)
    with k2:
        st.markdown(f'<div class="metric-card"><div class="metric-value">{converted:,}</div><div class="metric-label">Conversions</div></div>', unsafe_allow_html=True)
    with k3:
        st.markdown(f'<div class="metric-card"><div class="metric-value">{conversion_rate}%</div><div class="metric-label">Conv. Rate</div></div>', unsafe_allow_html=True)
    with k4:
        st.markdown(f'<div class="metric-card"><div class="metric-value">{avg_duration}s</div><div class="metric-label">Avg Duration</div></div>', unsafe_allow_html=True)

    st.markdown('<div class="glow-divider"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-header">◈ Data Intelligence Grid</div>', unsafe_allow_html=True)

    # 2x2 chart grid
    ca, cb = st.columns(2)
    with ca:
        st.markdown('<p style="font-family:Share Tech Mono;font-size:0.6rem;color:#00fff2;letter-spacing:0.1em;margin:0.2rem 0">▸ BY CHANNEL</p>', unsafe_allow_html=True)
        channel_conv = filtered_df.groupby('contact')['converted'].mean().mul(100).round(2).reset_index()
        st.plotly_chart(make_chart(channel_conv['contact'], channel_conv['converted'], "#00fff2", height=180), use_container_width=True, config={"displayModeBar": False})
    with cb:
        st.markdown('<p style="font-family:Share Tech Mono;font-size:0.6rem;color:#0080ff;letter-spacing:0.1em;margin:0.2rem 0">▸ BY JOB</p>', unsafe_allow_html=True)
        job_conv = filtered_df.groupby('job')['converted'].mean().mul(100).round(2).reset_index()
        st.plotly_chart(make_chart(job_conv['job'], job_conv['converted'], "#0080ff", height=180), use_container_width=True, config={"displayModeBar": False})

    cc, cd = st.columns(2)
    with cc:
        st.markdown('<p style="font-family:Share Tech Mono;font-size:0.6rem;color:#00fff2;letter-spacing:0.1em;margin:0.2rem 0">▸ BY MONTH</p>', unsafe_allow_html=True)
        month_order = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
        month_conv = filtered_df.groupby('month')['converted'].sum().reindex(month_order).fillna(0).reset_index()
        st.plotly_chart(make_chart(month_conv['month'], month_conv['converted'], "#00fff2", height=180), use_container_width=True, config={"displayModeBar": False})
    with cd:
        st.markdown('<p style="font-family:Share Tech Mono;font-size:0.6rem;color:#0080ff;letter-spacing:0.1em;margin:0.2rem 0">▸ BY EDUCATION</p>', unsafe_allow_html=True)
        edu_conv = filtered_df.groupby('education')['converted'].mean().mul(100).round(2).reset_index()
        st.plotly_chart(make_chart(edu_conv['education'], edu_conv['converted'], "#0080ff", height=180), use_container_width=True, config={"displayModeBar": False})

st.markdown('<div class="glow-divider"></div>', unsafe_allow_html=True)
st.markdown('<p style="font-family:Share Tech Mono;font-size:0.6rem;color:rgba(0,255,242,0.2);text-align:center;letter-spacing:0.2em;">NEURALBANK ANALYTICS SYSTEM v1.0 ▸ DURGESH CHOUBEY ▸ POWERED BY GROQ + LANGCHAIN</p>', unsafe_allow_html=True)
