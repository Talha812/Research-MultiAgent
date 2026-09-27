import os

from crewai import Crew, LLM, Process, Task
from crewai.tools import tool

from research_manager import create_research_manager
from web_researcher import create_web_researcher
from academic_researcher import create_academic_researcher
from industry_researcher import create_industry_researcher
from synthesizer import create_synthesizer

from tools import web_search


MODEL_NAME = "groq/openai/gpt-oss-120b"


def create_llm():

    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError("GROQ_API_KEY is missing.")

    return LLM(
        model=MODEL_NAME,
        api_key=api_key,
        temperature=0.2,
    )


@tool("Web Research Tool")
def research_web(query: str) -> str:
    """
    Search the live internet for current research information.
    Use this tool whenever current web information is required.
    """
    return web_search(query)


def run_research(question: str):

    llm = create_llm()

    # ---------------------------------------------------------
    # AGENTS
    # ---------------------------------------------------------

    manager = create_research_manager(
        llm,
        research_web
    )

    web_researcher = create_web_researcher(
        llm,
        research_web
    )

    academic_researcher = create_academic_researcher(
        llm,
        research_web
    )

    industry_researcher = create_industry_researcher(
        llm,
        research_web
    )

    synthesizer = create_synthesizer(
        llm,
        research_web
    )

    # ---------------------------------------------------------
    # TASK 1 - RESEARCH PLAN
    # ---------------------------------------------------------

    planning_task = Task(
        description=f"""
        Analyze this research question:

        {question}

        Create a research plan for the team.

        Identify:
        1. Main research question
        2. Important subtopics
        3. Key facts that must be investigated
        4. Academic evidence needed
        5. Industry evidence needed
        6. Important current developments

        Do not write the final report.
        """,

        expected_output=(
            "A structured research plan containing the main question, "
            "research areas, and evidence requirements."
        ),

        agent=manager,
    )

    # ---------------------------------------------------------
    # TASK 2 - WEB RESEARCH
    # ---------------------------------------------------------

    web_task = Task(
        description=f"""
        Research the following question using the research plan
        produced by the Research Manager:

        {question}

        Investigate:
        - Current information
        - Recent developments
        - Important organizations
        - Technologies
        - Statistics where available
        - Reliable web sources

        Use the Web Research Tool.

        Return factual findings with source names and URLs.
        """,

        expected_output=(
            "Detailed web research findings with source references."
        ),

        agent=web_researcher,

        context=[planning_task],
    )

    # ---------------------------------------------------------
    # TASK 3 - ACADEMIC RESEARCH
    # ---------------------------------------------------------

    academic_task = Task(
        description=f"""
        Investigate the academic and scientific evidence related to:

        {question}

        Focus on:
        - Research papers
        - Universities
        - Conferences
        - Scientific studies
        - Methodologies
        - Experimental findings
        - Limitations
        - Recent academic developments

        Use the Web Research Tool.

        Return findings with academic source names, paper titles,
        publication information, and URLs when available.
        """,

        expected_output=(
            "Academic research findings with scholarly source references."
        ),

        agent=academic_researcher,

        context=[planning_task],
    )

    # ---------------------------------------------------------
    # TASK 4 - INDUSTRY RESEARCH
    # ---------------------------------------------------------

    industry_task = Task(
        description=f"""
        Investigate real-world and industry applications related to:

        {question}

        Focus on:
        - Companies
        - Products
        - Commercial implementations
        - Industry adoption
        - Business applications
        - Technical implementations
        - Current industry trends

        Use the Web Research Tool.

        Return factual findings with source names and URLs.
        """,

        expected_output=(
            "Industry research findings with source references."
        ),

        agent=industry_researcher,

        context=[planning_task],
    )

    # ---------------------------------------------------------
    # TASK 5 - FINAL SYNTHESIS
    # ---------------------------------------------------------

    synthesis_task = Task(
        description=f"""
        Produce the final research report for:

        {question}

        Combine the findings from:

        1. Research Manager
        2. Web Researcher
        3. Academic Researcher
        4. Industry Researcher

        The report should contain:

        # Executive Summary

        # Introduction

        # Key Findings

        # Academic Evidence

        # Industry Applications

        # Current Developments

        # Challenges and Limitations

        # Future Directions

        # Conclusion

        # Sources

        Important rules:

        - Do not invent facts.
        - Do not invent citations.
        - Do not claim something is current unless the research supports it.
        - Clearly distinguish documented facts from interpretations.
        - Remove duplicate information.
        - Preserve useful source URLs.
        - If researchers disagree, mention the disagreement.
        - Write in professional but easy-to-understand language.

        Before finalizing, use the Web Research Tool to verify
        important or potentially outdated claims.
        """,

        expected_output=(
            "A complete evidence-based research report with source references."
        ),

        agent=synthesizer,

        context=[
            planning_task,
            web_task,
            academic_task,
            industry_task,
        ],
    )

    # ---------------------------------------------------------
    # CREW
    # ---------------------------------------------------------

    crew = Crew(
        agents=[
            manager,
            web_researcher,
            academic_researcher,
            industry_researcher,
            synthesizer,
        ],

        tasks=[
            planning_task,
            web_task,
            academic_task,
            industry_task,
            synthesis_task,
        ],

        process=Process.sequential,

        verbose=True,
    )

    return crew.kickoff()
