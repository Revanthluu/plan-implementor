from crewai import Crew, Process
from agents import WorkflowAgents
from tasks import WorkflowTasks

class WorkflowCrew:
    def __init__(self, use_case: str):
        self.use_case = use_case

    def run(self):
        agents = WorkflowAgents()
        tasks = WorkflowTasks()

        # Initialize agents
        researcher = agents.research_agent()
        writer = agents.writer_agent()
        analyst = agents.cost_analyst_agent()

        # Initialize tasks
        research_task = tasks.research_tools_task(researcher, self.use_case)
        design_task = tasks.design_workflow_task(writer, self.use_case)
        pricing_task = tasks.pricing_impact_task(analyst, self.use_case)

        # Setup Crew with an explicit max_rpm to prevent Google API exhaustion
        crew = Crew(
            agents=[researcher, writer, analyst],
            tasks=[research_task, design_task, pricing_task],
            process=Process.sequential,
            verbose=True,
            max_rpm=10
        )

        result = crew.kickoff()
        
        # CrewAI returns a CrewOutput object in newer versions, or a string in older ones.
        # We will safely return its string representation
        return str(result)
