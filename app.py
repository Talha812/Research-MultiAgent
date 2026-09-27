import streamlit as st

from crew import run_research


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Research Intelligence Lab",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    /* ---------- GLOBAL ---------- */

    .stApp {
        background:
            radial-gradient(
                circle at 15% 10%,
                rgba(37, 99, 235, 0.08),
                transparent 30%
            ),
            radial-gradient(
                circle at 85% 15%,
                rgba(14, 165, 233, 0.08),
                transparent 30%
            ),
            #f8fafc;
    }

    .main .block-container {
        max-width: 1250px;
        padding-top: 2rem;
        padding-bottom: 4rem;
    }


    /* ---------- HEADER ---------- */

    .hero {
        background: linear-gradient(
            135deg,
            #ffffff 0%,
            #f0f7ff 100%
        );

        border: 1px solid #dbeafe;
        border-radius: 24px;

        padding: 34px 38px;

        margin-bottom: 24px;

        box-shadow:
            0 12px 35px rgba(15, 23, 42, 0.07);
    }

    .hero-title {
        font-size: 42px;
        font-weight: 800;
        letter-spacing: -1.5px;
        color: #0f172a;
        margin-bottom: 8px;
    }

    .hero-subtitle {
        font-size: 17px;
        line-height: 1.6;
        color: #64748b;
        max-width: 800px;
    }

    .badge {
        display: inline-block;

        background: #dbeafe;
        color: #1d4ed8;

        border-radius: 999px;

        padding: 6px 13px;

        font-size: 13px;
        font-weight: 700;

        margin-bottom: 14px;
    }


    /* ---------- AGENT CARDS ---------- */

    .agent-card {
        background: white;

        border: 1px solid #e2e8f0;

        border-radius: 18px;

        padding: 17px;

        min-height: 118px;

        box-shadow:
            0 5px 18px rgba(15, 23, 42, 0.045);
    }

    .agent-active {
        border: 2px solid #2563eb;

        background:
            linear-gradient(
                135deg,
                #eff6ff,
                #ffffff
            );

        box-shadow:
            0 8px 28px rgba(37, 99, 235, 0.14);
    }

    .agent-done {
        border-color: #bbf7d0;
        background: #f0fdf4;
    }

    .agent-icon {
        font-size: 25px;
        margin-bottom: 8px;
    }

    .agent-name {
        font-size: 15px;
        font-weight: 750;
        color: #0f172a;
    }

    .agent-status {
        font-size: 12px;
        margin-top: 6px;
        color: #64748b;
    }


    /* ---------- CURRENT AGENT ---------- */

    .working-box {
        background: linear-gradient(
            135deg,
            #1d4ed8,
            #2563eb
        );

        border-radius: 18px;

        padding: 18px 22px;

        color: white;

        margin: 20px 0;

        box-shadow:
            0 10px 28px rgba(37, 99, 235, 0.22);
    }

    .working-label {
        font-size: 12px;
        opacity: 0.8;
        text-transform: uppercase;
        letter-spacing: 1px;
        font-weight: 700;
    }

    .working-agent {
        font-size: 23px;
        font-weight: 800;
        margin-top: 3px;
    }


    /* ---------- REPORT ---------- */

    .report-header {
        margin-top: 30px;
        margin-bottom: 12px;
    }


    /* ---------- SIDEBAR ---------- */

    [data-testid="stSidebar"] {
        background: #ffffff;

        border-right: 1px solid #e2e8f0;
    }

    .sidebar-title {
        font-size: 21px;
        font-weight: 800;
        color: #0f172a;
    }

    .sidebar-text {
        color: #64748b;
        font-size: 13px;
        line-height: 1.6;
    }


    /* ---------- BUTTON ---------- */

    .stButton > button {
        border-radius: 12px;

        min-height: 48px;

        font-weight: 700;

        border: none;

        background: #2563eb;

        color: white;

        box-shadow:
            0 6px 18px rgba(37, 99, 235, 0.18);
    }

    .stButton > button:hover {
        background: #1d4ed8;
        border: none;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# SESSION STATE
# ============================================================

if "research_started" not in st.session_state:
    st.session_state.research_started = False

if "report" not in st.session_state:
    st.session_state.report = None


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        '<div class="sidebar-title">🔬 Research Lab</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="sidebar-text">
        A multi-agent research team powered by CrewAI
        and Groq GPT-OSS 120B.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.divider()

    st.markdown("### Research Team")

    st.markdown("🧭 **Research Manager**")
    st.caption("Plans the investigation")

    st.markdown("🌐 **Web Researcher**")
    st.caption("Finds current web evidence")

    st.markdown("🎓 **Academic Researcher**")
    st.caption("Investigates scholarly evidence")

    st.markdown("🏢 **Industry Researcher**")
    st.caption("Investigates real-world applications")

    st.markdown("✍️ **Research Synthesizer**")
    st.caption("Combines and verifies findings")

    st.divider()

    st.caption("Model")
    st.code("GPT-OSS 120B", language=None)

    st.caption("Framework")
    st.code("CrewAI", language=None)

    st.caption("Research Tool")
    st.code("Groq Browser Search", language=None)


# ============================================================
# HERO
# ============================================================

st.markdown(
    """
    <div class="hero">

        <div class="badge">
            MULTI-AGENT RESEARCH SYSTEM
        </div>

        <div class="hero-title">
            Research Intelligence Lab
        </div>

        <div class="hero-subtitle">
            Ask a research question and let a specialized AI team
            investigate the web, academic evidence, industry activity,
            and synthesize everything into one structured report.
        </div>

    </div>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# RESEARCH INPUT
# ============================================================

st.markdown("### What should the research team investigate?")

question = st.text_area(
    label="Research question",
    placeholder=(
        "Example: What are the latest approaches to Retrieval-Augmented "
        "Generation and how are companies using them?"
    ),
    height=130,
    label_visibility="collapsed",
)


# ============================================================
# AGENT DISPLAY
# ============================================================

st.markdown("### Research Team")

agent_data = [
    ("🧭", "Research Manager", "Planning"),
    ("🌐", "Web Researcher", "Web evidence"),
    ("🎓", "Academic Researcher", "Academic evidence"),
    ("🏢", "Industry Researcher", "Industry evidence"),
    ("✍️", "Research Synthesizer", "Final report"),
]

cols = st.columns(5)

for col, (icon, name, description) in zip(cols, agent_data):

    with col:

        st.markdown(
            f"""
            <div class="agent-card">

                <div class="agent-icon">{icon}</div>

                <div class="agent-name">
                    {name}
                </div>

                <div class="agent-status">
                    {description}
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )


# ============================================================
# START
# ============================================================

st.write("")

start = st.button(
    "🚀  Start Research",
    use_container_width=True,
    type="primary",
)


# ============================================================
# RUN CREW
# ============================================================

if start:

    if not question.strip():

        st.warning(
            "Please enter a research question first."
        )

    else:

        st.session_state.research_started = True

        st.markdown(
            """
            <div class="working-box">

                <div class="working-label">
                    CURRENTLY WORKING
                </div>

                <div class="working-agent">
                    🧠 Research team is investigating your question...
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

        progress = st.progress(0)

        status = st.empty()

        try:

            status.info(
                "🧭 Research Manager is planning the investigation..."
            )

            progress.progress(10)

            status.info(
                "🌐 Web Researcher is gathering current web evidence..."
            )

            progress.progress(30)

            status.info(
                "🎓 Academic Researcher is investigating scholarly evidence..."
            )

            progress.progress(50)

            status.info(
                "🏢 Industry Researcher is investigating real-world applications..."
            )

            progress.progress(70)

            status.info(
                "✍️ Research Synthesizer is verifying and writing the report..."
            )

            progress.progress(85)

            result = run_research(question)

            progress.progress(100)

            status.success(
                "✅ Research completed successfully."
            )

            st.session_state.report = str(result)

        except Exception as e:

            progress.empty()

            status.error(
                "Research failed. Please check the error below."
            )

            st.exception(e)


# ============================================================
# FINAL REPORT
# ============================================================

if st.session_state.report:

    st.markdown(
        '<div class="report-header"><h2>📑 Research Report</h2></div>',
        unsafe_allow_html=True,
    )

    st.markdown(st.session_state.report)

    st.download_button(
        label="⬇️ Download Report",
        data=st.session_state.report,
        file_name="research_report.md",
        mime="text/markdown",
        use_container_width=True,
    )
