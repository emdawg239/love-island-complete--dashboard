
import streamlit as st
import pandas as pd
import plotly.express as px

# ---------- PAGE CONFIG ----------

st.set_page_config(layout="wide")

with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("Female Winner Behavioral Profiles")

# ---------- TABS ----------

tab1, tab2, tab3 = st.tabs([
    "Winners",
    "Early Exits",
    "Score Yourself"
])

# ---------- DATA ----------

winners = [
    {
        "season": "S4",
        "name": "Zeta Morrison",
        "quote": "I want something real. I'm not here for chaos.",
        "summary": """
        Consistently emotionally regulated.
        Avoided escalating conflict.
        Strong female alliance positioning.
        High partner loyalty.
        """,
        "traits": {
            "Loyalty": 8.7,
            "Low drama": 8.1,
            "Disclosure": 7.6,
            "Humor": 6.4,
            "Validation": 8.3
        }
    },

    {
        "season": "S5",
        "name": "Hannah Wright",
        "quote": "Marco and I — that's why I'm here.",
        "summary": """
        Strong emotional validation.
        Stable romantic arc.
        High audience relatability.
        Maintained alliances without conflict.
        """,
        "traits": {
            "Loyalty": 8.9,
            "Low drama": 8.3,
            "Disclosure": 7.7,
            "Humor": 6.6,
            "Validation": 8.6
        }
    }
]

# ---------- WINNERS TAB ----------

with tab1:

    st.markdown("""
    Research findings across all female winners.
    Click each contestant to expand.
    """)

    for person in winners:

        with st.expander(
            f"{person['season']} • {person['name']}",
            expanded=False
        ):

            col1, col2 = st.columns([1.4, 1])

            with col1:

                st.markdown(f"""
                ### Quote

                *"{person['quote']}"*

                ### Documented Behaviors

                {person['summary']}
                """)

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
                        "#ffb6d9",
                        "#ff4f98"
                    ]
                )

                fig.update_layout(
                    height=300,
                    margin=dict(l=0,r=0,t=0,b=0)
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True
                )

# ---------- EARLY EXITS ----------

with tab2:

    st.markdown("""
    Contestants eliminated early consistently display:
    """)

    st.markdown("""
    - emotional volatility
    - reactive communication
    - unstable partner dynamics
    - social isolation
    - high gossip participation
    - conflict escalation
    """)

# ---------- SELF SCORE ----------

with tab3:

    st.subheader("Behavioral Similarity Scoring")

    user_input = st.text_area(
        "Describe your dating/show behavior style:",
        height=250,
        placeholder="""
Example:
I am emotionally loyal, avoid drama,
value strong communication,
and prefer one stable relationship...
"""
    )

    if st.button("Calculate Winner Similarity"):

        score = 0

        positive_keywords = [
            "loyal",
            "stable",
            "honest",
            "warm",
            "calm",
            "emotionally intelligent",
            "communicative",
            "trust",
            "supportive"
        ]

        negative_keywords = [
            "dramatic",
            "jealous",
            "chaotic",
            "reactive",
            "toxic",
            "gossip",
            "aggressive"
        ]

        lowered = user_input.lower()

        for word in positive_keywords:
            if word in lowered:
                score += 1

        for word in negative_keywords:
            if word in lowered:
                score -= 1

        normalized = max(min((score + 5) * 10, 100), 0)

        st.metric(
            "Winner Similarity Score",
            f"{normalized}%"
        )

        # Archetype Logic

        if normalized >= 75:
            st.success("Primary Archetype: The Anchor")

        elif normalized >= 55:
            st.info("Primary Archetype: The Slow Burn")

        elif normalized >= 35:
            st.warning("Primary Archetype: The Social Butterfly")

        else:
            st.error("Primary Archetype: The Antagonist")
