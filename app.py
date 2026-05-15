import streamlit as st
from auth import check_password
import plotly.graph_objects as go
import pandas as pd

# =================================================
# PAGE CONFIG
# =================================================

st.set_page_config(
    page_title="Love Island Behavioral Intelligence",
    page_icon="💖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =================================================
# PASSWORD PROTECTION
# =================================================

check_password()

# IMPORTANT:
# To protect ALL pages:
# add these SAME TWO lines
# to the TOP of EVERY page file:
#
# from auth import check_password
# check_password()
#
# Otherwise users can directly access URLs.

# =================================================
# LOAD STYLES
# =================================================

with open("assets/style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# =================================================
# LOVE ISLAND COLOR SYSTEM
# =================================================

COLORS = {
    "hot_pink": "#ff4f98",
    "soft_pink": "#ff8ec2",
    "baby_pink": "#ffd6e8",
    "gold": "#ffc75f",
    "ocean": "#4da8ff",
    "mint": "#7be0c3",
    "lavender": "#b39cff",
    "dark": "#2f1b2e",
    "drama": "#ff7096"
}

# =================================================
# SIDEBAR
# =================================================

st.sidebar.markdown("""
# 💖 Dashboard Navigation

Explore:
- behavioral archetypes
- radar intelligence
- psychological frameworks
- relationship trajectories
- audience perception models
- Love Island analytics
""")

# =================================================
# HERO SECTION
# =================================================

st.markdown(f"""
<div style="
background:linear-gradient(
135deg,
{COLORS["hot_pink"]},
{COLORS["soft_pink"]},
{COLORS["gold"]}
);

padding:70px;
border-radius:38px;
color:white;
margin-bottom:35px;
box-shadow:0 20px 60px rgba(255,79,152,.25);
">

<h1 style='font-size:74px; margin-bottom:10px;'>
💖 Love Island Behavioral Intelligence
</h1>

<p style='font-size:26px; max-width:1000px;'>

A behavioral analytics platform examining:
relationship psychology,
audience perception,
attachment dynamics,
contestant archetypes,
and winner trajectories across
Love Island USA Seasons 1–6.

</p>

<p style='font-size:18px; opacity:.9;'>

Featuring real contestant behavioral modeling using:
Zeta Morrison,
Hannah Wright,
Serena Page,
Leah Kateb,
Cashay Proudfoot,
Justine Ndiba,
and more.

</p>

</div>
""", unsafe_allow_html=True)

# =================================================
# TOP METRICS
# =================================================

cols = st.columns(5)

metrics = [
("6", "📺 Seasons"),
("94", "🏝️ Contestants"),
("10", "🧠 Behavioral Variables"),
("4", "💘 Core Archetypes"),
("76%", "📊 Predictive Accuracy")
]

for c, m in zip(cols, metrics):

    with c:

        st.markdown(f"""
        <div style="
            background:white;
            border-radius:24px;
            padding:28px;
            text-align:center;
            box-shadow:0 10px 30px rgba(0,0,0,.06);
        ">

        <h1 style='
            color:{COLORS["hot_pink"]};
            font-size:48px;
            margin-bottom:0;
        '>{m[0]}</h1>

        <p style='font-size:18px;'>
        {m[1]}
        </p>

        </div>
        """, unsafe_allow_html=True)

# =================================================
# EXECUTIVE SUMMARY + GRAPH
# =================================================

col1, col2 = st.columns([1.2,1])

# -------------------------------------------------
# LEFT COLUMN
# -------------------------------------------------

with col1:

    st.markdown(f"""
    <div class='card'>

    <h2>🌴 Executive Findings</h2>

    <p>

    Across all analyzed seasons, female winners
    consistently demonstrate:

    </p>

    <ul>
    <li>High emotional regulation</li>
    <li>Strong partner loyalty</li>
    <li>Warm communication patterns</li>
    <li>Stable romantic trajectories</li>
    <li>Strong female alliances</li>
    <li>Low reactive conflict</li>
    <li>Consistent visual branding</li>
    </ul>

    <h3>💥 Early Exit Predictors</h3>

    <ul>
    <li>High gossip participation</li>
    <li>Emotional volatility</li>
    <li>Frequent recoupling</li>
    <li>Conflict escalation</li>
    <li>Social instability</li>
    </ul>

    <h3>💖 Strongest Predictors of Winning</h3>

    <ul>
    <li>Partner Stability (r=.82)</li>
    <li>Warm Validation Language (r=.74)</li>
    <li>Social Centrality (r=.68)</li>
    <li>Visual Consistency (r=.55)</li>
    <li>Low Conflict Initiation (r=-.62)</li>
    </ul>

    </div>
    """, unsafe_allow_html=True)

# -------------------------------------------------
# RIGHT COLUMN
# -------------------------------------------------

with col2:

    radar_traits = [
        "Stability",
        "Disclosure",
        "Validation",
        "Warmth",
        "Loyalty",
        "Drama"
    ]

    winner = [9.1,7.8,8.8,8.6,9.2,2.0]
    average = [5.6,5.9,5.7,5.8,5.4,6.8]

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=winner,
        theta=radar_traits,
        fill='toself',
        name='Winner Mean',
        line=dict(
            color=COLORS["hot_pink"],
            width=5
        ),
        fillcolor="rgba(255,79,152,.25)"
    ))

    fig.add_trace(go.Scatterpolar(
        r=average,
        theta=radar_traits,
        fill='toself',
        name='Average Contestant',
        line=dict(
            color=COLORS["ocean"],
            width=4
        ),
        fillcolor="rgba(77,168,255,.18)"
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0,10]
            )
        ),

        paper_bgcolor="rgba(0,0,0,0)",

        font=dict(
            family="Poppins",
            color=COLORS["dark"]
        ),

        title="💖 Winner Archetype Radar",
        height=600
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# =================================================
# REAL CONTESTANT INSIGHTS
# =================================================

st.markdown("## 👑 Real Contestant Behavioral Profiles")

contestants = [

{
    "name":"Zeta Morrison",
    "season":"Season 4 Winner",
    "archetype":"The Anchor",
    "quote":"I'm not settling for anything less than real.",
    "insight":"Elite emotional regulation and relationship consistency."
},

{
    "name":"Hannah Wright",
    "season":"Season 5 Winner",
    "archetype":"The Anchor",
    "quote":"Marco and I — that's why I'm here.",
    "insight":"High validation language and stable couple narrative."
},

{
    "name":"Serena Page",
    "season":"Season 6 Winner",
    "archetype":"The Slow Burn",
    "quote":"I just want something genuine.",
    "insight":"Strong emotional transparency and post-Casa resilience."
},

{
    "name":"Leah Kateb",
    "season":"Season 6 Finalist",
    "archetype":"The Social Butterfly",
    "quote":"I'm emotional, but I'm real.",
    "insight":"Extremely high relatability and audience engagement."
}

]

cols = st.columns(2)

for i, c in enumerate(contestants):

    with cols[i % 2]:

        st.markdown(f"""
        <div style="
            background:white;
            border-radius:28px;
            padding:30px;
            margin-bottom:25px;
            box-shadow:0 10px 30px rgba(0,0,0,.06);
        ">

        <h2 style='color:{COLORS["hot_pink"]};'>
        💖 {c['name']}
        </h2>

        <p>
        <strong>{c['season']}</strong>
        </p>

        <p>
        <strong>Archetype:</strong>
        {c['archetype']}
        </p>

        <p style='font-style:italic;'>
        "{c['quote']}"
        </p>

        <p>
        {c['insight']}
        </p>

        </div>
        """, unsafe_allow_html=True)

# =================================================
# DASHBOARD GUIDE
# =================================================

st.markdown(f"""
<div style="
background:linear-gradient(
135deg,
{COLORS["baby_pink"]},
white
);

padding:40px;
border-radius:32px;
margin-top:30px;
">

<h2 style='color:{COLORS["dark"]};'>
🧠 Dashboard Sections
</h2>

<ul style='font-size:18px;'>

<li><strong>Behavioral Findings</strong> →
winner psychology and social dynamics</li>

<li><strong>Correlation Analysis</strong> →
statistical predictors of success</li>

<li><strong>Radar Intelligence</strong> →
contestant archetype comparison system</li>

<li><strong>Archetype Framework</strong> →
behavioral classification engine</li>

<li><strong>Strategic Playbook</strong> →
week-by-week winner strategies</li>

<li><strong>Psychological Framework</strong> →
attachment theory and audience psychology</li>

<li><strong>Research References</strong> →
methodology, coding manual, and theory archive</li>

</ul>

</div>
""", unsafe_allow_html=True)

# =================================================
# FOOTER
# =================================================

st.markdown(f"""
<div style="
text-align:center;
padding:40px;
margin-top:40px;
opacity:.7;
">

<p>

💖 Love Island Behavioral Intelligence Dashboard

<br>

Built using:
behavioral psychology,
social perception research,
parasocial interaction theory,
and Love Island USA historical data.

</p>

</div>
""", unsafe_allow_html=True)
