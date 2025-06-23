# orchestrator_agent.py

from google.adk import Agent, AgentRuntime
from writer_agent import WriterAgent
from visual_agent import VisualCreatorAgent

class OrchestratorAgent(Agent):
    """
    Manages the entire content creation workflow by calling other agents.
    """
    def execute(self, state: dict) -> dict:
        """
        Executes the writer and visual creator agents in sequence.
        """
        print("🚀 Orchestrator starting workflow...")
        
        # Step 1: Run the Writer Agent
        print("Orchestrator: Calling Writer Agent...")
        # We pass the whole state dictionary to the agent
        article_text = AgentRuntime.execute(WriterAgent, state=state)
        
        if not article_text:
            state['error'] = "Writer Agent failed to produce text."
            print(f"❌ Orchestrator HALTED: {state['error']}")
            return state

        # Add the result to the state for the next agents to use
        state['article_text'] = article_text
        print("Orchestrator: Writer Agent successful.")

        # Step 2: Run the Visual Creator Agent
        print("Orchestrator: Calling Visual Creator Agent...")
        # It also receives the full state, so it can access the original topic
        image_bytes = AgentRuntime.execute(VisualCreatorAgent, state=state)

        if not image_bytes:
            state['error'] = "Visual Creator Agent failed to produce an image."
            print(f"❌ Orchestrator HALTED: {state['error']}")
            return state

        # Add the result to the state
        state['image_bytes'] = image_bytes
        print("Orchestrator: Visual Creator Agent successful.")
        
        print("✅ Orchestrator: Workflow complete.")
        return state