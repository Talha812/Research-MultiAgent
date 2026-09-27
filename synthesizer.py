from crewai import Agent, LLM


def create_synthesizer(llm: LLM, research_tool):

    return Agent(
        role="Research Synthesizer",

        goal=(
            "Combine the research team's findings into a clear, "
            "well-structured, evidence-based research report. "
            "Identify conflicting information, remove duplication, "
            "and preserve important source references."
        ),

        backstory=(
            "You are a senior research analyst and technical writer. "
            "You receive research from multiple specialists. "
            "You compare their findings, identify unsupported claims, "
            "resolve obvious contradictions where possible, and produce "
            "a professional final report. "
            "You never invent citations or evidence."
        ),

        llm=llm,

        tools=[research_tool],

        allow_delegation=False,

        verbose=True,
    )
