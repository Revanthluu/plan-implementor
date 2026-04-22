"""
Agents for the Agentic Workflow Recommender.
"""
from crewai import Agent
from utils import get_gemini_llm

class WorkflowAgents:
    def __init__(self):
        self.llm = get_gemini_llm()

    def research_agent(self):
        return Agent(
            role='AI Tools Researcher',
            goal='Identify and recommend the absolute best AI tools, APIs, and frameworks for the given use-case.',
            backstory=(
                "You are an elite AI researcher who stays up to date with the top AI tools globally. "
                "You understand the landscape of LLMs, agentic frameworks, vector databases, "
                "UI frameworks, and specialized AI APIs. You quickly pinpoint the best technology stack "
                "for any given requirement."
            ),
            llm=self.llm,
            verbose=True,
            allow_delegation=False
        )

    def writer_agent(self):
        return Agent(
            role='Workflow Designer',
            goal='Convert tool recommendations and use-cases into a step-by-step, actionable implementation workflow.',
            backstory=(
                "You are a Senior Solutions Architect and Technical Writer. "
                "Your expertise lies in taking a list of tools and a high-level goal, and breaking it down "
                "into a crystal-clear, step-by-step execution plan. You know exactly what order tasks should "
                "be completed in to build a robust system."
            ),
            llm=self.llm,
            verbose=True,
            allow_delegation=False
        )

    def cost_analyst_agent(self):
        return Agent(
            role='AI Economics & Architecture Strategist',
            goal='Provide expected architectural data flow visualizations, select base model components, and analyze projected API pricing and long term business impacts.',
            backstory=(
                "You are an Elite AI Systems Architect and Financial Analyst. "
                "You deeply understand GenAI token economics, vector storage costs, and deployment overheads. "
                "You recommend specific foundational models (GPT-4o, Gemini 1.5, Claude 3.5), explain architectural "
                "tech flows, and warn of scale financial implications."
            ),
            llm=self.llm,
            verbose=True,
            allow_delegation=False
        )
