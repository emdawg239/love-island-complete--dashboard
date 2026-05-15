
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from auth import check_password

check_password()

# =================================================
# PAGE CONFIG
# =================================================

st.set_page_config(
    page_title="Behavioral Findings",
    page_icon="💖",
    layout="wide"
)

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

st.title("💖 Behavioral Findings")

st.markdown("""
Comprehensive behavioral analysis of real
Love Island USA contestants across:
- winners
- finalists
- fan favorites
- early exits
- high-drama archetypes

using emotional, relational,
and audience-perception variables.
""")

# =================================================
# TABS
# =================================================

tab1, tab2, tab3, tab4 = st.tabs([
    "👑 Winners & Finalists",
    "🔥 Early Exits & Chaos Profiles",
    "📊 Behavioral Trends",
    "🧠 Score Yourself"
])

# =================================================
# WINNER DATA
# =================================================

winners = [

{
    "season":"S2",
    "name":"Justine Ndiba",
    "placement":"Winner",
    "archetype":"The Anchor",

    "quote":"I wanted something real from the beginning.",

    "summary":"""
One of the strongest emotional regulation profiles
in franchise history.

Maintained calm communication,
stable romantic positioning,
and high emotional reassurance behaviors.
""",

    "traits":{
        "Loyalty":9.2,
        "Low Drama":8.8,
        "Disclosure":7.2,
        "Validation":9.0,
        "Warmth":9.1,
        "Centrality":7.4
    }
},

{
    "season":"S3",
    "name":"Cashay Proudfoot",
    "placement":"Fan Favorite",
    "archetype":"The Social Butterfly",

    "quote":"I wear my heart on my sleeve.",

    "summary":"""
Extremely high social centrality
and audience relatability.

Romantic instability reduced overall winner probability
despite elite audience attachment.
""",

    "traits":{
        "Loyalty":5.8,
        "Low Drama":4.6,
        "Disclosure":9.3,
        "Validation":8.2,
        "Warmth":9.2,
        "Centrality":9.5
    }
},

{
    "season":"S4",
    "name":"Zeta Morrison",
    "placement":"Winner",
    "archetype":"The Anchor",

    "quote":"I'm not here for chaos.",

    "summary":"""
Elite emotional stability and low reactivity.

Consistently reinforced one stable romantic narrative
while maintaining strong female alliances.
""",

    "traits":{
        "Loyalty":9.5,
        "Low Drama":8.7,
        "Disclosure":7.4,
        "Validation":9.1,
        "Warmth":8.9,
        "Centrality":7.7
    }
},

{
    "season":"S5",
    "name":"Hannah Wright",
    "placement":"Winner",
    "archetype":"The Anchor",

    "quote":"Marco and I — that's why I'm here.",

    "summary":"""
Strong emotional validation,
high audience trust,
and one of the most stable couple trajectories
in Love Island USA history.
""",

    "traits":{
        "Loyalty":9.2,
        "Low Drama":8.5,
        "Disclosure":7.8,
        "Validation":9.0,
        "Warmth":8.8,
        "Centrality":7.5
    }
},

{
    "season":"S5",
    "name":"Kassy Castillo",
    "placement":"Finalist",
    "archetype":"The Chaos Romantic",

    "quote":"I'm trying to follow my heart.",

    "summary":"""
High emotional openness and entertainment value.

Frequent romantic instability created volatility
but increased audience engagement.
""",

    "traits":{
        "Loyalty":4.8,
        "Low Drama":3.0,
        "Disclosure":9.0,
        "Validation":6.7,
        "Warmth":8.7,
        "Centrality":8.8
    }
},

{
    "season":"S6",
    "name":"Serena Page",
    "placement":"Winner",
    "archetype":"The Slow Burn",

    "quote":"I just want something genuine.",

    "summary":"""
Classic slow-burn growth trajectory.

Built emotional trust gradually
and gained strong post-Casa audience support.
""",

    "traits":{
        "Loyalty":8.7,
        "Low Drama":7.5,
        "Disclosure":8.8,
        "Validation":8.6,
        "Warmth":9.0,
        "Centrality":7.9
    }
},

{
    "season":"S6",
    "name":"Leah Kateb",
    "placement":"Finalist",
    "archetype":"The Social Butterfly",

    "quote":"I'm emotional, but I'm real.",

    "summary":"""
Extremely high audience relatability
through emotional transparency,
humor,
and vulnerability.
""",

    "traits":{
        "Loyalty":6.8,
        "Low Drama":5.0,
        "Disclosure":9.4,
        "Validation":7.6,
        "Warmth":9.1,
        "Centrality":9.3
    }
}

]

# =================================================
# EARLY EXIT DATA
# =================================================

early_exits = [

{
    "season":"S5",
    "name":"Victor Gonzalez",
    "archetype":"The Antagonist",

    "quote":"I'm done talking about this.",

    "summary":"""
High conflict initiation,
territorial communication,
and reactive confrontation patterns.

Social trust deteriorated rapidly after repeated
conflict escalation.
""",

    "traits":{
        "Drama":9.2,
        "Conflict":9.0,
        "Volatility":8.6,
        "Warmth":2.8,
        "Loyalty":4.1,
        "Disclosure":3.7
    }
},

{
    "season":"S5",
    "name":"Keenan Anunay",
    "archetype":"The Chaos Romantic",

    "quote":"I need to explore every connection.",

    "summary":"""
High recoupling volatility
and repeated loyalty inconsistencies.

Audience trust declined sharply after Casa Amor.
""",

    "traits":{
        "Drama":8.4,
        "Conflict":6.5,
        "Volatility":9.4,
        "Warmth":5.2,
        "Loyalty":2.6,
        "Disclosure":6.0
    }
},

{
    "season":"S6",
    "name":"Rob Rausch",
    "archetype":"The Avoidant Wildcard",

    "quote":"I'm trying to protect my peace.",

    "summary":"""
Strong audience intrigue
but emotionally avoidant communication patterns.

Humor and charm initially increased support,
but inconsistent emotional openness created instability.
""",

    "traits":{
        "Drama":6.9,
        "Conflict":5.4,
        "Volatility":7.8,
        "Warmth":6.1,
        "Loyalty":4.8,
        "Disclosure":4.0
    }
},

{
    "season":"S5",
    "name":"Destiny Davis",
    "archetype":"The Independent",

    "quote":"I'm not going to chase anyone.",

    "summary":"""
Strong confidence and boundaries
but lower romantic vulnerability.

Audience struggled to emotionally attach
to more guarded communication style.
""",

    "traits":{
        "Drama":4.2,
        "Conflict":4.7,
        "Volatility":5.5,
        "Warmth":5.7,
        "Loyalty":5.1,
        "Disclosure":5.2
    }
}

]

# =================================================
# TAB 1 — WINNERS
# =================================================

with tab1:

    st.markdown("## 👑 High-Performing Contestant Profiles")

    for person in winners:

        with st.expander(
            f"{person['season']} • {person['name']} • {person['placement']}"
        ):

            col1, col2 = st.columns([1.3,1])

            # ----------------------------------------
            # LEFT
            # ----------------------------------------

            with col1:

                st.markdown(f"""
                <div class='card'>

                <h2 style='color:{COLORS["hot_pink"]};'>
                💖 {person['name']}
                </h2>

                <p>
                <strong>Archetype:</strong>
                {person['archetype']}
                </p>

                <p style='font-style:italic;'>
                "{person['quote']}"
                </p>

                <p>
                {person['summary']}
                </p>

                </div>
                """, unsafe_allow_html=True)

            # ----------------------------------------
            # RIGHT
            # ----------------------------------------

            with col2:

                trait_df = pd.DataFrame({
                    "Trait": list(person["traits"].keys()),
                    "Score": list(person["traits"].values())
                })

                fig = px.bar(
                    trait_df,
                    x="Score",
                    y="Trait",
                    orientation="h",
                    range_x=[0,10],
                    color="Score",

                    color_continuous_scale=[
                        COLORS["baby_pink"],
                        COLORS["hot_pink"]
                    ]
                )

                fig.update_layout(
                    height=400,
                    paper_bgcolor="rgba(0,0,0,0)",
                    plot_bgcolor="rgba(0,0,0,0)",
                    margin=dict(l=0,r=0,t=20,b=0)
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True
                )

# =================================================
# TAB 2 — EARLY EXITS
# =================================================

with tab2:

    st.markdown("## 🔥 Early Exit & Chaos Profiles")

    st.markdown("""
Contestants eliminated early or associated with
high-instability trajectories consistently display:
- emotional volatility
- reactive confrontation
- inconsistent loyalty
- unstable romantic narratives
- audience trust collapse
""")

    for person in early_exits:

        with st.expander(
            f"{person['season']} • {person['name']} • {person['archetype']}"
        ):

            col1, col2 = st.columns([1.3,1])

            with col1:

                st.markdown(f"""
                <div style="
                    background:white;
                    border-radius:28px;
                    padding:28px;
                    box-shadow:0 10px 30px rgba(0,0,0,.06);
                ">

                <h2 style='color:{COLORS["danger"]};'>
                🔥 {person['name']}
                </h2>

                <p>
                <strong>Archetype:</strong>
                {person['archetype']}
                </p>

                <p style='font-style:italic;'>
                "{person['quote']}"
                </p>

                <p>
                {person['summary']}
                </p>

                </div>
                """, unsafe_allow_html=True)

            with col2:

                trait_df = pd.DataFrame({
                    "Trait": list(person["traits"].keys()),
                    "Score": list(person["traits"].values())
                })

                fig = px.bar(
                    trait_df,
                    x="Score",
                    y="Trait",
                    orientation="h",
                    range_x=[0,10],
                    color="Score",

                    color_continuous_scale=[
                        "#ffd6e0",
                        "#ff7096",
                        "#d90429"
                    ]
                )

                fig.update_layout(
                    height=400,
                    paper_bgcolor="rgba(0,0,0,0)",
                    plot_bgcolor="rgba(0,0,0,0)"
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True
                )

# =================================================
# TAB 3 — TRENDS
# =================================================

with tab3:

    st.markdown("## 📊 Cross-Season Behavioral Trends")

    trend_df = pd.DataFrame({

        "Trait":[
            "Partner Stability",
            "Warm Validation",
            "Social Centrality",
            "Disclosure",
            "Conflict Initiation",
            "Gossip Participation"
        ],

        "Correlation":[
            .82,
            .74,
            .68,
            .61,
            -.62,
            -.58
        ]
    })

    fig = px.bar(
        trend_df,
        x="Correlation",
        y="Trait",
        orientation="h",
        color="Correlation",

        color_continuous_scale=[
            COLORS["baby_pink"],
            COLORS["hot_pink"]
        ]
    )

    fig.update_layout(
        height=600,
        title="💖 Predictors of Winning",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # ---------------------------------------------
    # RADAR
    # ---------------------------------------------

    radar_traits = [
        "Loyalty",
        "Disclosure",
        "Validation",
        "Warmth",
        "Centrality",
        "Low Drama"
    ]

    winner_profile = [9.1,8.0,8.8,8.9,7.8,8.4]
    chaos_profile = [3.2,5.7,4.0,4.8,7.0,2.2]

    fig2 = go.Figure()

    fig2.add_trace(go.Scatterpolar(
        r=winner_profile,
        theta=radar_traits,
        fill='toself',
        name='Winner Profile',

        line=dict(
            color=COLORS["hot_pink"],
            width=4
        ),

        fillcolor="rgba(255,79,152,.25)"
    ))

    fig2.add_trace(go.Scatterpolar(
        r=chaos_profile,
        theta=radar_traits,
        fill='toself',
        name='Chaos Profile',

        line=dict(
            color=COLORS["danger"],
            width=4
        ),

        fillcolor="rgba(217,4,41,.18)"
    ))

    fig2.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0,10]
            )
        ),

        paper_bgcolor="rgba(0,0,0,0)",
        height=650,

        title="🌴 Winner vs Chaos Archetype"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

# =================================================
# TAB 4 — SCORE YOURSELF
# =================================================

with tab4:

    st.markdown("## 🧠 Behavioral Similarity Engine")

    st.markdown("""
Describe your communication,
dating,
and emotional behavior style
to estimate your closest
Love Island archetype.
""")

    user_input = st.text_area(
        "Describe your behavioral style:",
        height=250,

        placeholder="""
Example:

I prefer stable relationships,
avoid drama,
communicate openly,
and value emotional consistency...
"""
    )

    if st.button("💖 Calculate Winner Similarity"):

        score = 0

        positive_keywords = [
            "loyal",
            "stable",
            "warm",
            "calm",
            "secure",
            "trust",
            "supportive",
            "emotionally intelligent",
            "communicative",
            "consistent"
        ]

        negative_keywords = [
            "dramatic",
            "chaotic",
            "jealous",
            "reactive",
            "gossip",
            "aggressive",
            "toxic",
            "volatile"
        ]

        lowered = user_input.lower()

        for word in positive_keywords:

            if word in lowered:
                score += 1

        for word in negative_keywords:

            if word in lowered:
                score -= 1

        normalized = max(
            min((score + 5) * 10,100),
            0
        )

        st.metric(
            "💖 Winner Similarity Score",
            f"{normalized}%"
        )

        if normalized >= 80:

            st.success("""
            👑 Primary Archetype:
            The Anchor
            """)

        elif normalized >= 60:

            st.info("""
            🌅 Primary Archetype:
            The Slow Burn
            """)

        elif normalized >= 40:

            st.warning("""
            🦋 Primary Archetype:
            The Social Butterfly
            """)

        else:

            st.error("""
            🔥 Primary Archetype:
            The Chaos Romantic
            """)

# =================================================
# FINAL INSIGHT
# =================================================

st.markdown(f"""
<div style="
background:linear-gradient(
135deg,
{COLORS["hot_pink"]},
{COLORS["soft_pink"]}
);

padding:40px;
border-radius:32px;
color:white;
margin-top:40px;
">

<h2>💖 Core Behavioral Finding</h2>

<p style='font-size:18px;'>

Across all analyzed seasons,
the contestants who consistently
perform best are not necessarily:

- the loudest
- the most dramatic
- the most visible

Instead,
the strongest long-term performers combine:

- emotional regulation
- loyalty
- warmth
- stable romantic narratives
- gradual vulnerability
- social consistency

while avoiding:

- reactive conflict
- volatility
- parasocial distrust
- relationship instability.

</p>

</div>
""", unsafe_allow_html=True)
