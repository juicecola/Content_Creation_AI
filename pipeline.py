# pipeline.py

import os
import json
import vertexai
from io import BytesIO

# --- Import All Agent Classes ---
from writer_agent import WriterAgent
from visual_agent import VisualCreatorAgent
from social_agent import SocialAgent

# --- CONFIGURATION ---
# It's better to configure this once when the app starts
GCP_PROJECT_ID = "adk-hackathon-project"  # Or your actual project ID
GCP_LOCATION = "us-central1"

# --- INITIALIZE VERTEX AI ---
# This should be called only once. We'll handle this in the Streamlit app.
def initialize_vertexai():
    try:
        # Using Application Default Credentials (ADC) is better than key files
        vertexai.init(project=GCP_PROJECT_ID, location=GCP_LOCATION)
        print("✅ Vertex AI Initialized")
        return True
    except Exception as e:
        print(f"❌ Vertex AI Initialization failed: {e}")
        return False

# This is our main, reusable function!
def run_content_pipeline(topic: str):
    """
    Executes the full content creation pipeline for a given topic.

    Args:
        topic: The subject for content creation.

    Returns:
        A tuple containing: (article_text, image_bytes, social_posts_json)
    """
    
    # --- STEP 1: RUN WRITER AGENT ---
    print("\n--- STEP 1: Running Writer Agent ---")
    writer_agent = WriterAgent(name="writer_agent")
    article_text = writer_agent.execute({"topic": topic})
    
    if not article_text:
        print("❌ Writer Agent failed. Halting workflow.")
        return None, None, None
    
    print(f"✅ Article generated successfully.")

    # --- STEP 2: RUN VISUAL AGENT ---
    print("--- STEP 2: Running Visual Creator Agent ---")
    visual_agent = VisualCreatorAgent(name="visual_agent")
    image_bytes = visual_agent.execute({"topic": topic})
    
    if not image_bytes:
        print("❌ Visual Agent failed.")
        # We can still return the article even if the image fails
        return article_text, None, None
        
    print(f"✅ Image generated successfully.")

    # --- STEP 3: RUN SOCIAL AGENT ---
    print("\n--- STEP 3: Running Social Media Agent ---")
    social_agent = SocialAgent(name="social_agent")
    social_posts = social_agent.execute({"article_text": article_text})

    if not social_posts:
        print("❌ Social Agent failed.")
        return article_text, image_bytes, None
        
    print(f"✅ Social posts generated successfully.")

    return article_text, image_bytes, social_posts
