import random
import uuid
from pathlib import Path

import streamlit as st

from data.db import add_photo, add_score, get_leaderboard, get_photos, init_db
from data.i18n import RTL_LANGS, t
from data.itinerary import ITINERARY_DAYS, ITINERARY_NOTES
from data.questions import QUESTIONS

ROOT = Path(__file__).parent
UPLOADS_DIR = ROOT / "uploads"
UPLOADS_DIR.mkdir(exist_ok=True)
ASSETS_DIR = ROOT / "assets"
HERO_WELCOME = ASSETS_DIR / "hero_sestriere.jpg"
HERO_HOME = ASSETS_DIR / "village_vialattea.jpg"

init_db()

st.set_page_config(page_title="Pragelato & Turin - Le Quiz", page_icon="🏔️", layout="centered")

DEFAULTS = {
    "nickname": "",
    "lang": "fr",
    "screen": "nickname",
    "quiz_category": "mix",
    "quiz_questions": [],
    "quiz_index": 0,
    "quiz_score": 0,
    "quiz_answered": False,
    "quiz_selected": None,
    "leaderboard_category": "",
}
for key, value in DEFAULTS.items():
    if key not in st.session_state:
        st.session_state[key] = value


def tt(key, **kwargs):
    return t(st.session_state.lang, key, **kwargs)


def go(screen):
    st.session_state.screen = screen
    st.rerun()


def start_quiz(category):
    pool = QUESTIONS if category == "mix" else [q for q in QUESTIONS if q["category"] == category]
    st.session_state.quiz_category = category
    st.session_state.quiz_questions = random.sample(pool, min(8, len(pool)))
    st.session_state.quiz_index = 0
    st.session_state.quiz_score = 0
    st.session_state.quiz_answered = False
    st.session_state.quiz_selected = None
    go("quiz")


def finish_quiz():
    score = st.session_state.quiz_score
    total = len(st.session_state.quiz_questions)
    add_score(st.session_state.nickname, st.session_state.quiz_category, score, total)
    go("result")


def render_hero(image_path, credit):
    if image_path.exists():
        st.image(str(image_path), use_container_width=True)
        st.caption(credit)


# --- Bascule de langue (avant tout le reste pour eviter un flash LTR/RTL) ---

lang_col1, lang_col2 = st.columns([3, 2])
with lang_col2:
    lang_choice = st.radio(
        "lang",
        ["FR", "עברית"],
        index=0 if st.session_state.lang == "fr" else 1,
        horizontal=True,
        label_visibility="collapsed",
        key="lang_radio",
    )
st.session_state.lang = "fr" if lang_choice == "FR" else "he"

rtl = st.session_state.lang in RTL_LANGS

st.markdown(
    f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700;800&family=Noto+Sans+Hebrew:wght@400;600;700;800&display=swap');

    header[data-testid="stHeader"] {{ display: none; }}

    html, body, [class*="css"] {{
        font-family: 'Poppins', 'Noto Sans Hebrew', sans-serif;
    }}

    .stApp {{
        direction: {"rtl" if rtl else "ltr"};
        background: #fdfbf6;
    }}

    .block-container {{ max-width: 560px; padding-top: 2.5rem; }}

    h1, h2, h3 {{
        color: #14181c;
        font-weight: 800;
        letter-spacing: -0.01em;
    }}

    [data-testid="stImage"] img {{
        border-radius: 20px;
    }}

    div.stButton > button, div.stFormSubmitButton > button, div.stLinkButton > a {{
        width: 100%;
        border-radius: 999px;
        font-weight: 700;
        border: none;
        background: #0a5a86;
        color: #ffffff;
        padding: 0.65rem 1rem;
        text-align: center;
        text-decoration: none;
        justify-content: center;
    }}
    div.stButton > button:hover, div.stFormSubmitButton > button:hover, div.stLinkButton > a:hover {{
        background: #073f5f;
        color: #ffffff;
    }}
    div.stButton > button[kind*="secondary"], div.stFormSubmitButton > button[kind*="secondary"] {{
        background: #f0e6cf;
        color: #14181c;
    }}
    div.stButton > button[kind*="secondary"]:hover, div.stFormSubmitButton > button[kind*="secondary"]:hover {{
        background: #e4d6ae;
        color: #14181c;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

with lang_col1:
    st.markdown(f"### {tt('app_title')}")

st.divider()

# --- Ecrans ---

if st.session_state.screen == "nickname":
    render_hero(HERO_WELCOME, "📷 Sestriere, Via Lattea — ChiaVB, Wikimedia Commons (CC BY-SA 3.0)")
    st.markdown(f"## {tt('welcome_title')}")
    st.write(tt("welcome_subtitle"))
    with st.form("nickname_form"):
        nickname = st.text_input(tt("nickname_label"), placeholder=tt("nickname_placeholder"), max_chars=30)
        submitted = st.form_submit_button(tt("start_btn"))
        if submitted:
            if nickname.strip():
                st.session_state.nickname = nickname.strip()
                go("home")
            else:
                st.warning(tt("nickname_required"))

elif st.session_state.screen == "home":
    render_hero(HERO_HOME, "📷 Via Lattea — Smt42, Wikimedia Commons (CC BY-SA 4.0)")
    st.markdown(f"## {tt('home_greeting', name=st.session_state.nickname)}")
    st.write(tt("home_subtitle"))

    if st.button(f"📅 {tt('card_itinerary_title')}", use_container_width=True, key="btn_itinerary"):
        go("itinerary")

    col1, col2 = st.columns(2)
    with col1:
        if st.button(f"🏔️ {tt('card_village_title')}", use_container_width=True, key="btn_village"):
            start_quiz("village")
        if st.button(f"🎲 {tt('card_mix_title')}", use_container_width=True, key="btn_mix"):
            start_quiz("mix")
    with col2:
        if st.button(f"🏛️ {tt('card_turin_title')}", use_container_width=True, key="btn_turin"):
            start_quiz("turin")
        if st.button(f"🏆 {tt('card_leaderboard_title')}", use_container_width=True, key="btn_leaderboard"):
            go("leaderboard")

    if st.button(f"📸 {tt('card_gallery_title')}", use_container_width=True, key="btn_gallery"):
        go("gallery")

    st.write("")
    st.markdown(f"#### {tt('videos_title')}")
    vid_col1, vid_col2 = st.columns(2)
    with vid_col1:
        st.link_button(tt("video_winter"), "https://youtu.be/X19uE3Zd9E0", use_container_width=True)
    with vid_col2:
        st.link_button(tt("video_summer"), "https://youtu.be/vZjeXf-52bE", use_container_width=True)

    st.write("")
    st.markdown(f"#### {tt('docs_title')}")
    doc_col1, doc_col2 = st.columns(2)
    with doc_col1:
        st.link_button(tt("doc_winter"), "https://factsheets.clubmed/en-gb/factsheet_prac_winter.pdf", use_container_width=True)
    with doc_col2:
        st.link_button(tt("doc_summer"), "https://factsheets.clubmed/en-gb/factsheet_prac_summer.pdf", use_container_width=True)

    st.write("")
    if st.button(tt("change_nickname"), key="btn_change_nick"):
        go("nickname")

elif st.session_state.screen == "itinerary":
    lang = st.session_state.lang
    st.markdown(f"## {tt('itinerary_title')}")

    st.markdown(f"**{tt('itinerary_notes_title')}**")
    for note in ITINERARY_NOTES[lang]:
        st.markdown(f"- {note}")

    for day in ITINERARY_DAYS:
        st.divider()
        st.markdown(f"### {day['day_name'][lang]} | {day['date']}")
        for item in day["items"]:
            st.markdown(f"**{item['time']}** — {item[lang]}")

    st.write("")
    if st.button(tt("back_btn"), key="itinerary_back"):
        go("home")

elif st.session_state.screen == "quiz":
    questions = st.session_state.quiz_questions
    idx = st.session_state.quiz_index
    q = questions[idx]
    lang = st.session_state.lang

    st.progress(idx / len(questions))
    st.caption(tt("quiz_progress", current=idx + 1, total=len(questions)))
    st.markdown(f"### {q['question'][lang]}")

    if not st.session_state.quiz_answered:
        for i, opt in enumerate(q["options"][lang]):
            if st.button(opt, key=f"opt_{idx}_{i}", use_container_width=True):
                st.session_state.quiz_selected = i
                st.session_state.quiz_answered = True
                if i == q["answer_index"]:
                    st.session_state.quiz_score += 1
                st.rerun()
    else:
        for i, opt in enumerate(q["options"][lang]):
            if i == q["answer_index"]:
                st.success(f"✅ {opt}")
            elif i == st.session_state.quiz_selected:
                st.error(f"❌ {opt}")
            else:
                st.write(opt)
        st.info(q["fun_fact"][lang])

        is_last = idx + 1 >= len(questions)
        next_label = tt("quiz_see_score") if is_last else tt("quiz_next")
        if st.button(next_label, key="quiz_next_btn", use_container_width=True):
            if is_last:
                finish_quiz()
            else:
                st.session_state.quiz_index += 1
                st.session_state.quiz_answered = False
                st.session_state.quiz_selected = None
                st.rerun()

    st.write("")
    if st.button(tt("quiz_quit"), key="quiz_quit_btn"):
        go("home")

elif st.session_state.screen == "result":
    score = st.session_state.quiz_score
    total = len(st.session_state.quiz_questions)
    ratio = score / total if total else 0
    emoji = "🏆" if ratio == 1 else "🎉" if ratio >= 0.7 else "👍" if ratio >= 0.4 else "🙂"
    title = tt("result_perfect") if ratio == 1 else tt("result_great") if ratio >= 0.7 else tt("result_good")

    st.markdown(f"## {emoji} {title}")
    st.write(tt("result_score_line", name=st.session_state.nickname, score=score, total=total))

    col1, col2 = st.columns(2)
    with col1:
        if st.button(tt("retry_btn"), use_container_width=True, key="retry_btn"):
            start_quiz(st.session_state.quiz_category)
    with col2:
        if st.button(tt("home_btn"), use_container_width=True, key="result_home_btn"):
            go("home")

elif st.session_state.screen == "leaderboard":
    st.markdown(f"## {tt('leaderboard_title')}")

    tabs = [("", "tab_all"), ("village", "tab_village"), ("turin", "tab_turin"), ("mix", "tab_mix")]
    cols = st.columns(4)
    for col, (cat_value, key) in zip(cols, tabs):
        with col:
            active = st.session_state.leaderboard_category == cat_value
            if st.button(tt(key), key=f"lb_tab_{cat_value or 'all'}", use_container_width=True, type="primary" if active else "secondary"):
                st.session_state.leaderboard_category = cat_value
                st.rerun()

    rows = get_leaderboard(st.session_state.leaderboard_category or None)
    if not rows:
        st.info(tt("leaderboard_empty"))
    else:
        cat_label_key = {"village": "tab_village", "turin": "tab_turin", "mix": "tab_mix"}
        for i, r in enumerate(rows, start=1):
            cat_label = tt(cat_label_key.get(r["category"], "tab_mix"))
            st.markdown(f"**#{i} — {r['nickname']}** &nbsp;·&nbsp; {cat_label} &nbsp;·&nbsp; **{r['score']}/{r['total']}**")

    st.write("")
    if st.button(tt("back_btn"), key="lb_back"):
        go("home")

elif st.session_state.screen == "gallery":
    st.markdown(f"## {tt('gallery_title')}")

    with st.expander(tt("add_photo_title"), expanded=False):
        with st.form("photo_form", clear_on_submit=True):
            photo_file = st.file_uploader(tt("photo_label"), type=["png", "jpg", "jpeg", "webp"])
            caption = st.text_input(tt("caption_label"), placeholder=tt("caption_placeholder"), max_chars=200)
            submitted = st.form_submit_button(tt("publish_btn"))
            if submitted:
                if not photo_file:
                    st.warning(tt("photo_required"))
                else:
                    ext = Path(photo_file.name).suffix or ".jpg"
                    filename = f"{uuid.uuid4()}{ext}"
                    (UPLOADS_DIR / filename).write_bytes(photo_file.getbuffer())
                    add_photo(st.session_state.nickname or "Anonyme", caption.strip(), filename)
                    st.success(tt("photo_success"))
                    st.rerun()

    photos = get_photos()
    if not photos:
        st.info(tt("gallery_empty"))
    else:
        cols = st.columns(2)
        for i, p in enumerate(photos):
            with cols[i % 2]:
                img_path = UPLOADS_DIR / p["filename"]
                if img_path.exists():
                    st.image(str(img_path), use_container_width=True)
                if p["caption"]:
                    st.caption(p["caption"])
                st.caption(tt("gallery_by", name=p["nickname"]))

    st.write("")
    if st.button(tt("back_btn"), key="gallery_back"):
        go("home")
