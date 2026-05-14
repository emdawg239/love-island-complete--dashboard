
import streamlit as st
import plotly.express as px
import pandas as pd

st.title("Correlation Analysis")

df = pd.DataFrame({
'Trait':[
'Partner Stability',
'Warm Sentiment',
'Validation Frequency',
'Social Centrality',
'Consistent Color Palette',
'Low Conflict Initiation',
'Gossip Participation',
'Outfit Volatility'
],
'Correlation':[.82,.74,.71,.68,.55,-.62,-.58,-.41]
})

fig = px.bar(
df,
x='Correlation',
y='Trait',
orientation='h',
color='Correlation',
title='Winning Correlation Matrix',
color_continuous_scale=['#ff9fcf','#ff4f98']
)

st.plotly_chart(fig,use_container_width=True)

st.markdown('''
## Interpretation

Strongest positive predictors:
- partner stability
- emotional warmth
- validation frequency
- social centrality

Strongest negative predictors:
- drama
- gossip participation
- conflict initiation
- inconsistent identity

Contestants with stable couples consistently outperform contestants
with chaotic recoupling behavior.
''')
