import streamlit as st
import base64
import os
import time

# ----------------------------------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------------------------------
st.set_page_config(
    page_title="The Man Behind My Dreams",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

IMAGES_DIR = "images"


def img_to_base64(path):
    """Return base64 string of an image, or None if it doesn't exist."""
    if path and os.path.exists(path):
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return None


def image_or_placeholder(filename, alt_emoji="📷", height="320px", radius="22px"):
    """
    Returns an <img> tag if the image exists in /images,
    otherwise returns a soft glassmorphic placeholder box
    so the page never breaks while you swap in real photos.
    """
    path = os.path.join(IMAGES_DIR, filename)
    b64 = img_to_base64(path)
    if b64:
        ext = filename.split(".")[-1]
        return f'''<img src="data:image/{ext};base64,{b64}"
                    style="width:100%;height:{height};object-fit:cover;
                    border-radius:{radius};display:block;" />'''
    else:
        return f'''<div style="width:100%;height:{height};border-radius:{radius};
                    background:linear-gradient(135deg, rgba(255,255,255,0.35), rgba(212,175,55,0.18));
                    display:flex;align-items:center;justify-content:center;
                    border:2px dashed rgba(212,175,55,0.55);">
                    <span style="font-size:42px;opacity:0.6;">{alt_emoji}</span>
                    </div>'''


# ----------------------------------------------------------------------------
# GLOBAL CSS — Warm Cream / White / Gold Glassmorphic Theme
# ----------------------------------------------------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,500;0,700;1,500&family=Poppins:wght@300;400;500;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

#MainMenu, header, footer {visibility: hidden;}

.stApp {
    background: linear-gradient(180deg, #fffdf7 0%, #fff6e8 40%, #fdf0d8 100%);
}

.block-container {
    padding-top: 0rem !important;
    padding-bottom: 0rem !important;
    max-width: 100% !important;
}

/* ---------- Headings ---------- */
.serif-title {
    font-family: 'Playfair Display', serif;
}

/* ---------- INTRO / HERO ---------- */
.hero {
    position: relative;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    background: radial-gradient(ellipse at top, #1b1f3b 0%, #0d0e21 60%, #05050f 100%);
    border-radius: 0 0 40px 40px;
    overflow: hidden;
    padding: 60px 20px;
}

.stars {
    position: absolute;
    inset: 0;
    background-image:
        radial-gradient(2px 2px at 20px 30px, #ffffff, transparent),
        radial-gradient(2px 2px at 120px 80px, #ffffff, transparent),
        radial-gradient(1.5px 1.5px at 200px 150px, #ffd700aa, transparent),
        radial-gradient(2px 2px at 300px 60px, #ffffff, transparent),
        radial-gradient(1.5px 1.5px at 400px 200px, #ffffff, transparent),
        radial-gradient(2px 2px at 500px 100px, #ffd700aa, transparent),
        radial-gradient(1.5px 1.5px at 80px 250px, #ffffff, transparent),
        radial-gradient(2px 2px at 600px 300px, #ffffff, transparent);
    background-repeat: repeat;
    background-size: 650px 400px;
    animation: twinkle 4s ease-in-out infinite alternate;
    opacity: 0.8;
}

@keyframes twinkle {
    from { opacity: 0.4; }
    to { opacity: 0.95; }
}

.hero-line1 {
    color: #f5e6c8;
    font-size: clamp(20px, 3.4vw, 34px);
    font-style: italic;
    font-family: 'Playfair Display', serif;
    max-width: 760px;
    line-height: 1.5;
    margin-bottom: 22px;
    animation: fadeInUp 1.6s ease-out;
    text-shadow: 0 0 18px rgba(255, 215, 0, 0.25);
}

.hero-sub {
    color: #ffd700;
    font-size: clamp(28px, 4.2vw, 46px);
    font-weight: 700;
    font-family: 'Playfair Display', serif;
    margin-top: 18px;
    animation: fadeInUp 2.2s ease-out;
    text-shadow: 0 0 25px rgba(255,215,0,0.4);
}

@keyframes fadeInUp {
    0% { opacity: 0; transform: translateY(25px); }
    100% { opacity: 1; transform: translateY(0); }
}

.hero-photo-wrap {
    margin-top: 36px;
    animation: fadeInUp 2.8s ease-out;
}

.hero-photo-frame {
    width: 230px;
    border-radius: 50%;
    padding: 6px;
    background: linear-gradient(135deg, #ffd700, #fff7df, #d4af37);
    box-shadow: 0 0 40px rgba(255, 215, 0, 0.35);
}

/* ---------- SECTION GENERAL ---------- */
.section-wrap {
    padding: 90px 6% 60px 6%;
}

.section-title {
    text-align: center;
    font-family: 'Playfair Display', serif;
    font-size: clamp(28px, 4vw, 42px);
    color: #5c4423;
    margin-bottom: 8px;
}

.section-sub {
    text-align: center;
    color: #9c7f4d;
    font-size: 16px;
    margin-bottom: 50px;
    font-style: italic;
}

/* ---------- GLASS CARD BASE ---------- */
.glass {
    background: rgba(255, 255, 255, 0.55);
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    border: 1px solid rgba(212, 175, 55, 0.35);
    border-radius: 26px;
    box-shadow: 0 8px 32px rgba(180, 140, 60, 0.15);
}

/* ---------- MEMORY CARDS ---------- */
.memory-card {
    padding: 14px 14px 22px 14px;
    margin-bottom: 28px;
    transition: transform 0.35s ease, box-shadow 0.35s ease;
}
.memory-card:hover {
    transform: translateY(-6px) scale(1.015);
    box-shadow: 0 16px 40px rgba(180, 140, 60, 0.28);
}
.memory-caption {
    margin-top: 16px;
    font-size: 15.5px;
    color: #5c4423;
    line-height: 1.55;
    font-style: italic;
    text-align: center;
    padding: 0 6px;
}

/* ---------- GIFT CARDS ---------- */
.gift-card {
    padding: 26px 16px;
    text-align: center;
    cursor: pointer;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    min-height: 150px;
    display:flex;
    flex-direction:column;
    align-items:center;
    justify-content:center;
}
.gift-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 14px 34px rgba(180, 140, 60, 0.3);
}
.gift-emoji { font-size: 38px; margin-bottom: 10px; }
.gift-label {
    font-family: 'Playfair Display', serif;
    font-size: 19px;
    color: #6b4f23;
    font-weight: 700;
}
.gift-message {
    margin-top: 14px;
    font-size: 14.5px;
    color: #5c4423;
    font-style: italic;
    line-height: 1.5;
}

/* ---------- LETTER SECTION ---------- */
.letter-panel {
    background: linear-gradient(135deg, #fffaf0, #fbeecb);
    border: 1px solid rgba(212,175,55,0.4);
    border-radius: 30px;
    padding: 50px 40px;
    max-width: 760px;
    margin: 0 auto 40px auto;
    box-shadow: 0 10px 40px rgba(180,140,60,0.18);
    background-image: repeating-linear-gradient(
        rgba(212,175,55,0.05) 0px,
        rgba(212,175,55,0.05) 1px,
        transparent 1px,
        transparent 32px
    );
}
.letter-text {
    font-family: 'Playfair Display', serif;
    font-size: clamp(17px, 1.8vw, 21px);
    color: #5c4423;
    line-height: 1.9;
    text-align: center;
    font-style: italic;
}

.shine-banner {
    text-align: center;
    max-width: 720px;
    margin: 0 auto 50px auto;
    padding: 26px 20px;
    border-radius: 22px;
    background: linear-gradient(120deg, #fff7df, #ffe9b0, #fff7df, #ffd700aa);
    background-size: 300% 300%;
    animation: shineMove 6s ease infinite;
    font-family: 'Playfair Display', serif;
    font-size: clamp(18px, 2.2vw, 24px);
    color: #5c3e12;
    font-weight: 600;
    box-shadow: 0 8px 30px rgba(212,175,55,0.3);
}
@keyframes shineMove {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

/* ---------- HUG BUTTON ---------- */
div.stButton > button {
    background: linear-gradient(135deg, #d4af37, #ffd700, #d4af37);
    color: #3b2a0f;
    font-family: 'Playfair Display', serif;
    font-size: 20px;
    font-weight: 700;
    padding: 16px 46px;
    border-radius: 50px;
    border: none;
    box-shadow: 0 0 0 0 rgba(255,215,0,0.55);
    animation: pulse 2.2s infinite;
    transition: transform 0.25s ease;
}
div.stButton > button:hover {
    transform: scale(1.05);
}
@keyframes pulse {
    0% { box-shadow: 0 0 0 0 rgba(255,215,0,0.55); }
    70% { box-shadow: 0 0 0 22px rgba(255,215,0,0); }
    100% { box-shadow: 0 0 0 0 rgba(255,215,0,0); }
}

.final-reveal {
    max-width: 480px;
    margin: 40px auto 0 auto;
    padding: 20px;
    text-align: center;
    animation: fadeInUp 1.2s ease-out;
}
.final-reveal-caption {
    margin-top: 18px;
    font-family: 'Playfair Display', serif;
    font-size: clamp(20px, 2.6vw, 28px);
    color: #6b4f23;
    font-weight: 700;
}

.footer-note {
    text-align: center;
    padding: 40px 20px 60px 20px;
    color: #b4965c;
    font-size: 14px;
    font-style: italic;
}
</style>
""", unsafe_allow_html=True)


# ----------------------------------------------------------------------------
# SESSION STATE
# ----------------------------------------------------------------------------
if "show_hug" not in st.session_state:
    st.session_state.show_hug = False

if "opened_gifts" not in st.session_state:
    st.session_state.opened_gifts = {}


# ----------------------------------------------------------------------------
# INTRO / HERO SECTION
# ----------------------------------------------------------------------------
hero_photo_html = image_or_placeholder(
    "papa-solo.jpg", alt_emoji="🧔", height="218px", radius="50%"
)

st.markdown(f"""
<div class="hero">
    <div class="stars"></div>
    <div style="position:relative; z-index:2;">
        <div class="hero-line1">
            "Every superhero wears a cape...<br>But mine wore responsibility."
        </div>
        <div class="hero-sub">Happy Father's Day Papa ❤️</div>
        <div class="hero-photo-wrap">
            <div class="hero-photo-frame">
                {hero_photo_html}
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)


# ----------------------------------------------------------------------------
# SECTION 1 — OUR BEAUTIFUL JOURNEY
# ----------------------------------------------------------------------------
st.markdown('<div class="section-wrap">', unsafe_allow_html=True)
st.markdown('<div class="section-title serif-title">🛤 Our Beautiful Journey</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">A few simple moments that mean everything</div>', unsafe_allow_html=True)

memories = [
    ("together-1.jpg", "🤝",
     "You've been my anchor from day one. Every beautiful memory I have started with you."),
    ("papa-solo-2.jpg", "🧔",
     "Watching you handle life with so much strength and patience taught me how to handle mine."),
    ("together-2.jpg", "🤝",
     "No matter how big the storm outside, knowing you are in my corner makes me feel completely safe."),
    ("together-3.jpg", "🤝",
     "Every single dream I chase is possible because you never once doubted what I could achieve."),
]

cols = st.columns(2)
for i, (fname, emoji, caption) in enumerate(memories):
    with cols[i % 2]:
        photo_html = image_or_placeholder(fname, alt_emoji=emoji, height="300px", radius="20px")
        st.markdown(f"""
        <div class="glass memory-card">
            {photo_html}
            <div class="memory-caption">"{caption}"</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)


# ----------------------------------------------------------------------------
# SECTION 2 — WHAT YOU GAVE ME (Interactive Gift Cards)
# ----------------------------------------------------------------------------
st.markdown('<div class="section-wrap">', unsafe_allow_html=True)
st.markdown('<div class="section-title serif-title">🎁 What You Gave Me</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">Tap a card to open the gift</div>', unsafe_allow_html=True)

gifts = [
    ("Strength", "💪", "You taught me to stand tall, even when the wind blows fierce."),
    ("Discipline", "📖", "The quiet routine and wisdom that built my foundation."),
    ("Confidence", "✨", "Because you believed in me, I finally believed in myself."),
    ("Kindness", "❤️", "The softest, most loving heart hidden behind the toughest exterior."),
    ("Dreams", "🌈", "You gave me wings before I even knew how to fly."),
]

gift_cols = st.columns(5)
for i, (label, emoji, message) in enumerate(gifts):
    with gift_cols[i]:
        is_open = st.session_state.opened_gifts.get(label, False)
        if st.button(f"{emoji}\n{label}", key=f"gift_{label}", use_container_width=True):
            st.session_state.opened_gifts[label] = not is_open
            is_open = st.session_state.opened_gifts[label]

        if is_open:
            st.markdown(f"""
            <div class="glass gift-card" style="margin-top:10px;">
                <div class="gift-emoji">{emoji}</div>
                <div class="gift-label">{label}</div>
                <div class="gift-message">"{message}"</div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="glass gift-card" style="margin-top:10px; opacity:0.85;">
                <div class="gift-emoji">{emoji}</div>
                <div class="gift-label">{label}</div>
                <div class="gift-message" style="opacity:0.5;">Tap above to open ✨</div>
            </div>
            """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)


# ----------------------------------------------------------------------------
# SECTION 3 — A LETTER & ONE LAST HUG
# ----------------------------------------------------------------------------
st.markdown('<div class="section-wrap">', unsafe_allow_html=True)
st.markdown('<div class="section-title serif-title">✍ A Letter & One Last Hug</div>', unsafe_allow_html=True)

st.markdown("""
<div class="letter-panel">
    <div class="letter-text">
        Papa, I may not say it every day, but every achievement of mine carries your fingerprints.
        Every dream I chase is possible because you never stopped believing in me.
        Thank you for being my first teacher, first protector, and forever hero.
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="shine-banner">
    Behind every successful daughter stands a father who never gave up.<br>Thank You Papa ❤️
</div>
""", unsafe_allow_html=True)

btn_col = st.columns([1, 1, 1])
with btn_col[1]:
    if st.button("One Last Hug 🤗", key="hug_button", use_container_width=True):
        st.session_state.show_hug = True

if st.session_state.show_hug:
    st.balloons()
    st.snow()

    final_photo_html = image_or_placeholder(
        "together-best.jpg", alt_emoji="❤️", height="320px", radius="24px"
    )

    st.markdown(f"""
    <div class="glass final-reveal">
        {final_photo_html}
        <div class="final-reveal-caption">I Love You Papa.<br>Forever and Always. ✨</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

st.markdown("""
<div class="footer-note">
    Made with all my love, for the man behind every dream I've ever dared to chase. 🤍
</div>
""", unsafe_allow_html=True)
