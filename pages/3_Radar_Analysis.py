import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import numpy as np

from auth import check_password

# =================================================
# PAGE CONFIG
# =================================================

st.set_page_config(
    page_title="Love Island Radar Intelligence",
    page_icon="💖",
    layout="wide"
)

# =================================================
# PASSWORD PROTECTION
# =================================================

check_password()

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
    "drama": "#ff7096",
    "danger": "#d90429"
}

# =================================================
# PAGE TITLE
# =================================================

st.title("💖 Winner Archetype Radar Intelligence")

st.markdown("""
Explore how contestants align with the historical
Love Island winner archetype across emotional,
social,
and relationship variables.
""")

# =================================================
# TRAITS
# =================================================

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

# =================================================
# REAL CONTESTANT DATA
# =================================================

contestants = {

    "Zeta Morrison (S4 Winner)": {
        "scores": [9.2,7.4,6.3,9.0,8.4,7.2,9.4,8.6],
        "quote": "I'm not settling for anything less than real.",
        "archetype": "The Anchor",
        "summary": """
Emotionally stable, low-drama relationship strategy.
Maintained strong female alliances while reinforcing
one primary romantic connection.
""",
        "partner":"Timmy Pandolfi",
        "winner_score":94
    },

    "Hannah Wright (S5 Winner)": {
        "scores": [8.8,7.8,6.8,8.9,8.0,7.4,9.1,8.3],
        "quote": "Marco and I — that's why I'm here.",
        "archetype": "The Anchor",
        "summary": """
Strong validation language,
stable relationship arc,
audience-friendly emotional warmth,
minimal unnecessary conflict.
""",
        "partner":"Marco Donatelli",
        "winner_score":92
    },

    "Serena Page (S6 Winner)": {
        "scores": [7.9,8.6,6.5,8.2,8.8,8.1,8.4,6.7],
        "quote": "I just want something genuine.",
        "archetype": "The Slow Burn",
        "summary": """
Started slower socially but gained audience support
through emotional transparency and post-Casa resilience.
""",
        "partner":"Kordell Beckham",
        "winner_score":89
    },

    "Leah Kateb (S6 Finalist)": {
        "scores": [6.9,9.0,7.3,7.4,9.2,8.8,6.8,4.7],
        "quote": "I'm emotional, but I'm real.",
        "archetype": "The Social Butterfly",
        "summary": """
Extremely high relatability and disclosure.
Strong audience engagement but more volatile
romantic positioning.
""",
        "partner":"Miguel Harichi",
        "winner_score":81
    },

    "Justine Ndiba (S2 Winner)": {
        "scores": [8.7,7.2,6.0,8.8,7.6,7.0,9.0,8.5],
        "quote": "I wanted something real from the beginning.",
        "archetype": "The Anchor",
        "summary": """
One of the strongest stability profiles in franchise history.
Low drama, high emotional consistency.
""",
        "partner":"Caleb Corprew",
        "winner_score":91
    },

    "Cashay Proudfoot (S3 Fan Favorite)": {
        "scores": [6.0,8.7,8.2,8.0,9.0,9.1,5.8,4.3],
        "quote": "I wear my heart on my sleeve.",
        "archetype": "The Social Butterfly",
        "summary": """
Elite social centrality and audience relatability.
More unstable romantic trajectory reduced winner probability.
""",
        "partner":"Cinco Holland",
        "winner_score":76
    },

    "Kassy Castillo (S5 Finalist)": {
        "scores": [5.8,8.9,7.5,6.6,8.7,8.4,4.9,3.2],
        "quote": "I'm trying to follow my heart.",
        "archetype": "The Chaos Romantic",
        "summary": """
High emotional expressiveness and audience entertainment value
but major volatility during Casa Amor.
""",
        "partner":"Leo Dionicio",
        "winner_score":67
    },

    "Destiny Davis (S5)": {
        "scores": [5.2,5.6,5.4,5.0,5.8,7.3,4.6,3.1],
        "quote": "I'm not going to chase anyone.",
        "archetype": "The Independent",
        "summary": """
Strong confidence and boundaries but struggled
to form stable long-term romantic attachment.
""",
        "partner":"Multiple",
        "winner_score":58
    }
}

# =================================================
# REAL COUPLE COMPATIBILITY DATA
# =================================================

couples = {

    "Zeta Morrison ❤️ Timmy Pandolfi": {

        "female":[9.2,7.4,6.3,9.0,8.4,7.2,9.4,8.6],

        "male":[8.4,6.9,6.5,8.1,7.7,7.4,8.8,7.9],

        "status":"Season 4 Winners",

        "compatibility":94,

        "archetype":"Secure Power Couple",

        "summary":"""
One of the strongest emotional regulation pairings
in Love Island USA history.

Both contestants demonstrated:
- high emotional consistency
- low conflict escalation
- strong reassurance behaviors
- secure attachment patterns
""",

        "strengths":[
            "High emotional regulation",
            "Stable romantic positioning",
            "Strong reassurance language",
            "Balanced communication"
        ],

        "risks":[
            "Occasional emotional withdrawal"
        ]
    },

    "Hannah Wright ❤️ Marco Donatelli": {

        "female":[8.8,7.8,6.8,8.9,8.0,7.4,9.1,8.3],

        "male":[8.2,6.5,6.6,8.0,7.8,7.0,8.7,7.6],

        "status":"Season 5 Winners",

        "compatibility":92,

        "archetype":"Audience Favorite Couple",

        "summary":"""
Extremely high audience trust and stable
relationship reinforcement throughout the season.
""",

        "strengths":[
            "High validation language",
            "Stable public perception",
            "Low volatility"
        ],

        "risks":[
            "Lower entertainment unpredictability"
        ]
    },

    "Serena Page ❤️ Kordell Beckham": {

        "female":[7.9,8.6,6.5,8.2,8.8,8.1,8.4,6.7],

        "male":[8.0,7.2,7.0,8.5,8.4,7.8,8.9,7.0],

        "status":"Season 6 Winners",

        "compatibility":90,

        "archetype":"Slow Burn Pairing",

        "summary":"""
Gradual emotional trust development
with strong post-Casa recovery.
""",

        "strengths":[
            "Post-conflict resilience",
            "Strong emotional pacing",
            "High vulnerability growth"
        ],

        "risks":[
            "Slower early attachment"
        ]
    },

    "Leah Kateb ❤️ Miguel Harichi": {

        "female":[6.9,9.0,7.3,7.4,9.2,8.8,6.8,4.7],

        "male":[7.1,6.9,7.8,6.8,7.2,8.1,6.7,5.2],

        "status":"Season 6 Finalists",

        "compatibility":82,

        "archetype":"Charisma Couple",

        "summary":"""
Extremely high relatability and entertainment value.
""",

        "strengths":[
            "High chemistry",
            "Strong audience engagement",
            "Emotional transparency"
        ],

        "risks":[
            "Higher emotional volatility"
        ]
    },

    "Cashay Proudfoot ❤️ Cinco Holland": {

        "female":[6.0,8.7,8.2,8.0,9.0,9.1,5.8,4.3],

        "male":[5.9,6.2,6.8,5.7,6.5,7.2,4.8,5.0],

        "status":"Season 3 Fan Favorite",

        "compatibility":71,

        "archetype":"Emotional Rollercoaster",

        "summary":"""
Elite audience engagement but unstable
romantic trajectory.
""",

        "strengths":[
            "Massive audience relatability",
            "High chemistry"
        ],

        "risks":[
            "Commitment instability",
            "Emotional inconsistency"
        ]
    },

    "Kassy Castillo ❤️ Leo Dionicio": {

        "female":[5.8,8.9,7.5,6.6,8.7,8.4,4.9,3.2],

        "male":[4.8,6.5,7.0,5.1,6.2,8.0,3.0,2.8],

        "status":"Season 5 Finalists",

        "compatibility":63,

        "archetype":"Chaos Couple",

        "summary":"""
High entertainment and emotional intensity
but major instability after Casa Amor.
""",

        "strengths":[
            "High emotional engagement",
            "Strong chemistry"
        ],

        "risks":[
            "Trust instability",
            "Casa Amor volatility"
        ]
    }
}

# =================================================
# WINNER ZONE SHADOW
# =================================================

winner_min = [6.8,6.7,5.8,7.0,6.5,6.2,7.4,5.8]
winner_max = [9.0,8.6,7.5,9.1,8.5,8.2,9.2,8.4]

winner_mean = [7.8,7.4,6.8,7.9,7.1,7.2,8.1,6.9]

# =================================================
# TABS
# =================================================

tab1, tab2, tab3, tab4 = st.tabs([
    "💘 Contestant Radar",
    "🏝️ Casa Amor Delta",
    "💞 Couple Compatibility",
    "🔥 Season Comparison"
])

# =================================================
# TAB 1 — CONTESTANT RADAR
# =================================================

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

    fig.add_trace(go.Scatterpolar(
        r=winner_max,
        theta=traits,
        fill='toself',
        opacity=.15,
        line=dict(color=COLORS["gold"]),
        name="Winner Zone Max"
    ))

    fig.add_trace(go.Scatterpolar(
        r=winner_min,
        theta=traits,
        fill='toself',
        opacity=.08,
        line=dict(color=COLORS["baby_pink"]),
        name="Winner Zone Min"
    ))

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

    selected_data = contestants[selected]

    st.markdown(f"""
    <div class='card'>

    <h2>💖 Contestant Intelligence Profile</h2>

    <h3>👑 {selected}</h3>

    <p><strong>Primary Archetype:</strong>
    {selected_data['archetype']}</p>

    <p><strong>Partner Association:</strong>
    {selected_data['partner']}</p>

    <p><strong>Representative Quote:</strong></p>

    <p><em>"{selected_data['quote']}"</em></p>

    <p><strong>Behavioral Summary:</strong></p>

    <p>{selected_data['summary']}</p>

    </div>
    """, unsafe_allow_html=True)

# =================================================
# TAB 2 — CASA AMOR DELTA
# =================================================

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

# =================================================
# TAB 3 — COUPLE COMPATIBILITY
# =================================================

with tab3:

    st.markdown("""
    ## 💞 Couple Compatibility Intelligence

    Compare real Love Island couples using:
    - emotional regulation
    - loyalty
    - communication compatibility
    - audience chemistry
    - long-term stability indicators
    """)

    selected_couple = st.selectbox(
        "Choose Couple",
        list(couples.keys())
    )

    data = couples[selected_couple]

    fig3 = go.Figure()

    fig3.add_trace(go.Scatterpolar(
        r=data["female"],
        theta=traits,
        fill='toself',
        opacity=.35,

        name="Partner A",

        line=dict(
            color=COLORS["hot_pink"],
            width=4
        ),

        fillcolor="rgba(255,79,152,.25)"
    ))

    fig3.add_trace(go.Scatterpolar(
        r=data["male"],
        theta=traits,
        fill='toself',
        opacity=.30,

        name="Partner B",

        line=dict(
            color=COLORS["ocean"],
            width=4
        ),

        fillcolor="rgba(77,168,255,.20)"
    ))

    fig3.update_layout(

        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0,10]
            )
        ),

        height=780,

        paper_bgcolor="rgba(0,0,0,0)",

        title=f"💞 {selected_couple} Compatibility Radar",

        font=dict(
            family="Poppins",
            size=14,
            color=COLORS["dark"]
        )
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "💖 Compatibility Score",
            f"{data['compatibility']}%"
        )

    with col2:

        st.metric(
            "🏝️ Couple Archetype",
            data["archetype"]
        )

    with col3:

        st.metric(
            "📺 Villa Outcome",
            data["status"]
        )

    st.markdown(f"""
    <div class='card'>

    <h2>🌴 Couple Intelligence Summary</h2>

    <p>
    {data['summary']}
    </p>

    </div>
    """, unsafe_allow_html=True)

    colA, colB = st.columns(2)

    with colA:

        st.markdown("""
        <div class='card'>
        <h2>💖 Relationship Strengths</h2>
        </div>
        """, unsafe_allow_html=True)

        for s in data["strengths"]:
            st.markdown(f"- {s}")

    with colB:

        st.markdown("""
        <div class='card'>
        <h2>🔥 Relationship Risks</h2>
        </div>
        """, unsafe_allow_html=True)

        for r in data["risks"]:
            st.markdown(f"- {r}")

    female_scores = np.array(data["female"])
    male_scores = np.array(data["male"])

    diff = np.abs(female_scores - male_scores)

    breakdown_df = pd.DataFrame({

        "Trait": traits,
        "Difference": diff
    })

    fig_breakdown = go.Figure()

    fig_breakdown.add_trace(go.Bar(
        x=breakdown_df["Trait"],
        y=breakdown_df["Difference"],

        marker=dict(
            color=breakdown_df["Difference"],
            colorscale=[
                [0, COLORS["mint"]],
                [.5, COLORS["gold"]],
                [1, COLORS["drama"]]
            ]
        )
    ))

    fig_breakdown.update_layout(
        title="💘 Trait Difference Breakdown",
        height=500,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )

    st.plotly_chart(
        fig_breakdown,
        use_container_width=True
    )

# =================================================
# TAB 4 — SEASON COMPARISON
# =================================================

with tab4:

    season_data = {

        "Season 2 Winner":[8.7,7.2,6.0,8.8,7.6,7.0,9.0,8.5],

        "Season 4 Winner":[9.2,7.4,6.3,9.0,8.4,7.2,9.4,8.6],

        "Season 5 Winner":[8.8,7.8,6.8,8.9,8.0,7.4,9.1,8.3],

        "Season 6 Winner":[7.9,8.6,6.5,8.2,8.8,8.1,8.4,6.7]
    }

    fig4 = go.Figure()

    season_colors = [
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
            line_color=season_colors[i]
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
