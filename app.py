"""
Autobiography and Portfolio App
CSIT 349 - Applied AI (G01)
Jezer R. Malubay

Run with:  streamlit run app.py
"""

import os
from datetime import datetime

import numpy as np
import pandas as pd
import streamlit as st

# ----------------------------------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------------------------------
st.set_page_config(
    page_title="Jezer Malubay | Portfolio",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ----------------------------------------------------------------------------
# INFO
# ----------------------------------------------------------------------------
NAME = "Jezer R. Malubay"
NICKNAME = "Fatchoi"
PROGRAM = "BS Information Technology"
SCHOOL = "Cebu Institute of Technology – University"
YEAR_LEVEL = "4th Year" 
SECTION = "CSIT 349 · Applied AI · Section G01"
EMAIL = "malubayjezer@gmail.com"  
GITHUB = "https://github.com/fatchoii"  
LINKEDIN = "https://www.linkedin.com/in/jezer-malubay-4460ba448/"  
PHOTO_PATH = "photo.png"  

TAGLINE = "Aspiring project manager and developer who likes turning plans into working systems."

BIO = (
    "I am a Computer Studies student at Cebu Institute of Technology – University. "
    "I enjoy the planning side of software as much as the coding side, which is why "
    "I often end up as the Project Manager or Product Owner of my group projects. "
    "I like web development, and I am now exploring how data and machine learning "
    "can be used on real, local problems."
)  

AUTOBIOGRAPHY = {
    "Background": (
        "I grew in in three places in the Philippines, namely first in siargao and manila for elementary and cebu for highschool and college. "
        "I have always been interested in technology, and I have been tinkering with computers since I was a kid. I am now pursuing a degree in Information Technology at Cebu Institute of Technology – University."
    ),  
    "Education": (
        "I am taking up Information Technology at Cebu Institute of Technology – "
        "University. Along the way I have worked with Django, React.js, and Spring "
        "Boot in group web development subjects, and I took IT Project Management "
        "(IT317) as an advance summer class."
    ),
    "Interests": (
        "Project management, web development, and applied AI."
        "My hobbies include music, games, or outdoor activities."
    ),  
    "Goals": (
        "Finish my capstone, grow as a developer who can also lead a team, and "
        "build software that is useful to real people."
    ),  
}

MILESTONES = [
    {"Year": "2021", "Milestone": "Started BSIT at CIT-U"},  # EDIT years
    {"Year": "2025", "Milestone": "Took IT317 IT Project Management as an advance summer class"},
    {"Year": "2026", "Milestone": "Became Project Manager / Product Owner of MarketLink"},
    {"Year": "2026", "Milestone": "Built a Spring Boot CRUD from the EduReach ERD"},
    {"Year": "2026", "Milestone": "Started the Applied AI SMS spam clustering project"},
    {"Year": "2026", "Milestone": "Started Capstone / Research 1 with my group"},
]

# Self-rated skill levels out of 100. EDIT these to your honest numbers.
SKILLS = pd.DataFrame(
    {
        "Skill": [
            "Project Management",
            "Spring Boot",
            "React.js",
            "Django",
            "Python / Data Analysis",
            "Documentation",
            "Teamwork",
        ],
        "Category": [
            "Management",
            "Backend",
            "Frontend",
            "Backend",
            "Data / AI",
            "Management",
            "Management",
        ],
        "Level": [85, 65, 60, 60, 55, 80, 85],
        "Years": [2, 1, 1, 1, 1, 3, 3],
    }
)

PROJECTS = [
    {
        "title": "MarketLink",
        "subtitle": "E-commerce Marketplace Management System",
        "role": "Project Manager / Product Owner",
        "course": "IT317 · IT Project Management",
        "tools": ["Project Charter", "Risk Register", "Sprint Planning", "Web stack (edit)"],
        "status": "In progress",
        "progress": 40,  
        "summary": (
            "A marketplace system for managing buyers, sellers, and orders. I lead the "
            "team, write the Project Charter (team structure, risk register, budget in "
            "Philippine Peso, milestones), and plan 10 sprints running from August to "
            "December 2026."
        ),
        "outcome": "Project Charter and sprint plan completed; development sprints ongoing.",
        "link": "",
    },
    {
        "title": "Philippine Spam/Scam SMS Clustering",
        "subtitle": "Mini data science project using K-Means",
        "role": "Co-author · screenshot documentation and slide presentation",
        "course": "CSIT 349 · Applied AI midterm",
        "tools": ["Python", "pandas", "scikit-learn", "K-Means", "Kaggle dataset"],
        "status": "In progress",
        "progress": 50,  
        "summary": (
            "Groups about 945 Philippine spam and scam text messages into clusters using "
            "features such as message length, word count, digit count, special "
            "characters, and URL presence, to see which scam styles are most common."
        ),
        "outcome": "Data preparation and planning done; clustering and analysis next.",
        "link": "",
    },
    {
        "title": "EduReach CRUD API",
        "subtitle": "Spring Boot CRUD built from the EduReach ERD",
        "role": "Backend developer",
        "course": "Application Development",
        "tools": ["Java", "Spring Boot", "REST", "ERD design"],
        "status": "Completed",
        "progress": 50,  
        "summary": (
            "EduReach models an online learning platform (User, Course, Enrollment, "
            "Module, Lesson, Assessment, Submission, and more). I picked one entity "
            "from the ERD and built full Create, Read, Update, Delete endpoints for it."
        ),
        "outcome": "Working CRUD for the chosen entity. Add your repo link below.",
        "link": "",
    },
]

# ----------------------------------------------------------------------------
# STYLING
# ----------------------------------------------------------------------------
st.markdown(
    """
    <style>
    .hero {
        padding: 1.6rem 1.8rem;
        border-radius: 16px;
        background: linear-gradient(135deg, #1e3a8a 0%, #6d28d9 100%);
        color: white;
        margin-bottom: 1rem;
    }
    .hero h1 { color: white; margin: 0 0 .2rem 0; font-size: 2.2rem; }
    .hero p  { color: #e0e7ff; margin: 0; font-size: 1.05rem; }
    .chip {
        display: inline-block; padding: 2px 10px; margin: 2px 4px 2px 0;
        border-radius: 999px; background: rgba(109,40,217,.12);
        border: 1px solid rgba(109,40,217,.35); font-size: .8rem;
    }
    .footer { text-align:center; opacity:.65; font-size:.85rem; margin-top:2rem; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ----------------------------------------------------------------------------
# SESSION STATE
# ----------------------------------------------------------------------------
if "visits" not in st.session_state:
    st.session_state.visits = 0
st.session_state.visits += 1
if "messages" not in st.session_state:
    st.session_state.messages = []
if "likes" not in st.session_state:
    st.session_state.likes = {p["title"]: 0 for p in PROJECTS}

# ----------------------------------------------------------------------------
# SIDEBAR
# ----------------------------------------------------------------------------
with st.sidebar:
    st.header("🧭 Quick Menu")
    if os.path.exists(PHOTO_PATH):
        st.image(PHOTO_PATH, width="stretch")
    else:
        st.image(
            f"https://placehold.co/400x400/6d28d9/ffffff?text={NICKNAME}",
            caption="Stand-in photo (replace with photo.jpg)",
            width="stretch",
        )
    st.markdown(f"**{NAME}**")
    st.caption(f"{PROGRAM} · {YEAR_LEVEL}")
    st.caption(SECTION)
    st.divider()

    theme_accent = st.selectbox(
        "Highlight color for charts",
        ["Violet", "Blue", "Green", "Orange"],
    )
    show_table = st.checkbox("Show raw skills table", value=True)
    detail_level = st.radio(
        "Project detail level",
        ["Short", "Full"],
        index=1,
        horizontal=True,
    )
    st.divider()
    st.link_button("GitHub", GITHUB, width="stretch")
    st.link_button("LinkedIn", LINKEDIN, width="stretch")
    st.caption(f"Page views this session: {st.session_state.visits}")

ACCENTS = {"Violet": "#6d28d9", "Blue": "#2563eb", "Green": "#16a34a", "Orange": "#ea580c"}
ACCENT = ACCENTS[theme_accent]

# ----------------------------------------------------------------------------
# HERO
# ----------------------------------------------------------------------------
st.markdown(
    f"""
    <div class="hero">
        <h1>👋 Hi, I'm {NICKNAME}</h1>
        <p>{TAGLINE}</p>
    </div>
    """,
    unsafe_allow_html=True,
)
st.caption(f"📌 {NAME} · {SECTION} · {SCHOOL}")

m1, m2, m3, m4 = st.columns(4)
m1.metric("Projects", len(PROJECTS))
m2.metric("Skills tracked", len(SKILLS))
m3.metric("Top skill", SKILLS.loc[SKILLS["Level"].idxmax(), "Skill"])
m4.metric("Average level", f"{SKILLS['Level'].mean():.0f}/100")

# ----------------------------------------------------------------------------
# TABS
# ----------------------------------------------------------------------------
tab_about, tab_story, tab_skills, tab_projects, tab_contact = st.tabs(
    ["🙋 About", "📖 Autobiography", "🛠️ Skills", "🚀 Projects", "✉️ Contact"]
)

# ---- ABOUT -----------------------------------------------------------------
with tab_about:
    left, right = st.columns([1, 2], gap="large")
    with left:
        if os.path.exists(PHOTO_PATH):
            st.image(PHOTO_PATH, width="stretch")
        else:
            st.image(
                f"https://placehold.co/500x500/1e3a8a/ffffff?text={NICKNAME}",
                caption="Stand-in photo. Add photo.jpg to replace it.",
                width="stretch",
            )
    with right:
        st.subheader(NAME)
        st.write(BIO)
        c1, c2 = st.columns(2)
        c1.info(f"🎓 **Program**\n\n{PROGRAM}")
        c2.info(f"🏫 **School**\n\n{SCHOOL}")
        c3, c4 = st.columns(2)
        c3.info(f"📅 **Year level**\n\n{YEAR_LEVEL}")
        c4.info(f"🧾 **Section**\n\n{SECTION}")

# ---- AUTOBIOGRAPHY ---------------------------------------------------------
with tab_story:
    st.header("My Story")
    col_a, col_b = st.columns(2, gap="large")
    items = list(AUTOBIOGRAPHY.items())
    for i, (heading, text) in enumerate(items):
        with (col_a if i % 2 == 0 else col_b):
            with st.container(border=True):
                st.subheader(heading)
                st.write(text)

    st.subheader("⏳ Milestones")
    st.dataframe(
        pd.DataFrame(MILESTONES),
        hide_index=True,
        width="stretch",
    )

    with st.expander("Fun facts about me"):
        st.markdown(
            "- likes to surf\n"
            "- beaches over mountains\n"
            "- build a web app for my capstone\n"
        )  

# ---- SKILLS ----------------------------------------------------------------
with tab_skills:
    st.header("Skills")
    st.write(
        "These are my self-ratings out of 100. Use the filter and the slider to "
        "explore them."
    )

    f1, f2 = st.columns([2, 1])
    categories = sorted(SKILLS["Category"].unique())
    chosen = f1.multiselect("Categories", categories, default=categories)
    min_level = f2.slider("Minimum level", 0, 100, 0, step=5)

    filtered = SKILLS[(SKILLS["Category"].isin(chosen)) & (SKILLS["Level"] >= min_level)]

    if filtered.empty:
        st.warning("No skills match those filters. Try lowering the minimum level.")
    else:
        chart_col, table_col = st.columns([3, 2], gap="large")
        with chart_col:
            st.subheader("Skill levels")
            st.bar_chart(
                filtered.set_index("Skill")["Level"],
                color=ACCENT,
                horizontal=True,
            )
        with table_col:
            if show_table:
                st.subheader("Table")
                st.dataframe(
                    filtered,
                    hide_index=True,
                    width="stretch",
                    column_config={
                        "Level": st.column_config.ProgressColumn(
                            "Level", min_value=0, max_value=100, format="%d"
                        ),
                        "Years": st.column_config.NumberColumn("Years", format="%d yr"),
                    },
                )
            else:
                st.caption("Table hidden. Turn it on from the sidebar.")

        st.subheader("Average level by category")
        by_cat = filtered.groupby("Category")["Level"].mean().round(1)
        st.line_chart(by_cat, color=ACCENT)

    st.download_button(
        "⬇️ Download my skills (CSV)",
        data=SKILLS.to_csv(index=False),
        file_name="jezer_skills.csv",
        mime="text/csv",
    )

# ---- PROJECTS --------------------------------------------------------------
with tab_projects:
    st.header("Projects")
    status_filter = st.selectbox("Show", ["All", "Completed", "In progress"])

    shown = [p for p in PROJECTS if status_filter in ("All", p["status"])]
    for p in shown:
        with st.container(border=True):
            top_l, top_r = st.columns([3, 1])
            top_l.subheader(f"{p['title']}")
            top_l.caption(f"{p['subtitle']} · {p['course']}")
            top_r.metric("Status", p["status"])

            st.write(f"**My role:** {p['role']}")
            st.markdown(
                "".join(f"<span class='chip'>{t}</span>" for t in p["tools"]),
                unsafe_allow_html=True,
            )
            st.progress(p["progress"], text=f"Progress: {p['progress']}%")

            if detail_level == "Full":
                st.write(p["summary"])
                st.success(f"**Outcome:** {p['outcome']}")

            b1, b2, _ = st.columns([1, 1, 3])
            if b1.button(f"👍 Like ({st.session_state.likes[p['title']]})", key=f"like_{p['title']}"):
                st.session_state.likes[p["title"]] += 1
                st.rerun()
            if p["link"]:
                b2.link_button("View project", p["link"])
            else:
                b2.button("No link yet", disabled=True, key=f"nolink_{p['title']}")

    if not shown:
        st.info("No projects match that filter.")

    st.subheader("Project timeline")
    timeline = pd.DataFrame(
        {
            "Sprint": [f"S{i}" for i in range(1, 11)],
            "Planned effort": [5, 8, 8, 10, 10, 9, 8, 7, 5, 4],  # EDIT
        }
    ).set_index("Sprint")
    st.area_chart(timeline, color=ACCENT)
    st.caption("Illustrative sprint effort for MarketLink. Replace with your real numbers.")

# ---- CONTACT ---------------------------------------------------------------
with tab_contact:
    st.header("Contact and Feedback")
    form_col, side_col = st.columns([2, 1], gap="large")

    with form_col:
        with st.form("contact_form", clear_on_submit=True):
            name = st.text_input("Your name")
            email = st.text_input("Your email")
            topic = st.selectbox("Topic", ["Feedback", "Collaboration", "Question", "Other"])
            rating = st.slider("How would you rate this site?", 1, 5, 4)
            message = st.text_area("Message", height=140)
            subscribe = st.checkbox("Send me a reply")
            submitted = st.form_submit_button("Send message")

        if submitted:
            if not name.strip() or not message.strip():
                st.error("Please enter at least your name and a message.")
            else:
                st.session_state.messages.append(
                    {
                        "time": datetime.now().strftime("%Y-%m-%d %H:%M"),
                        "name": name.strip(),
                        "topic": topic,
                        "rating": rating,
                    }
                )
                st.success(f"Thank you, {name.strip()}! Your {topic.lower()} was received.")
                st.balloons()
                if subscribe and not email.strip():
                    st.warning("You asked for a reply but did not leave an email.")

    with side_col:
        st.subheader("Find me")
        st.write(f"📧 {EMAIL}")
        st.write(f"💼 [LinkedIn]({LINKEDIN})")
        st.write(f"🐙 [GitHub]({GITHUB})")
        st.metric("Messages this session", len(st.session_state.messages))
        if st.session_state.messages:
            avg = np.mean([m["rating"] for m in st.session_state.messages])
            st.metric("Average site rating", f"{avg:.1f} / 5")

    if st.session_state.messages:
        with st.expander("Messages received this session"):
            st.dataframe(pd.DataFrame(st.session_state.messages), hide_index=True)

# ----------------------------------------------------------------------------
# FOOTER
# ----------------------------------------------------------------------------
st.markdown(
    f"<div class='footer'>Built with Streamlit · {NAME} · {SECTION}</div>",
    unsafe_allow_html=True,
)
