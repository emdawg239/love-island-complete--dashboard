import streamlit as st
import plotly.graph_objects as go

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

st.title("💖 Complete Love Island Strategic Playbook")

st.markdown("""
A behavioral intelligence framework modeling how
real contestants successfully navigate:
- emotional dynamics
- public perception
- Casa Amor
- relationship stabilization
- parasocial audience attachment
""")

# ------------------------------------------------
# ARCHETYPE TABS
# ------------------------------------------------

tab1, tab2, tab3, tab4 = st.tabs([
    "👑 Anchor Strategy",
    "🦋 Social Butterfly",
    "🔥 Antagonist",
    "🌅 Slow Burn"
])

# ------------------------------------------------
# PLAYBOOK DATA
# ------------------------------------------------

playbooks = {

"👑 Anchor Strategy": {

    "examples":[
        "Zeta Morrison",
        "Hannah Wright",
        "Justine Ndiba"
    ],

    "weeks": {

        "Weeks 1–2 — First Impressions": {

            "probability":[12,18,24,31,39],

            "actions":[
                "Prioritize one stable emotional connection",
                "Use calm validation language early",
                "Build strong female alliances",
                "Avoid becoming central villa drama",
                "Project warmth and emotional consistency"
            ],

            "avoid":[
                "Love triangles",
                "Aggressive confrontation",
                "Over-sharing too early",
                "Visible jealousy"
            ],

            "psychology":"""
Early emotional warmth and calm regulation
increase trustworthiness and perceived relationship stability.
"""
        },

        "Weeks 3–4 — Couple Consolidation": {

            "probability":[31,38,44,52,61],

            "actions":[
                "Deepen vulnerability gradually",
                "Reinforce loyalty verbally",
                "Create inside jokes and rituals",
                "Maintain visual consistency",
                "Publicly support partner"
            ],

            "avoid":[
                "Public emotional spirals",
                "Testing partner loyalty",
                "Emotional inconsistency"
            ],

            "psychology":"""
Consistent reinforcement behaviors increase parasocial
investment from viewers and stabilize public trust.
"""
        },

        "Casa Amor — Defining Test": {

            "probability":[41,48,55,68,79],

            "actions":[
                "Stay emotionally regulated",
                "Maintain dignity during uncertainty",
                "Avoid retaliatory recoupling",
                "Display emotional maturity"
            ],

            "avoid":[
                "Revenge flirting",
                "Public breakdowns",
                "Hostile reactions"
            ],

            "psychology":"""
Audiences strongly reward emotional control
during high-chaos periods like Casa Amor.
"""
        },

        "Weeks 6–8 — Finals Arc": {

            "probability":[72,78,85,93,100],

            "actions":[
                "Focus on gratitude and authenticity",
                "Discuss real-world future plans",
                "Maintain stable emotional tone",
                "Show couple growth arc"
            ],

            "avoid":[
                "New conflicts",
                "Last-minute indecision",
                "Attention-seeking behavior"
            ],

            "psychology":"""
Finalist couples succeed when audiences perceive
a believable long-term emotional trajectory.
"""
        }
    }
},

"🦋 Social Butterfly": {

    "examples":[
        "Cashay Proudfoot",
        "Leah Kateb",
        "Kassy Castillo"
    ],

    "weeks": {

        "Weeks 1–2 — Build Visibility": {

            "probability":[18,25,32,36,40],

            "actions":[
                "Maximize social integration",
                "Become emotionally relatable",
                "Use humor and openness",
                "Build friendships rapidly"
            ],

            "avoid":[
                "Becoming romantically chaotic too early",
                "Overcommitting emotionally",
                "Attention-seeking conflict"
            ],

            "psychology":"""
High relatability increases audience attachment
but instability reduces long-term winner probability.
"""
        },

        "Casa Amor — Critical Balance": {

            "probability":[38,42,47,55,63],

            "actions":[
                "Stay emotionally transparent",
                "Protect audience sympathy",
                "Avoid visible manipulation"
            ],

            "avoid":[
                "Flip-flopping repeatedly",
                "Using jealousy strategically",
                "Excessive flirting"
            ],

            "psychology":"""
Social butterflies thrive on emotional visibility
but public trust drops sharply after inconsistency.
"""
        }
    }
},

"🔥 Antagonist": {

    "examples":[
        "High-conflict contestants across multiple seasons"
    ],

    "weeks": {

        "Weeks 1–2 — Controlled Chaos": {

            "probability":[8,10,9,7,5],

            "actions":[
                "Use selective conflict only",
                "Maintain some vulnerability",
                "Avoid becoming isolated socially"
            ],

            "avoid":[
                "Constant gossip",
                "Reactive aggression",
                "Targeting multiple contestants"
            ],

            "psychology":"""
Drama creates airtime but sustained conflict
rapidly erodes public favor.
"""
        }
    }
},

"🌅 Slow Burn": {

    "examples":[
        "Serena Page",
        "Camilla Thurlow",
        "Jessie Wynter"
    ],

    "weeks": {

        "Weeks 1–2 — Quiet Positioning": {

            "probability":[5,9,14,18,24],

            "actions":[
                "Stay low-visibility but warm",
                "Avoid early coupling pressure",
                "Build quiet alliances",
                "Observe villa dynamics carefully"
            ],

            "avoid":[
                "Forcing emotional intimacy",
                "Trying to dominate screen time",
                "Early emotional dependency"
            ],

            "psychology":"""
Slow burns often underperform early but gain
massive audience support through authenticity over time.
"""
        },

        "Post Casa — Emotional Growth Arc": {

            "probability":[42,53,66,79,91],

            "actions":[
                "Increase vulnerability",
                "Demonstrate emotional resilience",
                "Lean into authenticity",
                "Build audience empathy"
            ],

            "avoid":[
                "Emotional shutdown",
                "Passive communication",
                "Avoiding vulnerability"
            ],

            "psychology":"""
Audiences strongly reward visible emotional growth
and redemption arcs after Casa Amor.
"""
        }
    }
}

}

# ------------------------------------------------
# FUNCTION
# ------------------------------------------------

def render_playbook(strategy_name):

    data = playbooks[strategy_name]

    st.markdown(f"""
    <div class='card'>

    <h2>{strategy_name}</h2>

    <p>
    Historical examples:
    {", ".join(data['examples'])}
    </p>

    </div>
    """, unsafe_allow_html=True)

    for week, content in data["weeks"].items():

        with st.expander(week):

            # ------------------------------------------------
            # SUCCESS CURVE
            # ------------------------------------------------

            fig = go.Figure()

            fig.add_trace(go.Scatter(
                y=content["probability"],
                mode="lines+markers",

                line=dict(
                    color=COLORS["hot_pink"],
                    width=5
                ),

                marker=dict(
                    size=10,
                    color=COLORS["gold"]
                )
            ))

            fig.update_layout(
                height=250,

                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",

                margin=dict(
                    l=20,
                    r=20,
                    t=20,
                    b=20
                ),

                xaxis_title="Timeline",
                yaxis_title="Win Probability %",

                font=dict(
                    family="Poppins",
                    color=COLORS["dark"]
                )
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

            # ------------------------------------------------
            # STRATEGIC ACTIONS
            # ------------------------------------------------

            st.markdown("### 💖 Recommended Behaviors")

            for item in content["actions"]:

                st.markdown(f"- {item}")

            # ------------------------------------------------
            # AVOID SECTION
            # ------------------------------------------------

            st.markdown(f"""
            <div style="
                background:#ffe0e8;
                padding:20px;
                border-radius:18px;
                margin-top:20px;
                margin-bottom:20px;
            ">

            <h3>🚫 What NOT To Do</h3>

            </div>
            """, unsafe_allow_html=True)

            for item in content["avoid"]:

                st.markdown(f"- {item}")

            # ------------------------------------------------
            # PSYCHOLOGY
            # ------------------------------------------------

            with st.expander("🧠 Why This Works"):

                st.markdown(content["psychology"])

# ------------------------------------------------
# RENDER TABS
# ------------------------------------------------

with tab1:
    render_playbook("👑 Anchor Strategy")

with tab2:
    render_playbook("🦋 Social Butterfly")

with tab3:
    render_playbook("🔥 Antagonist")

with tab4:
    render_playbook("🌅 Slow Burn")

# ------------------------------------------------
# FINAL INSIGHT
# ------------------------------------------------

st.markdown("""
<div class='card'>

## 🌴 Final Research Insight

Successful Love Island contestants do NOT simply:
- create drama
- maximize airtime
- pursue multiple relationships

Instead, the strongest long-term performers:
- stabilize emotionally over time
- maintain consistent relationship narratives
- cultivate audience trust
- demonstrate emotional growth after adversity

The most successful contestants balance:
- relatability
- vulnerability
- loyalty
- emotional regulation

while avoiding:
- reactive conflict
- instability
- social isolation.

</div>
""", unsafe_allow_html=True)
