
import streamlit as st

st.title("Complete Week-by-Week Playbook")

weeks={
"Weeks 1–2 — First Impressions":[
"Pick partner based on authentic chemistry",
"Use graduated self-disclosure",
"Build 2+ genuine female friendships",
"Avoid all early conflict initiation",
"Wear warm-toned outfits and consistent styling",
"Share humor early before vulnerability"
],

"Weeks 3–4 — Deepening the Bond":[
"Escalate emotional vulnerability",
"Increase validation language",
"Use playful teasing and inside jokes",
"Expand social capital",
"Verbally reinforce loyalty"
],

"Casa Amor — Defining Test":[
"Stay loyal where possible",
"Display calm emotional regulation",
"Strengthen female alliances",
"Respond with authentic emotion not aggression",
"Do not escalate public confrontation"
],

"Weeks 6–7 — Post Casa Recovery":[
"Resolve Casa conflict quickly",
"Increase vulnerability",
"Build couple narrative",
"Share future plans",
"Increase positive dialogue ratio"
],

"Weeks 7–8 — Finals Preparation":[
"Zero new conflict",
"Use warmth and gratitude",
"Maintain visual consistency",
"Discuss real-world plans",
"Express genuine uncertainty about outcome"
]
}

for week,items in weeks.items():
    with st.expander(week):
        for i in items:
            st.markdown(f"- {i}")
