from crewai import Agent, LLM


def create_web_researcher(llm: LLM, research_tool):

    return Agent(
        role="Web Research Specialist",

        goal=(
            "Investigate the research topic using current web sources "
            "and collect reliable facts, statistics, developments, "
            "organizations, technologies, and relevant evidence."
        ),

        backstory=(
            "You are a professional web researcher. "
            "You investigate topics using current online information. "
            "You prefer official documentation, reputable organizations, "
            "universities, established publications, and primary sources. "
            "You clearly distinguish facts from opinions."
        ),

        llm=llm,

        tools=[research_tool],

        allow_delegation=False,

        verbose=True,
    )
