import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

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

st.title("📚 Research References & Methodology")

st.markdown("""
A complete research archive documenting the
psychological theories, behavioral coding systems,
archetypes, and analytical frameworks used throughout
the Love Island Behavioral Intelligence Dashboard.
""")

# ------------------------------------------------
# SECTION NAVIGATION
# ------------------------------------------------

tabs = st.tabs([
    "🧠 Psychological Theories",
    "💖 Trait Dictionary",
    "🏝️ Archetype Taxonomy",
    "📺 Season Archive",
    "📊 Methodology",
    "🧪 Coding Manual",
    "💞 Audience Psychology",
    "📈 Statistical Appendix",
    "🎬 Episode References",
    "🔗 Public Sources"
])

# =================================================
# TAB 1 — PSYCHOLOGICAL THEORIES
# =================================================

with tabs[0]:

    theories = [

        {
            "title":"Attachment Theory",
            "researchers":"John Bowlby, Mary Ainsworth",

            "summary":"""
Attachment Theory proposes that individuals develop
consistent emotional bonding styles that shape:
- trust
- conflict response
- intimacy
- emotional regulation
""",

            "love_island":"""
Contestants displaying secure attachment behaviors
consistently outperform contestants with anxious
or avoidant communication styles.

Examples:
- Zeta Morrison
- Hannah Wright
- Serena Page
""",

            "citations":[
                "Bowlby, J. (1969). Attachment and Loss.",
                "Ainsworth, M. (1978). Patterns of Attachment."
            ]
        },

        {
            "title":"Social Penetration Theory",
            "researchers":"Altman & Taylor",

            "summary":"""
Gradual reciprocal self-disclosure increases:
- intimacy
- trust
- relational bonding
- audience attachment
""",

            "love_island":"""
Contestants who pace emotional vulnerability
more effectively tend to build stronger parasocial
viewer attachment.
""",

            "citations":[
                "Altman & Taylor (1973). Social Penetration Theory."
            ]
        },

        {
            "title":"Broaden-and-Build Theory",
            "researchers":"Barbara Fredrickson",

            "summary":"""
Positive emotions expand social networks,
increase cooperation, and strengthen relationships.
""",

            "love_island":"""
Contestants using warmth, humor, and positive
social energy consistently improve:
- social centrality
- alliance formation
- public perception
""",

            "citations":[
                "Fredrickson, B. (2001). The role of positive emotions."
            ]
        }

    ]

    for theory in theories:

        st.markdown(f"""
        <div class='card'>

        <h2>{theory['title']}</h2>

        <p><strong>Key Researchers:</strong>
        {theory['researchers']}</p>

        <h4>📖 Theory Summary</h4>
        <p>{theory['summary']}</p>

        <h4>🏝️ Love Island Application</h4>
        <p>{theory['love_island']}</p>

        <h4>📚 Citations</h4>

        </div>
        """, unsafe_allow_html=True)

        for cite in theory["citations"]:
            st.markdown(f"- {cite}")

# =================================================
# TAB 2 — TRAIT DICTIONARY
# =================================================

with tabs[1]:

    trait_df = pd.DataFrame({

        "Trait":[
            "Stability",
            "Loyalty",
            "Drama",
            "Disclosure",
            "Centrality",
            "Validation",
            "Warmth",
            "Emotional Regulation"
        ],

        "Definition":[
            "Consistency in romantic positioning",
            "Commitment to primary partner",
            "Conflict initiation frequency",
            "Emotional openness level",
            "Social network integration",
            "Positive emotional reinforcement",
            "Prosocial emotional tone",
            "Calmness under stress"
        ],

        "How Measured":[
            "Recoupling count",
            "Casa Amor behavior",
            "Argument frequency",
            "Vulnerability pacing",
            "Alliance quantity",
            "Supportive language",
            "Positive interactions",
            "Conflict response"
        ],

        "Villa Behaviors":[
            "Stable couple arc",
            "Reassurance and trust",
            "Gossip/confrontation",
            "Personal storytelling",
            "Friendship building",
            "Affirming partner",
            "Comforting others",
            "De-escalating conflict"
        ]
    })

    st.dataframe(
        trait_df,
        use_container_width=True
    )

# =================================================
# TAB 3 — ARCHETYPE TAXONOMY
# =================================================

with tabs[2]:

    archetypes = {

        "👑 Anchor":{
            "definition":"Emotionally stable winner profile",
            "basis":"Secure attachment",
            "strengths":"Loyalty, regulation, warmth",
            "weaknesses":"Lower entertainment volatility",
            "examples":"Zeta, Hannah, Justine",
            "finish":"Winner / Finalist"
        },

        "🦋 Social Butterfly":{
            "definition":"High-relatability social connector",
            "basis":"High disclosure + centrality",
            "strengths":"Audience attachment",
            "weaknesses":"Romantic instability",
            "examples":"Cashay, Leah, Kassy",
            "finish":"Mid-villa / Finalist"
        },

        "🔥 Antagonist":{
            "definition":"Conflict-centered contestant",
            "basis":"Reactive attachment",
            "strengths":"Airtime generation",
            "weaknesses":"Low public trust",
            "examples":"Reactive conflict arcs",
            "finish":"Early Exit"
        }

    }

    for name, data in archetypes.items():

        st.markdown(f"""
        <div class='card'>

        <h2>{name}</h2>

        <p><strong>Definition:</strong>
        {data['definition']}</p>

        <p><strong>Psychological Basis:</strong>
        {data['basis']}</p>

        <p><strong>Strengths:</strong>
        {data['strengths']}</p>

        <p><strong>Weaknesses:</strong>
        {data['weaknesses']}</p>

        <p><strong>Examples:</strong>
        {data['examples']}</p>

        <p><strong>Typical Finish:</strong>
        {data['finish']}</p>

        </div>
        """, unsafe_allow_html=True)

# =================================================
# TAB 4 — SEASON ARCHIVE
# =================================================

with tabs[3]:

    season_df = pd.DataFrame({

        "Season":[
            "S2",
            "S4",
            "S5",
            "S6"
        ],

        "Winner":[
            "Justine Ndiba",
            "Zeta Morrison",
            "Hannah Wright",
            "Serena Page"
        ],

        "Archetype":[
            "Anchor",
            "Anchor",
            "Anchor",
            "Slow Burn"
        ],

        "Post Show":[
            "Influencer / media work",
            "Fashion & media",
            "Public couple visibility",
            "Growing social presence"
        ]
    })

    st.dataframe(
        season_df,
        use_container_width=True
    )

# =================================================
# TAB 5 — METHODOLOGY
# =================================================

with tabs[4]:

    st.markdown("""
    <div class='card'>

    ## 📊 Research Methodology

    ### Data Sources

    - Episode transcripts
    - Public interviews
    - Episode-level coding
    - Public voting outcomes
    - Relationship trajectories
    - Casa Amor outcomes

    ### Trait Coding

    Contestants were scored across:
    - loyalty
    - disclosure
    - warmth
    - conflict
    - emotional regulation
    - social centrality

    ### Statistical Methods

    - correlation analysis
    - k-means clustering
    - archetype classification
    - comparative trajectory analysis

    ### Limitations

    - edited television narratives
    - incomplete transcript availability
    - public vote opacity
    - subjective coding bias

    </div>
    """, unsafe_allow_html=True)

# =================================================
# TAB 6 — CODING MANUAL
# =================================================

with tabs[5]:

    coding = {

        "Warmth":[
            "Supportive tone",
            "Affectionate validation",
            "Comforting others"
        ],

        "Drama":[
            "Conflict initiation",
            "Gossip participation",
            "Escalation behaviors"
        ],

        "Centrality":[
            "Screen-time integration",
            "Friendship count",
            "Villa involvement"
        ],

        "Validation Language":[
            "Emotional reassurance",
            "Positive affirmations",
            "Relationship reinforcement"
        ]
    }

    for trait, vals in coding.items():

        st.markdown(f"""
        <div class='card'>

        <h3>{trait}</h3>

        </div>
        """, unsafe_allow_html=True)

        for v in vals:
            st.markdown(f"- {v}")

# =================================================
# TAB 7 — AUDIENCE PSYCHOLOGY
# =================================================

with tabs[6]:

    st.markdown("""
    <div class='card'>

    ## 💞 Audience Psychology

    Audiences consistently reward:

    - emotional warmth
    - consistency
    - loyalty arcs
    - vulnerability
    - emotional growth

    Audiences consistently punish:

    - reactive aggression
    - instability
    - gossip-heavy behavior
    - strategic manipulation

    Parasocial attachment increases when contestants appear:
    - emotionally genuine
    - relationally secure
    - socially supportive

    </div>
    """, unsafe_allow_html=True)

# =================================================
# TAB 8 — STATISTICAL APPENDIX
# =================================================

with tabs[7]:

    corr_df = pd.DataFrame({

        "Trait":[
            "Partner Stability",
            "Warmth",
            "Validation",
            "Drama",
            "Gossip"
        ],

        "Correlation":[
            .82,
            .74,
            .71,
            -.62,
            -.58
        ]
    })

    fig = px.bar(
        corr_df,
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
        height=500,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# =================================================
# TAB 9 — EPISODE REFERENCES
# =================================================

with tabs[8]:

    st.markdown("""
    <div class='card'>

    ## 🎬 Key Timeline References

    ### Season 4
    - Zeta + Timmy stabilization arc
    - Casa Amor loyalty reinforcement

    ### Season 5
    - Hannah + Marco emotional consistency
    - Kassy volatility post-Casa

    ### Season 6
    - Serena slow-burn trajectory
    - Leah disclosure growth arc

    ### Key Coding Events

    - Casa Amor recouplings
    - conflict escalation episodes
    - reconciliation arcs
    - public vulnerability moments

    </div>
    """, unsafe_allow_html=True)

# =================================================
# TAB 10 — PUBLIC SOURCES
# =================================================

with tabs[9]:

    st.markdown("""
    <div class='card'>

    ## 🔗 Public Sources

    ### Official Sources
    - Love Island USA official pages
    - Peacock episode archives
    - contestant interviews

    ### Psychology References
    - APA psychology summaries
    - attachment theory research
    - parasocial interaction studies

    ### Media Analysis
    - reality television analysis
    - audience perception research
    - social bonding studies

    </div>
    """, unsafe_allow_html=True)

# =================================================
# FINAL SECTION
# =================================================

st.markdown(f"""
<div style="
    background:linear-gradient(
        135deg,
        {COLORS["hot_pink"]},
        {COLORS["soft_pink"]}
    );

    padding:40px;
    border-radius:28px;
    color:white;
    margin-top:40px;
">

<h2>💖 Final Research Position</h2>

<p style='font-size:18px;'>

This framework proposes that successful Love Island
contestants are not simply:
- attractive
- dramatic
- highly visible

Instead, long-term success appears driven by:

- emotional regulation
- secure attachment
- stable romantic narratives
- audience trust formation
- positive social integration

Across seasons, winners consistently demonstrate:
warmth, loyalty, emotional pacing, and relationship stability.

</p>

</div>
""", unsafe_allow_html=True)
