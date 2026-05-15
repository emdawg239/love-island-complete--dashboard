
import streamlit as st

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

st.title("🧠 Psychological Framework")

st.markdown("""
A behavioral psychology framework explaining why
certain contestants consistently outperform others
in:
- audience perception
- relationship stability
- public voting
- long-term villa integration
""")

# ------------------------------------------------
# THEORY DATA
# ------------------------------------------------

theories = [

{
    "title":"💖 Attachment Theory",

    "desc":"""
Winning contestants overwhelmingly display
secure attachment behaviors:
- emotional openness
- calm communication
- relational consistency
- low jealousy
- emotional regulation
""",

    "real_examples":[
        "Zeta Morrison calmly de-escalating conflict",
        "Hannah Wright reinforcing emotional security with Marco",
        "Serena Page maintaining emotional transparency post-Casa"
    ],

    "behavioral_indicators":{

        "Secure":[
            "Calm tone during conflict",
            "Consistent eye contact",
            "Comfort with vulnerability",
            "Low emotional reactivity",
            "Direct communication"
        ],

        "Anxious":[
            "Reassurance seeking",
            "Jealousy spikes",
            "Emotional volatility",
            "Fear of abandonment"
        ],

        "Avoidant":[
            "Humor deflection",
            "Emotional distancing",
            "Low vulnerability",
            "Difficulty reassuring partner"
        ]
    },

    "archetypes":[
        "👑 Anchors → secure attachment",
        "🦋 Social Butterflies → anxious-avoidant blend",
        "🔥 Antagonists → insecure + reactive",
        "🌅 Slow Burns → secure but low early disclosure"
    ],

    "audience_interpretation":[
        "They're genuine",
        "They're emotionally safe",
        "They're relationship-ready",
        "They're not performing"
    ]
},

{
    "title":"🌴 Social Perception Theory",

    "desc":"""
Public voting behavior strongly rewards:
- warmth over dominance
- consistency over unpredictability
- prosocial behavior over aggression
- emotional maturity over chaos
""",

    "real_examples":[
        "Justine Ndiba comforting islanders during conflict",
        "Serena Page maintaining calm emotional tone post-Casa",
        "Cashay gaining audience support through warmth and humor"
    ],

    "behavioral_indicators":{

        "Warmth Cues":[
            "Soft smiles",
            "Open posture",
            "Gentle teasing",
            "Supportive tone",
            "Comforting behaviors"
        ],

        "Consistency Cues":[
            "Same romantic partner",
            "Stable emotional tone",
            "Consistent styling",
            "Predictable reactions"
        ],

        "Prosocial Cues":[
            "De-escalating conflict",
            "Supporting friends",
            "Encouraging others",
            "Repairing tension"
        ]
    },

    "archetypes":[
        "👑 Anchors → highest public trust",
        "🦋 Social Butterflies → highest relatability",
        "🔥 Antagonists → highest airtime but lowest trust",
        "🌅 Slow Burns → strongest long-term audience growth"
    ],

    "audience_interpretation":[
        "They're kind",
        "They're trustworthy",
        "They're emotionally mature",
        "I'd vote for them"
    ]
},

{
    "title":"💬 Social Penetration Theory",

    "desc":"""
Gradual reciprocal self-disclosure strongly predicts:
- intimacy
- emotional trust
- parasocial bonding
- public support
""",

    "real_examples":[
        "Leah Kateb increasing emotional openness over time",
        "Zeta slowly revealing vulnerability rather than oversharing",
        "Serena building emotional intimacy gradually"
    ],

    "behavioral_indicators":{

        "Healthy Disclosure":[
            "Gradual vulnerability",
            "Balanced openness",
            "Reciprocal sharing",
            "Emotional pacing"
        ],

        "Over-Disclosure":[
            "Trauma dumping early",
            "Immediate attachment",
            "Hyper-emotional conflict"
        ],

        "Under-Disclosure":[
            "Emotional walls",
            "Detached humor",
            "Avoiding intimacy"
        ]
    },

    "archetypes":[
        "👑 Anchors → paced emotional disclosure",
        "🦋 Social Butterflies → high emotional openness",
        "🔥 Antagonists → low authentic disclosure",
        "🌅 Slow Burns → delayed but meaningful vulnerability"
    ],

    "audience_interpretation":[
        "They're authentic",
        "They're emotionally real",
        "They're vulnerable in a healthy way",
        "They're opening up naturally"
    ]
},

{
    "title":"✨ Broaden-and-Build Theory",

    "desc":"""
Positive emotional expression broadens:
- social networks
- alliance formation
- romantic bonding
- audience attachment
""",

    "real_examples":[
        "Cashay using humor to build social centrality",
        "Hannah creating emotionally positive villa interactions",
        "Serena increasing audience empathy through warmth"
    ],

    "behavioral_indicators":{

        "Positive Behaviors":[
            "Humor",
            "Playfulness",
            "Affection",
            "Supportive validation",
            "Joyful reactions"
        ],

        "Negative Spiral Behaviors":[
            "Reactive conflict",
            "Emotional shutdown",
            "Social isolation",
            "Bitterness"
        ]
    },

    "archetypes":[
        "👑 Anchors → emotionally stabilizing",
        "🦋 Social Butterflies → socially expansive",
        "🔥 Antagonists → emotionally narrowing",
        "🌅 Slow Burns → gradually emotionally expansive"
    ],

    "audience_interpretation":[
        "They're fun to watch",
        "They make the villa better",
        "They feel emotionally healthy",
        "People want them around"
    ]
}

]

# ------------------------------------------------
# RENDER THEORY SECTIONS
# ------------------------------------------------

for theory in theories:

    st.markdown(f"""
    <div class='card'>

    <h1>{theory['title']}</h1>

    <p>{theory['desc']}</p>

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

        st.markdown("### 💖 Real Love Island Examples")

        for item in theory["real_examples"]:

            st.markdown(f"- {item}")

        st.markdown("")

        st.markdown("### 🧠 Archetype Expression")

        for item in theory["archetypes"]:

            st.markdown(f"- {item}")

        st.markdown("")

        st.markdown("### 👀 Audience Interpretation")

        for item in theory["audience_interpretation"]:

            st.markdown(f"- {item}")

    # ------------------------------------------------
    # RIGHT COLUMN
    # ------------------------------------------------

    with col2:

        st.markdown("### 🌴 Behavioral Indicators")

        for section, behaviors in theory["behavioral_indicators"].items():

            st.markdown(f"""
            <div style="
                background:white;
                padding:18px;
                border-radius:18px;
                margin-bottom:18px;
                box-shadow:0 8px 20px rgba(0,0,0,.06);
            ">

            <h4 style='color:{COLORS["hot_pink"]};'>
            {section}
            </h4>

            </div>
            """, unsafe_allow_html=True)

            for behavior in behaviors:

                st.markdown(f"- {behavior}")

    st.markdown("---")

# ------------------------------------------------
# FINAL INSIGHT
# ------------------------------------------------

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

<h2>🌴 Core Psychological Finding</h2>

<p style='font-size:18px;'>

Winning contestants consistently combine:

- emotional regulation
- warmth
- secure attachment
- strategic vulnerability
- social consistency

while avoiding:

- emotional volatility
- reactive confrontation
- unstable romantic positioning
- parasocial distrust

The most successful contestants are not necessarily
the loudest or most dramatic.

They are the contestants who make audiences feel:
safe, emotionally connected, and invested long-term.

</p>

</div>
""", unsafe_allow_html=True)
