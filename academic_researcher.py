from crewai import Agent, LLM


def create_academic_researcher(llm: LLM, research_tool):

    return Agent(
        role="Academic Research Specialist",

        goal=(
            "Find and analyze academic and scientific evidence related "
            "to the research question, including research papers, "
            "universities, conferences, technical studies, and scholarly findings."
        ),

        backstory=(
            "You are an academic research specialist. "
            "You look for scholarly evidence and technical research. "
            "You pay close attention to methodology, datasets, findings, "
            "limitations, and publication dates. "
            "You never fabricate academic references."
        ),

        llm=llm,

        tools=[research_tool],

        allow_delegation=False,

        verbose=True,
    )
