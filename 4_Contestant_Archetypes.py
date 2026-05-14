
import streamlit as st
import plotly.graph_objects as go

st.title("Winner Archetype Radar")

categories=[
'Stability',
'Disclosure',
'Humor',
'Validation',
'Sentiment',
'Centrality',
'Loyalty',
'Low Drama'
]

winner=[7.8,7.4,6.8,7.9,7.1,7.2,8.1,6.9]
average=[5.1,5.5,5.3,5.8,5.6,5.4,5.9,4.8]

fig = go.Figure()

fig.add_trace(go.Scatterpolar(
r=winner,
theta=categories,
fill='toself',
name='Winner Mean',
line_color='#ff4f98'
))

fig.add_trace(go.Scatterpolar(
r=average,
theta=categories,
fill='toself',
name='Average Contestant',
line_color='#888780'
))

fig.update_layout(
height=700,
polar=dict(radialaxis=dict(visible=True,range=[0,10]))
)

st.plotly_chart(fig,use_container_width=True)

st.markdown('''
Winners are substantially higher on:
- emotional validation
- loyalty
- social intelligence
- emotional regulation

and substantially lower on:
- drama
- conflict
- instability
''')
