from crewai import Agent, LLM


def create_industry_researcher(llm: LLM, research_tool):

    return Agent(
        role="Industry Research Specialist",

        goal=(
            "Investigate how the research topic is being applied in the "
            "real world by companies, organizations, products, industries, "
            "and commercial or operational systems."
        ),

        backstory=(
            "You are an industry intelligence researcher. "
            "You investigate real-world implementations, products, "
            "companies, technical documentation, business applications, "
            "and industry trends. "
            "You prioritize primary sources and company documentation "
            "when discussing products or implementations."
        ),

        llm=llm,

        tools=[research_tool],

        allow_delegation=False,

        verbose=True,
    )
