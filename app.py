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
            radial-gradient(circle at 10% 0%, rgba(59, 130, 246, 0.08), transparent 28%),
            radial-gradient(circle at 90% 10%, rgba(14, 165, 233, 0.07), transparent 25%),
            #f7f9fc;
        color: #172033;
    }

    .block-container {
        max-width: 1250px;
        padding-top: 2rem;
        padding-bottom: 4rem;
    }

    /* ---------- SIDEBAR ---------- */

    section[data-testid="stSidebar"] {
        background: #ffffff;
        border-right: 1px solid #e7ebf2;
    }

    section[data-testid="stSidebar"] .block-container {
        padding-top: 2rem;
    }

    /* ---------- HERO ---------- */

    .hero-wrapper {
        background: linear-gradient(
            135deg,
            #ffffff 0%,
            #f5f9ff 55%,
            #eef7ff 100%
        );
        border: 1px solid #e1eaf5;
        border-radius: 28px;
        padding: 48px 48px 42px 48px;
        margin-bottom: 28px;
        box-shadow: 0 15px 45px rgba(30, 64, 175, 0.08);
        position: relative;
        overflow: hidden;
    }

    .hero-wrapper::after {
        content: "";
        position: absolute;
        width: 280px;
        height: 280px;
        border-radius: 50%;
        background: rgba(59, 130, 246, 0.06);
        right: -80px;
        top: -100px;
    }

    .badge {
        display: inline-block;
        padding: 7px 14px;
        border-radius: 999px;
        background: #eaf3ff;
        color: #1769d1;
        border: 1px solid #cfe3ff;
        font-size: 12px;
        font-weight: 700;
        letter-spacing: 0.8px;
        margin-bottom: 18px;
    }

    .hero-title {
        font-size: 46px;
        line-height: 1.08;
        font-weight: 800;
        color: #10213f;
        margin-bottom: 15px;
        letter-spacing: -1.5px;
    }

    .hero-subtitle {
        max-width: 850px;
        font-size: 17px;
        line-height: 1.7;
        color: #5b6b82;
    }

    /* ---------- SECTION TITLES ---------- */

    .section-title {
        font-size: 25px;
        font-weight: 750;
        color: #17233b;
        margin-top: 30px;
        margin-bottom: 7px;
    }

    .section-subtitle {
        color: #718096;
        font-size: 15px;
        margin-bottom: 20px;
    }

    /* ---------- AGENT CARDS ---------- */

    .agent-card {
        background: #ffffff;
        border: 1px solid #e6ebf2;
        border-radius: 18px;
        padding: 20px;
        min-height: 150px;
        box-shadow: 0 7px 22px rgba(15, 23, 42, 0.045);
        transition: all 0.2s ease;
    }

    .agent-card:hover {
        transform: translateY(-2px);
        border-color: #c8dcf7;
        box-shadow: 0 12px 30px rgba(30, 64, 175, 0.09);
    }

    .agent-number {
        font-size: 12px;
        font-weight: 800;
        color: #3b82f6;
        letter-spacing: 1px;
        margin-bottom: 8px;
    }

    .agent-name {
        font-size: 18px;
        font-weight: 750;
        color: #17233b;
        margin-bottom: 8px;
    }

    .agent-description {
        font-size: 13px;
        line-height: 1.55;
        color: #6b778c;
    }

    /* ---------- INPUT ---------- */

    .question-label {
        font-size: 19px;
        font-weight: 700;
        color: #17233b;
        margin-top: 25px;
        margin-bottom: 10px;
    }

    textarea {
        border-radius: 14px !important;
    }

    /* ---------- STATUS ---------- */

    .status-box {
        background: #ffffff;
        border: 1px solid #e5eaf1;
        border-radius: 16px;
        padding: 18px 20px;
        margin-top: 18px;
        margin-bottom: 20px;
    }

    .status-title {
        font-size: 14px;
        font-weight: 750;
        color: #263650;
        margin-bottom: 8px;
    }

    .status-text {
        font-size: 13px;
        color: #718096;
    }

    /* ---------- RESULT ---------- */

    .result-header {
        background: linear-gradient(135deg, #10213f, #174a85);
        color: white;
        padding: 24px 28px;
        border-radius: 18px 18px 0 0;
        margin-top: 25px;
    }

    .result-header-title {
        font-size: 23px;
        font-weight: 750;
    }

    .result-header-subtitle {
        font-size: 13px;
        opacity: 0.8;
        margin-top: 5px;
    }

    /* ---------- BUTTON ---------- */

    .stButton > button {
        border-radius: 12px;
        border: none;
        background: linear-gradient(135deg, #1769d1, #2789ed);
        color: white;
        font-weight: 700;
        padding: 0.65rem 1.3rem;
        min-height: 48px;
        box-shadow: 0 7px 18px rgba(37, 99, 235, 0.20);
    }

    .stButton > button:hover {
        background: linear-gradient(135deg, #1259b4, #1878d7);
        color: white;
    }

    /* ---------- FOOTER ---------- */

    .footer {
        text-align: center;
        color: #8a96a8;
        font-size: 12px;
        margin-top: 55px;
        padding-top: 20px;
        border-top: 1px solid #e7ebf2;
    }

    /* ---------- MOBILE ---------- */

    @media (max-width: 768px) {

        .block-container {
            padding-left: 1rem;
            padding-right: 1rem;
        }

        .hero-wrapper {
            padding: 32px 24px;
            border-radius: 22px;
        }

        .hero-title {
            font-size: 34px;
        }

        .hero-subtitle {
            font-size: 15px;
        }

    }

    </style>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        """
        <div style="
            font-size:26px;
            font-weight:800;
            color:#10213f;
            margin-bottom:4px;
        ">
            🔬 Research Lab
        </div>

        <div style="
            color:#718096;
            font-size:13px;
            line-height:1.5;
            margin-bottom:25px;
        ">
            A specialized multi-agent research team powered by AI.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div style="
            font-size:13px;
            font-weight:700;
            color:#34445d;
            margin-bottom:12px;
        ">
            YOUR AI RESEARCH TEAM
        </div>
        """,
        unsafe_allow_html=True,
    )

    sidebar_agents = [
        ("01", "Research Manager", "Breaks the question into research tasks."),
        ("02", "Web Researcher", "Finds current web information."),
        ("03", "Academic Researcher", "Investigates papers and evidence."),
        ("04", "Industry Researcher", "Studies real-world applications."),
        ("05", "Research Synthesizer", "Combines findings into one report."),
    ]

    for number, name, description in sidebar_agents:

        st.markdown(
            f"""
            <div style="
                padding:12px;
                margin-bottom:9px;
                background:#f8fafc;
                border:1px solid #e7edf5;
                border-radius:12px;
            ">
                <div style="
                    font-size:10px;
                    font-weight:800;
                    color:#3b82f6;
                    margin-bottom:3px;
                ">
                    AGENT {number}
                </div>

                <div style="
                    font-size:13px;
                    font-weight:700;
                    color:#263650;
                ">
                    {name}
                </div>

                <div style="
                    font-size:11px;
                    color:#7a8799;
                    margin-top:3px;
                    line-height:1.4;
                ">
                    {description}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown(
        """
        <div style="
            margin-top:25px;
            padding:14px;
            background:#eef7ff;
            border:1px solid #d7eaff;
            border-radius:12px;
            font-size:12px;
            color:#42617f;
            line-height:1.5;
        ">
            <b>How it works</b><br><br>
            Your question is passed through multiple specialized agents.
            Each agent researches a different aspect before the final
            report is created.
        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# HERO
# ============================================================

st.markdown(
    """
    <div class="hero-wrapper">

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
# AGENT TEAM
# ============================================================

st.markdown(
    """
    <div class="section-title">
        Meet Your Research Team
    </div>

    <div class="section-subtitle">
        Each agent has a specialized responsibility in the research workflow.
    </div>
    """,
    unsafe_allow_html=True,
)

agents = [
    (
        "01",
        "Research Manager",
        "Understands your question and creates a focused research plan.",
    ),
    (
        "02",
        "Web Researcher",
        "Searches the live web for current and relevant information.",
    ),
    (
        "03",
        "Academic Researcher",
        "Looks for academic evidence, scientific studies, and papers.",
    ),
    (
        "04",
        "Industry Researcher",
        "Investigates companies, products, trends, and real-world use.",
    ),
    (
        "05",
        "Research Synthesizer",
        "Combines the findings into a clear and structured report.",
    ),
]

columns = st.columns(5)

for column, agent in zip(columns, agents):

    number, name, description = agent

    with column:

        st.markdown(
            f"""
            <div class="agent-card">

                <div class="agent-number">
                    AGENT {number}
                </div>

                <div class="agent-name">
                    {name}
                </div>

                <div class="agent-description">
                    {description}
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )


# ============================================================
# QUESTION INPUT
# ============================================================

st.markdown(
    """
    <div class="question-label">
        What would you like to research?
    </div>
    """,
    unsafe_allow_html=True,
)

question = st.text_area(
    label="Research Question",
    placeholder=(
        "Example: How is generative AI changing software engineering "
        "jobs, and what skills will become important over the next 5 years?"
    ),
    height=150,
    label_visibility="collapsed",
)


# ============================================================
# START BUTTON
# ============================================================

start_research = st.button(
    "🚀 Start Multi-Agent Research",
    use_container_width=True,
)


# ============================================================
# RUN RESEARCH
# ============================================================

if start_research:

    if not question.strip():

        st.warning("Please enter a research question first.")

    else:

        # ----------------------------------------------------
        # STATUS AREA
        # ----------------------------------------------------

        st.markdown(
            """
            <div class="status-box">
                <div class="status-title">
                    🔄 Research team is working
                </div>

                <div class="status-text">
                    Your question is being analyzed by the multi-agent system.
                    This may take a little while while the agents research
                    different sources.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        progress = st.progress(0)

        status = st.empty()

        status.info("🧠 Research Manager is creating the research plan...")
        progress.progress(15)

        try:

            status.info("🌐 Web Researcher is investigating current information...")
            progress.progress(30)

            status.info("🎓 Academic Researcher is examining research evidence...")
            progress.progress(50)

            status.info("🏢 Industry Researcher is investigating real-world applications...")
            progress.progress(70)

            result = run_research(question)

            status.info("🧩 Research Synthesizer is preparing the final report...")
            progress.progress(90)

            progress.progress(100)

            status.success("✅ Research completed successfully.")

            # ------------------------------------------------
            # RESULT
            # ------------------------------------------------

            st.markdown(
                """
                <div class="result-header">

                    <div class="result-header-title">
                        📊 Research Report
                    </div>

                    <div class="result-header-subtitle">
                        Synthesized from the work of the multi-agent research team
                    </div>

                </div>
                """,
                unsafe_allow_html=True,
            )

            st.markdown(result)

            # ------------------------------------------------
            # DOWNLOAD
            # ------------------------------------------------

            st.download_button(
                label="⬇️ Download Research Report",
                data=result,
                file_name="research_report.md",
                mime="text/markdown",
                use_container_width=True,
            )

        except Exception as e:

            progress.empty()

            status.error("❌ Research failed.")

            st.error(
                f"Something went wrong while running the research team:\n\n{e}"
            )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">
        Research Intelligence Lab · Multi-Agent AI Research System
    </div>
    """,
    unsafe_allow_html=True,
)
