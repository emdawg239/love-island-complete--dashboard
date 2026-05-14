
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
    background: linear-gradient(180deg,#fff0f7,#ffe6f2);
    color:#34192b;
}

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg,#ff4f98,#ff9fcf);
}

section[data-testid="stSidebar"] * {
    color:white !important;
}

.hero {
    background: linear-gradient(135deg,#ff4f98,#ff8fc5,#ffd1e6);
    padding:80px;
    border-radius:32px;
    color:white;
    margin-bottom:35px;
    box-shadow:0 20px 60px rgba(255,79,152,.25);
}

.card {
    background:white;
    border-radius:28px;
    padding:35px;
    margin-bottom:24px;
    box-shadow:0 10px 30px rgba(0,0,0,.08);
}

.metric {
    background:white;
    border-radius:22px;
    padding:24px;
    text-align:center;
    box-shadow:0 10px 25px rgba(0,0,0,.06);
}

.metric h2 {
    color:#ff4f98;
    font-size:42px;
}

.tag {
    display:inline-block;
    background:#ff4f98;
    color:white;
    padding:6px 12px;
    border-radius:999px;
    margin-right:8px;
    margin-top:8px;
    font-size:12px;
}
