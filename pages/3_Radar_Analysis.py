import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# ------------------------------------------------
# LOAD STYLES
# ------------------------------------------------

with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------

st.set_page_config(
    page_title="Love Island Radar Intelligence",
    page_icon="💖",
    layout="wide"
)

# ------------------------------------------------
# LOVE ISLAND COLOR SYSTEM
# ------------------------------------------------

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

# ------------------------------------------------
# PAGE TITLE
# ------------------------------------------------

st.title("💖 Winner Archetype Radar Intelligence")

st.markdown("""
Explore how contestants align with the historical
Love Island winner archetype across emotional,
social, and relationship variables.
""")

# ------------------------------------------------
# TRAITS
# ------------------------------------------------

traits = [
    "❤️ Stability",
    "💬 Disclosure",
    "😎 Humor",
    "💗 Validation",
    "🌴 Sentiment",
    "🔥 Centrality",
    "💞 Loyalty",
    "🚫 Drama"
]

# ------------------------------------------------
# REAL CONTESTANT DATA
# ------------------------------------------------

contestants = {

    "Zeta Morrison (S4 Winner)": {
        "scores": [9.2, 7.4, 6.3, 9.0, 8.4, 7.2, 9.4, 8.6],
        "quote": "I'm not settling for anything less than real.",
        "archetype": "The Anchor",
        "summary": """
Emotionally stable, low-drama relationship strategy.
Maintained strong female alliances while reinforcing
one primary romantic connection.
""",
        "partner": "Timmy",
        "winner_score": 94
    },

    "Hannah Wright (S5 Winner)": {
        "scores": [8.8, 7.8, 6.8, 8.9, 8.0, 7.4, 9.1, 8.3],
        "quote": "Marco and I — that's why I'm here.",
        "archetype": "The Anchor",
        "summary": """
Strong validation language, stable relationship arc,
audience-friendly emotional warmth,
minimal unnecessary conflict.
""",
        "partner": "Marco",
        "winner_score": 92
    },

    "Serena Page (S6 Winner)": {
        "scores": [7.9, 8.6, 6.5, 8.2, 8.8, 8.1, 8.4, 6.7],
        "quote": "I just want something genuine.",
        "archetype": "The Slow Burn",
        "summary": """
Started slower socially but gained audience support
through emotional transparency and post-Casa resilience.
""",
        "partner": "Kordell",
        "winner_score": 89
    },

    "Leah Kateb (S6 Finalist)": {
        "scores": [6.9, 9.0, 7.3, 7.4, 9.2, 8.8, 6.8, 4.7],
        "quote": "I'm emotional, but I'm real.",
        "archetype": "The Social Butterfly",
        "summary": """
Extremely high relatability and disclosure.
Strong audience engagement but more volatile
romantic positioning.
""",
        "partner": "Miguel",
        "winner_score": 81
    },

    "Justine Ndiba (S2 Winner)": {
        "scores": [8.7, 7.2, 6.0, 8.8, 7.6, 7.0, 9.0, 8.5],
        "quote": "I wanted something real from the beginning.",
        "archetype": "The Anchor",
        "summary": """
One of the strongest stability profiles in franchise history.
Low drama, high emotional consistency.
""",
        "partner": "Caleb",
        "winner_score": 91
    },

    "Cashay Proudfoot (S3 Fan Favorite)": {
        "scores": [6.0, 8.7, 8.2, 8.0, 9.0, 9.1, 5.8, 4.3],
        "quote": "I wear my heart on my sleeve.",
        "archetype": "The Social Butterfly",
        "summary": """
Elite social centrality and audience relatability.
More unstable romantic trajectory reduced winner probability.
""",
        "partner": "Cinco",
        "winner_score": 76
    },

    "Kassy Castillo (S5 Finalist)": {
        "scores": [5.8, 8.9, 7.5, 6.6, 8.7, 8.4, 4.9, 3.2],
        "quote": "I'm trying to follow my heart.",
        "archetype": "The Chaos Romantic",
        "summary": """
High emotional expressiveness and audience entertainment value
but major volatility during Casa Amor.
""",
        "partner": "Leo",
        "winner_score": 67
    },

    "Destiny Davis (S5)": {
        "scores": [5.2, 5.6, 5.4, 5.0, 5.8, 7.3, 4.6, 3.1],
        "quote": "I'm not going to chase anyone.",
        "archetype": "The Independent",
        "summary": """
Strong confidence and boundaries but struggled
to form stable long-term romantic attachment.
""",
        "partner": "Multiple",
        "winner_score": 58
    }
}

# ------------------------------------------------
# WINNER ZONE SHADOW
# ------------------------------------------------

winner_min = [6.8,6.7,5.8,7.0,6.5,6.2,7.4,5.8]
winner_max = [9.0,8.6,7.5,9.1,8.5,8.2,9.2,8.4]

winner_mean = [7.8,7.4,6.8,7.9,7.1,7.2,8.1,6.9]

# ------------------------------------------------
# TABS
# ------------------------------------------------

tab1, tab2, tab3, tab4 = st.tabs([
    "💘 Contestant Radar",
    "🏝️ Casa Amor Delta",
    "💞 Couple Compatibility",
    "🔥 Season Comparison"
])

# ------------------------------------------------
# TAB 1 — CONTESTANT RADAR
# ------------------------------------------------

with tab1:

    selected = st.selectbox(
        "Choose Contestant",
        list(contestants.keys())
    )

    compare = st.multiselect(
        "Compare Contestants",
        list(contestants.keys()),
        default=[selected]
    )

    fig = go.Figure()

    # Winner Shadow Max

    fig.add_trace(go.Scatterpolar(
        r=winner_max,
        theta=traits,
        fill='toself',
        opacity=.15,
        line=dict(color=COLORS["gold"]),
        name="Winner Zone Max"
    ))

    # Winner Shadow Min

    fig.add_trace(go.Scatterpolar(
        r=winner_min,
        theta=traits,
        fill='toself',
        opacity=.08,
        line=dict(color=COLORS["baby_pink"]),
        name="Winner Zone Min"
    ))

    # Winner Mean

    fig.add_trace(go.Scatterpolar(
        r=winner_mean,
        theta=traits,
        fill='toself',
        opacity=.25,
        line=dict(
            color=COLORS["hot_pink"],
            width=4
        ),
        name="Winner Mean"
    ))

    palette = [
        COLORS["hot_pink"],
        COLORS["ocean"],
        COLORS["gold"],
        COLORS["mint"],
        COLORS["lavender"]
    ]

    # Contestants

    for i, name in enumerate(compare):

        fig.add_trace(go.Scatterpolar(
            r=contestants[name]["scores"],
            theta=traits,
            fill='toself',
            opacity=.35,
            line=dict(
                color=palette[i % len(palette)],
                width=4
            ),
            name=name
        ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0,10]
            )
        ),

        paper_bgcolor="rgba(0,0,0,0)",
        height=800,

        title="💖 Winner Archetype Comparison Radar",

        font=dict(
            family="Poppins",
            size=14,
            color=COLORS["dark"]
        )
    )

    st.plotly_chart(fig, use_container_width=True)

    # ------------------------------------------------
    # CONTESTANT INSIGHT CARD
    # ------------------------------------------------

    selected_data = contestants[selected]

    st.markdown(f"""
    <div class='card'>

    ## 💖 Contestant Intelligence Profile

    ### 👑 {selected}

    **Primary Archetype:** {selected_data['archetype']}

    **Partner Association:** {selected_data['partner']}

    ### 💬 Representative Quote

    *"{selected_data['quote']}"*

    ### 🌴 Behavioral Summary

    {selected_data['summary']}

    </div>
    """, unsafe_allow_html=True)

    # ------------------------------------------------
    # METRICS
    # ------------------------------------------------

    winner_score = selected_data["winner_score"]

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "👑 Winner Alignment",
            f"{winner_score}%"
        )

    with col2:

        if winner_score >= 85:
            label = "Winner Tier"

        elif winner_score >= 70:
            label = "Finalist Tier"

        elif winner_score >= 55:
            label = "Mid Villa"

        else:
            label = "Early Exit Risk"

        st.metric(
            "🏝️ Predicted Placement",
            label
        )

    with col3:

        stability = selected_data["scores"][0]
        drama = selected_data["scores"][7]

        compatibility = round((stability + drama) * 5,1)

        st.metric(
            "💞 Public Vote Potential",
            f"{compatibility}%"
        )

# ------------------------------------------------
# TAB 2 — CASA AMOR DELTA
# ------------------------------------------------

with tab2:

    pre_casa = [8.1,7.2,6.8,8.0,7.9,6.8,8.7,7.9]
    post_casa = [5.2,8.0,5.9,6.1,5.5,7.9,3.4,2.1]

    fig2 = go.Figure()

    fig2.add_trace(go.Scatterpolar(
        r=pre_casa,
        theta=traits,
        fill='toself',
        name="Pre Casa",
        line_color=COLORS["hot_pink"]
    ))

    fig2.add_trace(go.Scatterpolar(
        r=post_casa,
        theta=traits,
        fill='toself',
        name="Post Casa",
        line_color=COLORS["ocean"]
    ))

    fig2.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0,10]
            )
        ),
        height=700,
        title="🏝️ Casa Amor Delta Radar"
    )

    st.plotly_chart(fig2, use_container_width=True)

# ------------------------------------------------
# TAB 3 — COUPLE COMPATIBILITY
# ------------------------------------------------

with tab3:

    person_a = st.selectbox(
        "Select Partner A",
        list(contestants.keys()),
        index=0
    )

    person_b = st.selectbox(
        "Select Partner B",
        list(contestants.keys()),
        index=1
    )

    fig3 = go.Figure()

    fig3.add_trace(go.Scatterpolar(
        r=contestants[person_a]["scores"],
        theta=traits,
        fill='toself',
        name=person_a,
        line_color=COLORS["hot_pink"]
    ))

    fig3.add_trace(go.Scatterpolar(
        r=contestants[person_b]["scores"],
        theta=traits,
        fill='toself',
        name=person_b,
        line_color=COLORS["ocean"]
    ))

    fig3.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0,10]
            )
        ),
        height=700,
        title="💞 Couple Compatibility Overlay"
    )

    st.plotly_chart(fig3, use_container_width=True)

    a = np.array(contestants[person_a]["scores"])
    b = np.array(contestants[person_b]["scores"])

    compatibility = round(
        100 - np.mean(np.abs(a-b))*10,
        1
    )

    st.metric(
        "💘 Compatibility Score",
        f"{compatibility}%"
    )

# ------------------------------------------------
# TAB 4 — SEASON COMPARISON
# ------------------------------------------------

with tab4:

    season_data = {
        "Season 2 Winner":[8.7,7.2,6.0,8.8,7.6,7.0,9.0,8.5],

        "Season 4 Winner":[9.2,7.4,6.3,9.0,8.4,7.2,9.4,8.6],

        "Season 5 Winner":[8.8,7.8,6.8,8.9,8.0,7.4,9.1,8.3],

        "Season 6 Winner":[7.9,8.6,6.5,8.2,8.8,8.1,8.4,6.7]
    }

    fig4 = go.Figure()

    colors = [
        COLORS["hot_pink"],
        COLORS["gold"],
        COLORS["ocean"],
        COLORS["mint"]
    ]

    for i, (name, vals) in enumerate(season_data.items()):

        fig4.add_trace(go.Scatterpolar(
            r=vals,
            theta=traits,
            fill='toself',
            name=name,
            line_color=colors[i]
        ))

    fig4.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0,10]
            )
        ),
        height=750,
        title="🔥 Season-by-Season Winner Evolution"
    )

    st.plotly_chart(fig4, use_container_width=True)

    st.markdown("""
    ### 🌴 Historical Winner Evolution

    Earlier seasons rewarded:
    - stability
    - loyalty
    - relationship consistency

    Newer seasons increasingly reward:
    - emotional transparency
    - relatability
    - audience vulnerability
    """)
