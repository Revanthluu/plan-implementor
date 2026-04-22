from crewai import Task

class WorkflowTasks:
    def research_tools_task(self, agent, use_case):
        return Task(
            description=(
                f"Analyze the following user use-case: '{use_case}'.\n"
                "You need to research and identify the best AI tools, APIs, and frameworks "
                "to effectively build this project.\n"
                "Break down the needs (e.g. LLM, vector database, agent framework, frontend) "
                "and select the optimal tech stack."
            ),
            expected_output=(
                "A structured markdown list containing:\n"
                "1. Tool Name\n"
                "2. Purpose (What it does)\n"
                "3. Why it is recommended for this specific use-case"
            ),
            agent=agent
        )

    def design_workflow_task(self, agent, use_case):
        return Task(
            description=(
                f"Based on the required use-case '{use_case}' and the tools recommended by the researcher in the previous step, "
                "design a comprehensive step-by-step implementation workflow.\n"
                "The workflow should guide a developer from zero to a fully working prototype."
            ),
            expected_output=(
                "A clear, structured step-by-step execution plan in markdown.\n"
                "Each step must include:\n"
                "- Step Title\n"
                "- Actionable instructions\n"
                "- Tools to be used in that step\n"
                "Finish with a final execution summary."
            ),
            agent=agent
        )

    def pricing_impact_task(self, agent, use_case):
        return Task(
            description=(
                f"Based on the use-case '{use_case}' and the generated workflow, provide a deep architectural "
                "tech flow overview, foundational model recommendations, and financial cost estimates."
            ),
            expected_output=(
                "A structured markdown section detailing:\n"
                "1. **Suggested Tech Flow**: A sequential explanation of how data travels through the system.\n"
                "2. **Recommended AI Models**: Specific model choices (e.g., Gemini 1.5, GPT-4o, Llama 3) focusing on speed vs quality.\n"
                "3. **Estimated Pricing**: Token-based cost evaluation or hosting estimates.\n"
                "4. **Business Impact**: How this specific workflow scales and potential blockers."
            ),
            agent=agent
        )
