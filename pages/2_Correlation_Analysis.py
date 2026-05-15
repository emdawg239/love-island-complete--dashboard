import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from auth import check_password

check_password()


# ------------------------------------------------
# LOVE ISLAND DESIGN SYSTEM
# ------------------------------------------------

LOVE_ISLAND_COLORS = {
    "hot_pink": "#ff4f98",
    "soft_pink": "#ff8ec2",
    "baby_pink": "#ffd6e8",
    "sunset": "#ff9671",
    "gold": "#ffc75f",
    "ocean": "#4da8ff",
    "mint": "#7be0c3",
    "lavender": "#b39cff",
    "cream": "#fff8f3",
    "dark": "#2f1b2e"
}

WINNER_COLOR_SCALE = [
    LOVE_ISLAND_COLORS["baby_pink"],
    LOVE_ISLAND_COLORS["soft_pink"],
    LOVE_ISLAND_COLORS["hot_pink"]
]

DRAMA_SCALE = [
    "#ffe5ec",
    "#ff7096",
    "#d90429"
]


def apply_love_island_theme(fig):

    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",

        font=dict(
            family="Poppins",
            color=LOVE_ISLAND_COLORS["dark"],
            size=14
        ),

        title_font=dict(
            size=24,
            color=LOVE_ISLAND_COLORS["dark"]
        ),

        margin=dict(
            l=20,
            r=20,
            t=60,
            b=20
        ),

        legend=dict(
            bgcolor="rgba(255,255,255,.6)",
            borderwidth=0
        )
    )

    return fig

with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("💖 Love Island Predictor Matrix")

st.markdown("""
Explore which behavioral traits most strongly predict
winning outcomes across Love Island USA seasons.
""")

# ------------------------------------------------
# TABS
# ------------------------------------------------

tab1, tab2, tab3, tab4 = st.tabs([
    "💘 Winner Correlations",
    "🔥 Season Heatmap",
    "🏝️ Drama Metrics",
    "💞 Couple Trajectories"
])

# ------------------------------------------------
# TAB 1 — CORRELATIONS
# ------------------------------------------------

with tab1:

    df = pd.DataFrame({
        'Trait':[
            'Partner Stability',
            'Warm Sentiment',
            'Validation Frequency',
            'Social Centrality',
            'Consistent Color Palette',
            'Low Conflict Initiation',
            'Gossip Participation',
            'Outfit Volatility'
        ],

        'Correlation':[.82,.74,.71,.68,.55,-.62,-.58,-.41]
    })

    winner_overlay = pd.DataFrame({
        'Trait':[
            'Partner Stability',
            'Warm Sentiment',
            'Validation Frequency',
            'Social Centrality',
            'Consistent Color Palette',
            'Low Conflict Initiation',
            'Gossip Participation',
            'Outfit Volatility'
        ],

        'Winner Average':[8.9,8.4,8.1,7.9,7.4,8.2,2.1,3.0]
    })

    fig = px.bar(
    df,
    x="Correlation",
    y="Trait",
    orientation="h",
    color="Correlation",
    color_continuous_scale=WINNER_COLOR_SCALE,
    text="Correlation",
    title="💖 Winner Behavioral Correlations"
)

fig.update_traces(
    texttemplate='%{text:.2f}',
    textposition='outside'
)

fig.add_vline(
    x=0,
    line_dash="dash",
    line_color="#999"
)

fig.add_trace(
    go.Scatter(
        x=df["Correlation"],
        y=df["Trait"],
        mode="markers+text",
        marker=dict(
            size=22,
            color=LOVE_ISLAND_COLORS["hot_pink"],
            symbol="diamond"
        ),
        text=["❤️"] * len(df),
        textposition="middle right",
        name="Winner Traits"
    )
)

fig = apply_love_island_theme(fig)

st.plotly_chart(fig, use_container_width=True)

   st.markdown("""
<div class='card'>

## 🌴 Villa Insight

Contestants with:
- high emotional warmth
- stable partner dynamics
- strong female alliances

consistently outperform contestants centered around
high-drama villa dynamics.

Public voting appears to reward:
- emotional consistency
- secure attachment
- relationship clarity

over chaos-driven airtime.

</div>
""", unsafe_allow_html=True)

# ------------------------------------------------
# TAB 2 — HEATMAP
# ------------------------------------------------

with tab2:

    heatmap_df = pd.DataFrame({
        "Season":["S1","S2","S3","S4","S5","S6"],
        "Stability":[6,7,8,7,9,8],
        "Warmth":[5,7,8,9,8,7],
        "Drama":[8,6,5,7,4,6],
        "Gossip":[7,5,4,6,3,5],
        "Centrality":[6,7,8,7,9,8]
    })

    fig2 = px.imshow(
        heatmap_df.set_index("Season"),
        text_auto=True,
        color_continuous_scale=[
            "#ffe5f1",
            "#ff8ec2",
            "#ff4f98"
        ],
        aspect="auto",
        title="🔥 Season-by-Season Villa Dynamics"
    )

    fig2.update_layout(height=550)

    st.plotly_chart(fig2, use_container_width=True)

    st.markdown("""
    ### 🌴 Key Findings

    - Seasons with lower chaos produce more stable winners
    - High warmth seasons tend to create audience-favorite couples
    - Chaotic seasons generate airtime but lower public trust
    """)

# ------------------------------------------------
# TAB 3 — DRAMA METRICS
# ------------------------------------------------

with tab3:

    drama_df = pd.DataFrame({
        "Contestant":[
            "Average Villa Girl",
            "Typical Winner",
            "Casa Chaos Queen",
            "Social Butterfly"
        ],

        "Drama Index":[
            6.8,
            2.1,
            9.4,
            5.8
        ],

        "Casa Amor Survival":[
            5.0,
            9.1,
            2.2,
            6.0
        ]
    })

    col1, col2 = st.columns(2)

    with col1:

        fig3 = px.bar(
            drama_df,
            x="Contestant",
            y="Drama Index",
            color="Drama Index",
            title="🔥 Drama Index",
            color_continuous_scale=[
                "#ffd6e8",
                "#ff4f98"
            ]
        )

        st.plotly_chart(fig3, use_container_width=True)

    with col2:

        fig4 = px.bar(
            drama_df,
            x="Contestant",
            y="Casa Amor Survival",
            color="Casa Amor Survival",
            title="🏝️ Casa Amor Survival Score",
            color_continuous_scale=[
                "#ffe5f1",
                "#ff4f98"
            ]
        )

        st.plotly_chart(fig4, use_container_width=True)

    st.markdown("""
    ### 💥 Observations

    Winners consistently score:
    - LOW on Drama Index
    - HIGH on Casa Survival

    Contestants who emotionally spiral during Casa Amor
    rarely recover in public perception.
    """)

# ------------------------------------------------
# TAB 4 — COUPLE TRAJECTORIES
# ------------------------------------------------

with tab4:

    traj = pd.DataFrame({
        "Episode":[1,2,3,4,5,6,7,8],

        "Winner Couple":[
            5,
            6,
            7,
            7,
            8,
            8,
            9,
            9
        ],

        "Chaotic Couple":[
            8,
            9,
            6,
            4,
            5,
            2,
            1,
            0
        ]
    })

    fig5 = go.Figure()

    fig5.add_trace(go.Scatter(
        x=traj["Episode"],
        y=traj["Winner Couple"],
        mode="lines+markers",
        name="💖 Winner Couple",
        line=dict(color="#ff4f98", width=5)
    ))

    fig5.add_trace(go.Scatter(
        x=traj["Episode"],
        y=traj["Chaotic Couple"],
        mode="lines+markers",
        name="💥 Chaotic Couple",
        line=dict(color="#ff9fcf", width=5)
    ))

    fig5.update_layout(
        title="💞 Couple Stability Trajectories",
        xaxis_title="Episode",
        yaxis_title="Relationship Stability",
        height=600
    )

    st.plotly_chart(fig5, use_container_width=True)

    st.markdown("""
    ### 💘 Arc Analysis

    Winning couples tend to:
    - gradually increase in emotional stability
    - recover smoothly from conflict
    - maintain audience trust

    Chaotic couples:
    - spike early
    - collapse post-Casa
    - generate drama but lose public votes
    """)
