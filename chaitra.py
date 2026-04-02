import streamlit as st
import datetime
import random

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="For Bangaramm 💕",
    page_icon="💌",
    layout="centered"
)

# ── Global styles ─────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400;1,600&family=DM+Sans:wght@300;400&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    background-color: #0d0a14;
    color: #f5e9f7;
}
.stApp { background-color: #0d0a14; }

h1, h2, h3 { font-family: 'Cormorant Garamond', serif; font-style: italic; }

.big-title {
    font-family: 'Cormorant Garamond', serif;
    font-style: italic;
    font-size: 3rem;
    color: #f9c8d9;
    text-align: center;
    line-height: 1.2;
    margin-bottom: 0.2rem;
}
.subtitle {
    text-align: center;
    font-size: 0.95rem;
    color: #c9a8d4;
    margin-bottom: 2rem;
    letter-spacing: 0.08em;
}
.msg-card {
    background: linear-gradient(135deg, #1e0f2e 0%, #2a1040 100%);
    border: 1px solid #6b3fa0;
    border-radius: 20px;
    padding: 2.2rem 2.5rem;
    margin: 1.5rem 0;
    text-align: center;
    box-shadow: 0 0 40px #9b59b620;
}
.msg-label {
    font-size: 0.75rem;
    letter-spacing: 0.18em;
    color: #c9a8d4;
    text-transform: uppercase;
    margin-bottom: 1rem;
}
.msg-text {
    font-family: 'Cormorant Garamond', serif;
    font-style: italic;
    font-size: 1.6rem;
    color: #fce4ec;
    line-height: 1.5;
}
.msg-from { margin-top: 1.2rem; font-size: 0.85rem; color: #b085c9; }

.date-card {
    background: linear-gradient(135deg, #1a0a2e, #2a1040);
    border: 1px solid #9b59b640;
    border-radius: 16px;
    padding: 1.5rem 2rem;
    text-align: center;
    margin: 1.5rem 0;
}
.date-num {
    font-family: 'Cormorant Garamond', serif;
    font-size: 3.5rem;
    color: #f9c8d9;
    line-height: 1;
}
.date-label {
    font-size: 0.8rem;
    letter-spacing: 0.15em;
    color: #c9a8d4;
    text-transform: uppercase;
    margin-top: 0.3rem;
}
.soft-divider {
    border: none;
    border-top: 1px solid #3d1f5e44;
    margin: 2.5rem 0;
}
.star-section-title {
    font-family: 'Cormorant Garamond', serif;
    font-style: italic;
    font-size: 2rem;
    color: #f9c8d9;
    text-align: center;
    margin: 2rem 0 0.3rem;
}
.star-section-sub {
    text-align: center;
    font-size: 0.85rem;
    color: #9b7ab5;
    margin-bottom: 1.2rem;
}
.star-reveal {
    background: linear-gradient(135deg, #1e0f2e, #2a1040);
    border: 1px solid #9b59b666;
    border-radius: 16px;
    padding: 1.4rem 1.8rem;
    text-align: center;
    margin-top: 0.8rem;
}
.star-reveal-title {
    font-family: 'Cormorant Garamond', serif;
    font-style: italic;
    font-size: 1.4rem;
    color: #f9c8d9;
    margin-bottom: 0.5rem;
}
.star-reveal-desc {
    font-size: 0.95rem;
    color: #c9a8d4;
    line-height: 1.6;
}
.footer {
    text-align: center;
    font-size: 0.8rem;
    color: #6b3fa0;
    margin-top: 3rem;
    padding-bottom: 2rem;
}

/* Style star buttons */
div[data-testid="column"] .stButton button {
    background: transparent !important;
    border: none !important;
    font-size: 1.8rem !important;
    padding: 0.3rem 0.5rem !important;
    color: #f9c8d9 !important;
    text-shadow: 0 0 10px #f9c8d988 !important;
    box-shadow: none !important;
    width: 100% !important;
    transition: transform 0.2s !important;
}
div[data-testid="column"] .stButton button:hover {
    transform: scale(1.3) !important;
    text-shadow: 0 0 22px #f9c8d9cc !important;
    background: transparent !important;
    border: none !important;
}
</style>
""", unsafe_allow_html=True)

# ── Data ──────────────────────────────────────────────────────────────────────
MESSAGES = [
    "Always remember, you're my barre 💜",
    "Ahaaaaaaaaa mastttt unnnav today 😍",
    "Today's reminder: You make every day better just by existing 💕",
    '"Nak brain ledu" — J. Chaitra, probably 😂',
    "Bangaramm, I don't know what I did to deserve you, but I'm glad I did it 😁",
    "Every time you smile, I forget what I was even worrying about 🌸",
    "You're my favourite person to do nothing with 💫",
    "Why did you steal my heart HUH?? 💋",
    "You didn't just steal my heart — you ran away with it and I'm not even mad 🏃‍♀️💜",
    "Chaitra, you are my home 🏡💕",
    "Just a reminder:I think you're literally perfect today 🌟",
    "You're the best plot twist of my life!  📖💗",
]

STARS = [
    ("Your eyes ✨",                   "The first thing I noticed about you and still my favourite view. 👀"),
    ("Your nose 🌸",                   "Honestly so cute I'd kiss it everyday. 😁"),
    ("Your lips 💋",                   "Hehe you know. 😉"),
    ("The way you make me happy 😊",   "You do it without even trying. Your magical babess. 😁"),
    ("The way you stole my heart 💜",  "Didn't even ask. Just took it. Your rude. 🤭"),
    ("Your laugh 🌙",                  "It's the sound I want to hear every single day. 😚"),
    ("🫶🏻💕",         "I never wanna see you sad because of me. 🙁💋"),
    ("How you say my name 🗣️",        "You dont say. 🙂"),
    ("Your random questions 🌌",    "Chaitra's(Barre) brain is undefeated and I love it. 🤭😚"),
    ("The way you care 🤍",            "You love me so deeply. It's one of the most beautiful things about you. And you have always done your best for me! 😚"),
    ("Your voice 🎶",                   "Soo soo good that I wanna hear it everyday. 😘"),
    ("Just... you 💫",                 "All of it. Every single part. I wouldn't change a thing. 🌟"),
]

STAR_EMOJIS = ["★", "✦", "✶", "✸", "⭐", "🌟", "💫", "✨", "★", "✦", "✶", "✸"]

# ── Day's Since Together! :) ────────────────────────────────────────────────────────────
DAYS_TOGETHER = datetime.date(2025, 3, 5)   

# ── Session state ─────────────────────────────────────────────────────────────
if "selected_star" not in st.session_state:
    st.session_state.selected_star = None

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown('<div class="big-title">For Bangaramm 💌</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">made with love by Lakshya · just for you, Chaitra</div>', unsafe_allow_html=True)

# ── Daily message ─────────────────────────────────────────────────────────────
today = datetime.date.today()
daily_msg = MESSAGES[today.toordinal() % len(MESSAGES)]

st.markdown(f"""
<div class="msg-card">
    <div class="msg-label">✦ today's love note · {today.strftime("%B %d, %Y")} ✦</div>
    <div class="msg-text">"{daily_msg}"</div>
    <div class="msg-from">— Lakshya 💜</div>
</div>
""", unsafe_allow_html=True)

# ── Days counter ──────────────────────────────────────────────────────────────
days = (today - DAYS_TOGETHER).days
st.markdown(f"""
<div class="date-card">
    <div class="date-label">days since our first kiss 💋</div>
    <div class="date-num">{days}</div>
    <div class="date-label" style="margin-top:0.5rem;">and every one of them has been worth it</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<hr class="soft-divider">', unsafe_allow_html=True)

# ── Star map ──────────────────────────────────────────────────────────────────
st.markdown('<div class="star-section-title">A sky full of reasons ⭐</div>', unsafe_allow_html=True)
st.markdown('<div class="star-section-sub">every star is something I love about you · tap one  babess</div>', unsafe_allow_html=True)

# 4 stars per row
cols_per_row = 4
rows = [STARS[i:i+cols_per_row] for i in range(0, len(STARS), cols_per_row)]

for row_idx, row in enumerate(rows):
    cols = st.columns(len(row))
    for col_idx in range(len(row)):
        star_i = row_idx * cols_per_row + col_idx
        with cols[col_idx]:
            if st.button(STAR_EMOJIS[star_i], key=f"star_{star_i}"):
                st.session_state.selected_star = star_i

# Show reveal card when a star is selected
if st.session_state.selected_star is not None:
    title, desc = STARS[st.session_state.selected_star]
    st.markdown(f"""
    <div class="star-reveal">
        <div class="star-reveal-title">{title}</div>
        <div class="star-reveal-desc">{desc}</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<hr class="soft-divider">', unsafe_allow_html=True)

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="footer">
    with a lot of love and using our combined brain cells 🧠💜<br>
    — Lakshya, your mogudu 😁👉👈
</div>
""", unsafe_allow_html=True)
