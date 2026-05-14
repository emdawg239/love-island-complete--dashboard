
import streamlit as st

st.title("Contestant Archetypes")

cards = [
{
'title':'The Anchor',
'desc':'Emotionally stable, low drama, one strong couple. Avg finish: winner or finalist in 88% of appearances. The most common winner profile.',
'tags':['High loyalty','Low drama','Secure attach.'],
'example':'Examples include contestants like Zeta who balanced emotional security with strong relationship consistency.'
},
{
'title':'The Social Butterfly',
'desc':'High centrality, moderate drama, multiple recouplings. Likeable but struggles to convert network into public votes. Avg finish: mid-villa.',
'tags':['High centrality','Mid drama','Low loyalty'],
'example':'Often extremely popular inside the villa but lacks strong couple stability.'
},
{
'title':'The Antagonist',
'desc':'High drama, high conflict initiation, low self-disclosure. Gets airtime but almost never wins public vote. Avg finish: early-mid exit.',
'tags':['High drama','High conflict','Low disclose'],
'example':'Contestants heavily tied to gossip arcs or reactive confrontations consistently lose public trust.'
},
{
'title':'The Slow Burn',
'desc':'Low early visibility, high emotional intelligence, peaks post-Casa. Underperforms weeks 1–2, overperforms weeks 5–8. Avg finish: finalist.',
'tags':['High EI','Low conflict','Late bloomer'],
'example':'These contestants often gain popularity after audiences observe emotional maturity over time.'
}
]

for card in cards:
    tags=''.join([f"<span class=tag>{t}</span>" for t in card['tags']])

    st.markdown(f'''
    <div class='card'>
    <h2>{card['title']}</h2>
    <p>{card['desc']}</p>
    <p><strong>Behavioral Example:</strong> {card['example']}</p>
    {tags}
    </div>
    ''',unsafe_allow_html=True)
