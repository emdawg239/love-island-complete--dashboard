import streamlit as st
from auth import check_password

st.set_page_config(
    page_title="Love Island Research Dashboard",
    page_icon="💖",
    layout="wide",
    initial_sidebar_state="expanded"
)

check_password()

st.sidebar.title("Navigation")

with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown("""
<div class='hero'>
<h1 style='font-size:72px;'>Love Island USA Research Dashboard</h1>

<p style='font-size:22px;'>
Complete behavioral, psychological, communication,
visual-branding, and social-network analysis
of successful female contestants across Seasons 1–6.
</p>

</div>
""", unsafe_allow_html=True)

cols = st.columns(4)

metrics = [
("6", "Seasons"),
("94", "Contestants"),
("10", "Behavioral Variables"),
("76%", "Prediction Accuracy")
]

for c, m in zip(cols, metrics):
    with c:
        st.markdown(f'''
        <div class='metric'>
        <h2>{m[0]}</h2>
        <p>{m[1]}</p>
        </div>
        ''', unsafe_allow_html=True)

st.markdown("""
<div class='card'>

## Executive Summary

Female winners consistently display:

- High emotional regulation
- Strong partner loyalty
- Warm communication patterns
- Strong female alliances
- Low conflict initiation
- Consistent visual branding

Early exits consistently display:

- Emotional volatility
- High gossip involvement
- Frequent recouplings
- Reactive communication
- Low social integration

### Top Predictors of Winning

- Partner stability (r=.82)
- Warm validation language (r=.74)
- Social centrality (r=.68)
- Visual consistency (r=.55)
- Low conflict initiation (r=-.62)

Use the sidebar to navigate through the complete dashboard.

</div>
""", unsafe_allow_html=True)
