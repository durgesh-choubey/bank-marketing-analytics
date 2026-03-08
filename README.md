<div align="center">

```
███╗   ██╗███████╗██╗   ██╗██████╗  █████╗██╗              ██████╗  █████╗ ███╗  ██╗██╗  ██╗
████╗  ██║██╔════╝██║   ██║██╔══██╗██╔══██╗██║             ██╔══██╗██╔══██╗████╗ ██║██║ ██╔╝
██╔██╗ ██║█████╗  ██║   ██║██████╔╝███████║██║             ██████╔╝███████║██╔██╗██║█████╔╝ 
██║╚██╗██║██╔══╝  ██║   ██║██╔══██╗██╔══██║██║             ██╔══██╗██╔══██║██║╚████║██╔═██╗ 
██║ ╚████║███████╗╚██████╔╝██║  ██║██║  ██║███████╗        ██████╔╝██║  ██║██║ ╚███║██║  ██╗
╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝        ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚══╝╚═╝  ╚═╝
```

### `[ RAG-POWERED CONVERSATIONAL MARKETING INTELLIGENCE SYSTEM ]`

![Python](https://img.shields.io/badge/Python-3.10+-00fff2?style=for-the-badge&logo=python&logoColor=black)
![Streamlit](https://img.shields.io/badge/Streamlit-1.x-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-Core-1C3C3C?style=for-the-badge&logo=chainlink&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-LLaMA_3.3_70B-F54E00?style=for-the-badge)
![Plotly](https://img.shields.io/badge/Plotly-Interactive-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-00fff2?style=for-the-badge)

**[`⚡ LIVE DEMO`](https://bankmarket.streamlit.app)** &nbsp;·&nbsp; **[`📊 DATASET`](https://archive.ics.uci.edu/dataset/222/bank+marketing)** &nbsp;·&nbsp; **[`👤 AUTHOR`](https://linkedin.com/in/durgeshchoubey)**

</div>

---

```bash
> SYSTEM INITIALIZING...
> LOADING BANK MARKETING DATASET.............. [45,211 RECORDS] ✓
> CONNECTING TO GROQ INFERENCE ENGINE......... [LLAMA 3.3 70B]  ✓
> BUILDING RAG PIPELINE....................... [LANGCHAIN CORE]  ✓
> RENDERING NEURAL UI......................... [STREAMLIT]       ✓
> STATUS: ONLINE — NEURAL LINK ACTIVE
```

---

## `// OVERVIEW`

**NeuralBank Analytics** is a production-grade conversational analytics engine built on the UCI Bank Marketing Dataset (45,211 records). It combines a **Retrieval-Augmented Generation (RAG) pipeline** with real-time visual intelligence — enabling any business stakeholder to query 45K+ marketing records in plain English and receive structured, data-grounded insights in seconds.

> *Ask:* `"Which contact channel maximizes conversion probability for blue-collar customers?"`
>
> *Get:* Direct answer · Key insight · Recommended action — all grounded in real statistics.

---

## `// SYSTEM ARCHITECTURE`

```
┌─────────────────────────────────────────────────────────────────┐
│  INPUT LAYER                                                    │
│  ▸ Natural language query from business stakeholder             │
│  ▸ Optional segment filters (job type, contact channel)         │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│  DATA CONTEXT ENGINE  [Pandas]                                  │
│  ▸ Conversion rates  → by segment, channel, month, education    │
│  ▸ Behavioural stats → avg call duration (converted vs not)     │
│  ▸ Demographic stats → age distribution across outcomes         │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│  PROMPT ORCHESTRATION LAYER  [LangChain Core]                   │
│  ▸ PromptTemplate injects computed data context into query      │
│  ▸ Role: Senior Marketing Data Scientist @ Financial Services   │
│  ▸ Output schema: Answer → Insight → Recommended Action         │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│  INFERENCE ENGINE  [Groq API]                                   │
│  ▸ Model: LLaMA 3.3 70B Versatile                               │
│  ▸ Temperature: 0.2  (factual grounding, low hallucination)     │
│  ▸ Latency: ~1-2s per query (Groq hardware acceleration)        │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│  RENDERING LAYER  [Streamlit + Plotly]                          │
│  ▸ Futuristic dark UI with custom CSS (Orbitron font)           │
│  ▸ 4 interactive Plotly charts + live KPI cards                 │
│  ▸ Chat interface with session state management                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## `// TECH STACK`

| `LAYER` | `TECHNOLOGY` | `PURPOSE` |
|---|---|---|
| UI Framework | Streamlit + Custom CSS | Futuristic dark-theme dashboard |
| LLM Orchestration | LangChain Core | Prompt templating & chain execution |
| Inference Engine | Groq API — LLaMA 3.3 70B | Sub-2s language model inference |
| Data Processing | Pandas, NumPy | Feature aggregation & summary stats |
| Visualizations | Plotly Graph Objects | Interactive charts with custom theming |
| Env Management | python-dotenv | Secure API key handling |
| Dataset | UCI Bank Marketing | 45,211 rows × 17 features |

---

## `// CORE MODULES`

**`[01] CONVERSATIONAL ANALYTICS ENGINE`**
```
Input  → Natural language business question
Process → Data context injection via LangChain PromptTemplate
Output → Structured insight: Answer + Key Finding + Action
```

**`[02] DYNAMIC SEGMENTATION ENGINE`**
```
Input  → Job segment filter + Contact channel filter  
Process → Real-time Pandas aggregation on filtered subset
Output → Updated KPIs + 4 Plotly charts recalculated instantly
```

**`[03] MISSION CONTROL KPI BOARD`**
```
Metrics → Total Customers | Conversions | Conversion Rate% | Avg Call Duration
Updates → Fully reactive to applied segment filters
```

**`[04] DATA INTELLIGENCE GRID`**
```
Chart 1 → Conversion rate by contact channel
Chart 2 → Conversion rate by job segment  
Chart 3 → Conversion volume by month (seasonality analysis)
Chart 4 → Conversion rate by education level
```

---

## `// DATASET PROFILE`

```
SOURCE   : UCI Machine Learning Repository
RECORDS  : 45,211 customer interactions
FEATURES : 17
           ├── Demographics  → age, job, marital, education
           ├── Financial     → balance, housing, loan, default
           ├── Campaign      → contact, duration, campaign, pdays
           └── Outcome       → previous, poutcome, y (target)
TARGET   : Binary → subscribed to term deposit [yes / no]
BASELINE : 11.7% conversion rate
DOMAIN   : Portuguese bank direct marketing campaign (2008-2010)
```

---

## `// KEY INTELLIGENCE FINDINGS`

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 CHANNEL INTELLIGENCE
 ├── cellular   → highest conversion rate
 └── unknown    → lowest ROI, avoid targeting

 SEGMENT INTELLIGENCE
 ├── retired    → top conversion segment
 ├── student    → high conversion, low volume
 └── blue-collar→ high volume, below-average conversion

 TEMPORAL INTELLIGENCE
 ├── peak months  : March · September · October
 └── avoid months : May (high volume, lowest rate)

 BEHAVIOURAL SIGNAL  ← strongest predictor
 ├── converted     → avg call duration: ~537s
 └── not converted → avg call duration: ~220s
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## `// SAMPLE QUERIES`

```bash
▸ "Which job segment has the highest conversion probability?"
▸ "What is the optimal month to run acquisition campaigns?"
▸ "How does previous campaign outcome affect current conversion?"
▸ "Which contact channel delivers the best cost-per-conversion?"
▸ "What customer profile should we prioritize for the next campaign?"
```

---

## `// LOCAL SETUP`

```bash
# 01 — Clone repository
git clone https://github.com/imdurgeshchoubey/bank-marketing-analytics.git
cd bank-marketing-analytics

# 02 — Install dependencies
pip install -r requirements.txt

# 03 — Configure API key
echo "GROQ_API_KEY=your_key_here" > .env
# Get free key → https://console.groq.com

# 04 — Add dataset
# Download bank-full.csv from UCI repo and place in project root
# https://archive.ics.uci.edu/dataset/222/bank+marketing

# 05 — Launch
streamlit run app.py
# → http://localhost:8501
```

---

## `// REPOSITORY STRUCTURE`

```
bank-marketing-analytics/
│
├── app.py                  # Core app — UI, LLM chain, Plotly charts
├── bank-full.csv           # UCI Bank Marketing dataset (45K records)
├── requirements.txt        # Python dependencies
├── .env                    # API keys (git-ignored)
├── .gitignore
└── README.md
```

---

## `// AUTHOR`

<div align="center">

```
╔══════════════════════════════════════╗
║   DURGESH CHOUBEY                   ║
║   Data Scientist & AI Engineer      ║
║   Building AI · Analytics · Tools   ║
╚══════════════════════════════════════╝
```

[![LinkedIn](https://img.shields.io/badge/LinkedIn-durgeshchoubey-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/durgeshchoubey)
[![Instagram](https://img.shields.io/badge/Instagram-ai.with.durgesh-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://instagram.com/ai.with.durgesh)
[![Live Demo](https://img.shields.io/badge/Live_Demo-bankmarket.streamlit.app-00fff2?style=for-the-badge&logo=streamlit&logoColor=black)](https://bankmarket.streamlit.app)

---

`[ BUILT WITH LANGCHAIN · GROQ · STREAMLIT · PLOTLY · UCI BANK MARKETING ]`

</div>
