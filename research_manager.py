from crewai import Agent, LLM


def create_research_manager(llm: LLM, research_tool):

    return Agent(
        role="Research Manager",

        goal=(
            "Understand the user's research question, break it into "
            "clear research areas, and create a focused research plan "
            "for the research team."
        ),

        backstory=(
            "You are an experienced research director. "
            "You do not write the final report. "
            "You analyze the question, identify what must be investigated, "
            "and create a practical research plan for other specialists."
        ),

        llm=llm,

        tools=[research_tool],

        allow_delegation=False,

        verbose=True,
    )
