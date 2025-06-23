# writer_agent.py

from google.adk import Agent
from vertexai.generative_models import GenerativeModel

class WriterAgent(Agent):
    def execute(self, data: dict) -> str:
        topic = data.get("topic", "a default topic about technology")
        print(f"✍️ Writer Agent received topic: '{topic}'.")

        # <-- REVERTED: Using the user-specified model name that worked previously.
        model_name = "gemini-2.5-flash"
        model = GenerativeModel(model_name)
        
        prompt = (
            f"You are an expert content creator. "
            f"Write a compelling and informative 300-word blog post about '{topic}'. "
            f"The tone should be engaging and accessible for a general audience."
        )

        try:
            print(f"--> Calling model: {model_name}")
            response = model.generate_content(prompt)
            return response.text
        except Exception as e:
            print(f"❌ Writer Agent failed: {e}")
            return None