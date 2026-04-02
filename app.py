
import streamlit as st
import datetime
import random
import math

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

h1, h2, h3 {
    font-family: 'Cormorant Garamond', serif;
    font-style: italic;
}

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

/* Message card */
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

.msg-from {
    margin-top: 1.2rem;
    font-size: 0.85rem;
    color: #b085c9;
}

/* Star map */
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
    margin-bottom: 1.5rem;
}

/* Star tooltip card */
.star-info {
    background: #1e0f2e;
    border: 1px solid #6b3fa055;
    border-radius: 14px;
    padding: 1rem 1.4rem;
    text-align: center;
    margin-top: 0.5rem;
}

/* Date section */
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

/* Divider */
.soft-divider {
    border: none;
    border-top: 1px solid #3d1f5e44;
    margin: 2.5rem 0;
}

/* Footer */
.footer {
    text-align: center;
    font-size: 0.8rem;
    color: #6b3fa0;
    margin-top: 3rem;
    padding-bottom: 2rem;
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
    ("Your eyes ✨", "The first thing I noticed about you and still my favourite view."),
    ("Your nose 🌸", "Honestly so cute I don't know what to say."),
    ("Your lips 💋", "Enough said."),
    ("The way you make me happy 😊", "You do it without even trying. That's the magic."),
    ("The way you stole my heart 💜", "Didn't even ask. Just took it. Rude. I love it."),
    ("Your laugh 🌙", "It's the sound I want to hear every single day."),
    ("Your stubbornness 😤💕", "Drives me crazy. Also drives me to be better."),
    ("How you say my name 🗣️", "Nobody else says it like you do."),
    ("Your random 3am thoughts 🌌", "Chaitra's brain is undefeated and I love it."),
    ("The way you care 🤍", "You love people so deeply. It's one of the most beautiful things about you."),
    ("Your vibe 🎶", "Unmatchable. Unreplicable. Very much mine."),
    ("Just... you 💫", "All of it. Every single part. I wouldn't change a thing."),
]

# ── Day's Since Together! :) ────────────────────────────────────────────────────────────
DAYS_TOGETHER = datetime.date(2025, 3, 5)   
# ── Header ────────────────────────────────────────────────────────────────────
st.markdown('<div class="big-title">For Bangaramm 💌</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">made with love by Lakshya · just for you, Chaitra</div>', unsafe_allow_html=True)

# ── Daily message ─────────────────────────────────────────────────────────────
today = datetime.date.today()
msg_index = today.toordinal() % len(MESSAGES)
daily_msg = MESSAGES[msg_index]

st.markdown(f"""
<div class="msg-card">
    <div class="msg-label">✦ today's love note · {today.strftime("%B %d, %Y")} ✦</div>
    <div class="msg-text">"{daily_msg}"</div>
    <div class="msg-from">— Lakshya 💜</div>
</div>
""", unsafe_allow_html=True)

# ── Days since together display ─────────────────────────────────────────────────────
days_together = (today - DAYS_TOGETHER).days

st.markdown(f"""
<div class="date-card">
    <div class="date-label">days since we are together! 💋</div>
    <div class="date-num">{days_together}</div>
    <div class="date-label" style="margin-top:0.5rem;">and every one of them has been worth it</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<hr class="soft-divider">', unsafe_allow_html=True)

# ── Star map ──────────────────────────────────────────────────────────────────
st.markdown('<div class="star-section-title">A sky full of reasons ⭐ "I can not make it work"😕</div>', unsafe_allow_html=True)
st.markdown('<div class="star-section-sub">every star is something I love about you · tap one to read it</div>', unsafe_allow_html=True)

# Generate stable star positions using index as seed
def star_positions(n, width=700, height=380, seed=42):
    rng = random.Random(seed)
    positions = []
    for i in range(n):
        x = rng.randint(40, width - 40)
        y = rng.randint(30, height - 30)
        size = rng.choice([14, 18, 22, 16, 20])
        positions.append((x, y, size))
    return positions

positions = star_positions(len(STARS))

# Build SVG star map
svg_stars = ""
for i, (x, y, size) in enumerate(positions):
    label = STARS[i][0]
    svg_stars += f'''
    <g class="star-group" onclick="selectStar({i})" style="cursor:pointer;" id="star-{i}">
      <circle cx="{x}" cy="{y}" r="{size//2 + 6}" fill="transparent"/>
      <text x="{x}" y="{y}" text-anchor="middle" dominant-baseline="middle"
            font-size="{size}" fill="#f9c8d9"
            style="filter: drop-shadow(0 0 6px #f9c8d988); transition: font-size 0.2s;"
            onmouseover="this.style.fontSize='{size+4}px'" 
            onmouseout="this.style.fontSize='{size}px'">★</text>
    </g>
    '''

# Twinkle dots (tiny background stars)
bg_stars = ""
rng2 = random.Random(99)
for _ in range(60):
    bx = rng2.randint(0, 700)
    by = rng2.randint(0, 380)
    br = rng2.uniform(0.8, 2)
    bg_stars += f'<circle cx="{bx}" cy="{by}" r="{br}" fill="#ffffff" opacity="{rng2.uniform(0.2,0.6)}"/>'

star_svg = f"""
<svg viewBox="0 0 700 380" xmlns="http://www.w3.org/2000/svg" width="100%" style="border-radius:20px; background: radial-gradient(ellipse at 50% 60%, #1a0a2e 0%, #0d0a14 100%); border: 1px solid #3d1f5e;">
  {bg_stars}
  {svg_stars}
  <text x="350" y="365" text-anchor="middle" font-size="11" fill="#6b3fa0" font-family="DM Sans, sans-serif">tap a star ✦</text>
</svg>

<script>
function selectStar(i) {{
    const stars = {str([(s[0], s[1]) for s in STARS])};
    const descs = {str([s[1] for s in STARS])};
    document.getElementById('star-label').innerText = stars[i][0];
    document.getElementById('star-desc').innerText = descs[i];
    document.getElementById('star-info').style.display = 'block';
}}
</script>

<div id="star-info" style="display:none; background:#1e0f2e; border:1px solid #6b3fa055; border-radius:14px; padding:1rem 1.4rem; text-align:center; margin-top:0.8rem;">
    <div style="font-family:'Cormorant Garamond',serif; font-style:italic; font-size:1.3rem; color:#f9c8d9;" id="star-label"></div>
    <div style="font-size:0.9rem; color:#c9a8d4; margin-top:0.5rem;" id="star-desc"></div>
</div>
"""

st.markdown(star_svg, unsafe_allow_html=True)

st.markdown('<hr class="soft-divider">', unsafe_allow_html=True)

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="footer">
    made secretly, with a lot of love and zero brain cells 🧠💜<br>
    — Lakshya, your biggest fan
</div>
""", unsafe_allow_html=True)
