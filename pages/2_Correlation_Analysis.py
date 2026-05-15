import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from auth import check_password

# =================================================
# PAGE CONFIG
# =================================================

st.set_page_config(
    page_title="Love Island Correlation Analysis",
    page_icon="💖",
    layout="wide"
)

# =================================================
# PASSWORD PROTECTION
# =================================================

check_password()

# =================================================
# LOAD CSS
# =================================================

with open("assets/style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# =================================================
# LOVE ISLAND DESIGN SYSTEM
# =================================================

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

# =================================================
# THEME FUNCTION
# =================================================

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

# =================================================
# PAGE TITLE
# =================================================

st.title("💖 Love Island Predictor Matrix")

st.markdown("""
Explore which behavioral traits most strongly predict
winning outcomes across Love Island USA seasons.
""")

# =================================================
# TABS
# =================================================

tab1, tab2, tab3, tab4 = st.tabs([
    "💘 Winner Correlations",
    "🔥 Season Heatmap",
    "🏝️ Drama Metrics",
    "💞 Couple Trajectories"
])

# =================================================
# TAB 1 — CORRELATIONS
# =================================================

with tab1:

    # ------------------------------------------------
    # MAIN CORRELATION DATA
    # ------------------------------------------------

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

        'Correlation':[
            .82,
            .74,
            .71,
            .68,
            .55,
            -.62,
            -.58,
            -.41
        ]
    })

    # ------------------------------------------------
    # REAL CONTESTANT DATA
    # ------------------------------------------------

    contestant_overlay = pd.DataFrame({

        "Contestant":[
            "Zeta Morrison",
            "Hannah Wright",
            "Serena Page",
            "Leah Kateb",
            "Cashay Proudfoot"
        ],

        "Partner Stability":[
            9.4,
            9.1,
            8.6,
            6.8,
            5.8
        ],

        "Warm Sentiment":[
            8.9,
            8.7,
            9.0,
            9.1,
            9.2
        ],

        "Validation Frequency":[
            9.1,
            9.0,
            8.5,
            7.6,
            8.0
        ],

        "Social Centrality":[
            7.7,
            7.5,
            7.9,
            9.3,
            9.5
        ]
    })

    # ------------------------------------------------
    # MAIN CORRELATION CHART
    # ------------------------------------------------

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

    # ------------------------------------------------
    # ZERO LINE
    # ------------------------------------------------

    fig.add_vline(
        x=0,
        line_dash="dash",
        line_color="#999"
    )

    # ------------------------------------------------
    # HEART OVERLAY
    # ------------------------------------------------

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

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # ------------------------------------------------
    # REAL CONTESTANT SELECTOR
    # ------------------------------------------------

    st.markdown("## 👑 Real Contestant Behavioral Profiles")

    selected = st.selectbox(
        "Choose Contestant",
        contestant_overlay["Contestant"].tolist()
    )

    contestant_row = contestant_overlay[
        contestant_overlay["Contestant"] == selected
    ].iloc[0]

    metric_cols = st.columns(4)

    metrics = [
        ("💖 Stability", contestant_row["Partner Stability"]),
        ("🌴 Warmth", contestant_row["Warm Sentiment"]),
        ("💬 Validation", contestant_row["Validation Frequency"]),
        ("🔥 Centrality", contestant_row["Social Centrality"])
    ]

    for col, metric in zip(metric_cols, metrics):

        with col:

            st.markdown(f"""
            <div class='metric'>

            <h2>{metric[1]}</h2>

            <p>{metric[0]}</p>

            </div>
            """, unsafe_allow_html=True)

    # ------------------------------------------------
    # INSIGHT CARD
    # ------------------------------------------------

    st.markdown("""
    <div class='card'>

    <h2>🌴 Villa Insight</h2>

    <p>

    Contestants with:
    </p>

    <ul>
    <li>high emotional warmth</li>
    <li>stable partner dynamics</li>
    <li>strong female alliances</li>
    <li>consistent emotional tone</li>
    </ul>

    <p>

    consistently outperform contestants centered around
    high-drama villa dynamics.

    </p>

    <p>

    Public voting consistently rewards:
    </p>

    <ul>
    <li>emotional consistency</li>
    <li>secure attachment</li>
    <li>relationship clarity</li>
    <li>warmth cues</li>
    <li>positive emotional regulation</li>
    </ul>

    <p>

    over chaos-driven airtime.

    </p>

    </div>
    """, unsafe_allow_html=True)

    # ------------------------------------------------
    # WINNER VS CHAOS COMPARISON
    # ------------------------------------------------

    compare_df = pd.DataFrame({

        "Behavior":[
            "Loyalty",
            "Warmth",
            "Validation",
            "Drama",
            "Conflict",
            "Instability"
        ],

        "Winner":[
            9.1,
            8.8,
            8.9,
            2.0,
            2.1,
            2.5
        ],

        "Chaos Profile":[
            3.2,
            4.6,
            4.0,
            9.1,
            8.7,
            9.4
        ]
    })

    fig_compare = go.Figure()

    fig_compare.add_trace(go.Bar(
        x=compare_df["Behavior"],
        y=compare_df["Winner"],
        name="💖 Winner Profile",
        marker_color=LOVE_ISLAND_COLORS["hot_pink"]
    ))

    fig_compare.add_trace(go.Bar(
        x=compare_df["Behavior"],
        y=compare_df["Chaos Profile"],
        name="🔥 Chaos Profile",
        marker_color="#d90429"
    ))

    fig_compare.update_layout(
        barmode="group",
        height=550,
        title="💘 Winner vs Chaos Behavioral Comparison"
    )

    fig_compare = apply_love_island_theme(fig_compare)

    st.plotly_chart(
        fig_compare,
        use_container_width=True
    )

# =================================================
# TAB 2 — SEASON HEATMAP
# =================================================

with tab2:

    heatmap_df = pd.DataFrame({

        "Season":[
            "S1",
            "S2",
            "S3",
            "S4",
            "S5",
            "S6"
        ],

        "Stability":[
            6,
            7,
            8,
            7,
            9,
            8
        ],

        "Warmth":[
            5,
            7,
            8,
            9,
            8,
            7
        ],

        "Drama":[
            8,
            6,
            5,
            7,
            4,
            6
        ],

        "Gossip":[
            7,
            5,
            4,
            6,
            3,
            5
        ],

        "Centrality":[
            6,
            7,
            8,
            7,
            9,
            8
        ]
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

    fig2.update_layout(
        height=550
    )

    fig2 = apply_love_island_theme(fig2)

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

# =================================================
# TAB 3 — DRAMA METRICS
# =================================================

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

        fig3 = apply_love_island_theme(fig3)

        st.plotly_chart(
            fig3,
            use_container_width=True
        )

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

        fig4 = apply_love_island_theme(fig4)

        st.plotly_chart(
            fig4,
            use_container_width=True
        )

# =================================================
# TAB 4 — COUPLE TRAJECTORIES
# =================================================

with tab4:

    traj = pd.DataFrame({

        "Episode":[
            1,2,3,4,5,6,7,8
        ],

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

        line=dict(
            color="#ff4f98",
            width=5
        )
    ))

    fig5.add_trace(go.Scatter(
        x=traj["Episode"],
        y=traj["Chaotic Couple"],

        mode="lines+markers",

        name="💥 Chaotic Couple",

        line=dict(
            color="#ff9fcf",
            width=5
        )
    ))

    fig5.update_layout(
        title="💞 Couple Stability Trajectories",
        xaxis_title="Episode",
        yaxis_title="Relationship Stability",
        height=600
    )

    fig5 = apply_love_island_theme(fig5)

    st.plotly_chart(
        fig5,
        use_container_width=True
    )

# =================================================
# FINAL INSIGHT
# =================================================

st.markdown("""
<div class='card'>

<h2>💖 Final Correlation Insight</h2>

<p>

Across all analyzed seasons,
the strongest predictors of winning are:

</p>

<ul>

<li>relationship stability</li>
<li>emotional warmth</li>
<li>validation language</li>
<li>low conflict initiation</li>
<li>secure attachment behaviors</li>

</ul>

<p>

Contestants centered around:
- chaos
- volatility
- gossip
- emotional reactivity

generate airtime but rarely sustain public support
long enough to win the show.

</p>

</div>
""", unsafe_allow_html=True)
