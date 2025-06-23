# social_agent.py

import json
from google.adk import Agent
from vertexai.generative_models import GenerativeModel

class SocialAgent(Agent):
    def execute(self, data: dict) -> dict:
        article_text = data.get('article_text', '')
        if not article_text:
            return None
        
        print(f"📱 Social Agent is processing the article...")

        # <-- REVERTED: Using the user-specified model name that worked previously.
        model_name = "gemini-2.5-flash"
        model = GenerativeModel(model_name)
        
        prompt = f"""
        Analyze the following blog post. Your task is to generate social media content.
        Your output MUST be a single, valid JSON object with two keys: "tweet" and "linkedin_post".
        Blog Post: --- {article_text} ---
        """
        try:
            print(f"--> Calling model: {model_name}")
            response = model.generate_content(prompt)
            cleaned_response = response.text.strip().replace("```json", "").replace("```", "")
            return json.loads(cleaned_response)
        except Exception as e:
            print(f"❌ Social Agent failed: {e}")
            return None