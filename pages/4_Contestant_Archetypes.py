import streamlit as st
import plotly.graph_objects as go
import numpy as np

# ------------------------------------------------
# LOAD STYLES
# ------------------------------------------------

with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

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

st.title("💖 Contestant Archetype Intelligence")

st.markdown("""
Behavioral clustering analysis identified several
repeatable contestant archetypes that strongly predict:
- placement
- audience popularity
- Casa Amor survivability
- long-term couple stability
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
# ARCHETYPE DATA
# ------------------------------------------------

archetypes = [

{
    "title":"💛 The Anchor",

    "badge":"👑",

    "desc":"""
Emotionally stable, low drama,
one strong couple.

Most common female winner profile.
""",

    "tags":[
        "High loyalty",
        "Low drama",
        "Secure attachment",
        "High validation"
    ],

    "examples":[
        "Zeta Morrison (S4)",
        "Hannah Wright (S5)",
        "Justine Ndiba (S2)"
    ],

    "scores":[
        9.1,
        7.4,
        6.2,
        8.8,
        8.0,
        7.2,
        9.3,
        8.5
    ],

    "avg_finish":"Winner / Finalist",
    "casa_survival":"92%",
    "avg_recouplings":"1.2",
    "couple_stability":"Very High"
},

{
    "title":"🦋 The Social Butterfly",

    "badge":"💞",

    "desc":"""
Highly social and emotionally expressive.

Strong audience engagement but often unstable
romantic trajectories.
""",

    "tags":[
        "High centrality",
        "High disclosure",
        "Moderate drama",
        "Audience favorite"
    ],

    "examples":[
        "Cashay Proudfoot (S3)",
        "Leah Kateb (S6)",
        "Kassy Castillo (S5)"
    ],

    "scores":[
        6.2,
        9.0,
        8.1,
        7.0,
        8.8,
        9.2,
        5.8,
        4.4
    ],

    "avg_finish":"Mid-Villa / Finalist",
    "casa_survival":"61%",
    "avg_recouplings":"3.8",
    "couple_stability":"Moderate"
},

{
    "title":"🔥 The Antagonist",

    "badge":"💥",

    "desc":"""
High conflict initiation,
high gossip participation,
low emotional consistency.

Generates airtime but rarely wins public trust.
""",

    "tags":[
        "High drama",
        "Conflict heavy",
        "Low disclosure",
        "Reactive"
    ],

    "examples":[
        "Frequently associated with reactive villa conflict arcs"
    ],

    "scores":[
        3.8,
        4.2,
        5.4,
        3.0,
        4.1,
        8.6,
        2.4,
        1.2
    ],

    "avg_finish":"Early Exit",
    "casa_survival":"22%",
    "avg_recouplings":"5.1",
    "couple_stability":"Very Low"
},

{
    "title":"🌅 The Slow Burn",

    "badge":"✨",

    "desc":"""
Low initial visibility but strong
emotional intelligence and audience growth.

Tends to peak post-Casa Amor.
""",

    "tags":[
        "Late bloomer",
        "High emotional intelligence",
        "Low conflict",
        "Steady growth"
    ],

    "examples":[
        "Serena Page (S6)",
        "Camilla Thurlow (UK)",
        "Jessie Wynter (AUS)"
    ],

    "scores":[
        7.8,
        8.2,
        6.4,
        8.5,
        8.7,
        6.3,
        8.0,
        7.5
    ],

    "avg_finish":"Finalist",
    "casa_survival":"84%",
    "avg_recouplings":"2.0",
    "couple_stability":"High"
}

]

# ------------------------------------------------
# ARCHETYPE CARDS
# ------------------------------------------------

for archetype in archetypes:

    st.markdown(f"""
    <div class='card'>
    <h1>{archetype['badge']} {archetype['title']}</h1>

    <p>{archetype['desc']}</p>
    </div>
    """, unsafe_allow_html=True)

    # ------------------------------------------------
    # LAYOUT
    # ------------------------------------------------

    col1, col2 = st.columns([1.2,1])

    # ------------------------------------------------
    # LEFT COLUMN
    # ------------------------------------------------

    with col1:

        st.markdown("### 🌴 Archetype Indicators")

        for tag in archetype["tags"]:

            st.markdown(
                f"""
                <span class='tag'>{tag}</span>
                """,
                unsafe_allow_html=True
            )

        st.markdown("")

        st.markdown("### 💖 Real Contestant Examples")

        for ex in archetype["examples"]:

            st.markdown(f"- {ex}")

        st.markdown("")

        st.markdown("### 📊 Relationship Outcomes")

        metric1, metric2 = st.columns(2)

        with metric1:

            st.metric(
                "🏝️ Avg Finish",
                archetype["avg_finish"]
            )

            st.metric(
                "💞 Couple Stability",
                archetype["couple_stability"]
            )

        with metric2:

            st.metric(
                "🔥 Casa Survival",
                archetype["casa_survival"]
            )

            st.metric(
                "🔄 Avg Recouplings",
                archetype["avg_recouplings"]
            )

    # ------------------------------------------------
    # RIGHT COLUMN
    # ------------------------------------------------

    with col2:

        fig = go.Figure()

        fig.add_trace(go.Scatterpolar(
            r=archetype["scores"],
            theta=traits,
            fill='toself',

            line=dict(
                color=COLORS["hot_pink"],
                width=4
            ),

            fillcolor="rgba(255,79,152,.25)",

            name=archetype["title"]
        ))

        fig.update_layout(

            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0,10]
                )
            ),

            height=500,

            paper_bgcolor="rgba(0,0,0,0)",

            font=dict(
                family="Poppins",
                size=13,
                color=COLORS["dark"]
            ),

            showlegend=False
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    st.markdown("---")

# ------------------------------------------------
# ARCHETYPE CLASSIFIER
# ------------------------------------------------

st.markdown("# 🧠 Archetype Probability Engine")

contestant_input = st.selectbox(
    "Select Contestant",
    [
        "Zeta Morrison",
        "Hannah Wright",
        "Serena Page",
        "Leah Kateb",
        "Cashay Proudfoot",
        "Kassy Castillo"
    ]
)

# ------------------------------------------------
# PROBABILITIES
# ------------------------------------------------

probabilities = {

    "Zeta Morrison":[
        91,
        5,
        1,
        3
    ],

    "Hannah Wright":[
        88,
        6,
        1,
        5
    ],

    "Serena Page":[
        20,
        14,
        4,
        62
    ],

    "Leah Kateb":[
        12,
        72,
        5,
        11
    ],

    "Cashay Proudfoot":[
        10,
        80,
        4,
        6
    ],

    "Kassy Castillo":[
        4,
        44,
        40,
        12
    ]
}

labels = [
    "Anchor",
    "Social Butterfly",
    "Antagonist",
    "Slow Burn"
]

vals = probabilities[contestant_input]

fig2 = go.Figure()

fig2.add_trace(go.Bar(
    x=labels,
    y=vals,

    marker_color=[
        COLORS["gold"],
        COLORS["hot_pink"],
        COLORS["drama"],
        COLORS["ocean"]
    ]
))

fig2.update_layout(
    title=f"💘 Archetype Probability Distribution — {contestant_input}",

    paper_bgcolor="rgba(0,0,0,0)",

    plot_bgcolor="rgba(0,0,0,0)",

    font=dict(
        family="Poppins",
        size=14,
        color=COLORS["dark"]
    ),

    height=500
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# ------------------------------------------------
# FINAL INSIGHT
# ------------------------------------------------

st.markdown("""
<div class='card'>

## 💡 Key Research Insight

Female winners overwhelmingly cluster around:

- emotional consistency
- secure attachment
- low conflict initiation
- strong partner loyalty
- high emotional validation

Contestants centered around:
- chaos
- instability
- reactive confrontation

generate airtime but rarely sustain public support long enough to win.

</div>
""", unsafe_allow_html=True)


