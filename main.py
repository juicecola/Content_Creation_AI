# main.py

import os
import sys
import json
import vertexai

# --- Import All Agent Classes ---
from writer_agent import WriterAgent
from visual_agent import VisualCreatorAgent
from social_agent import SocialAgent

# ==============================================================================
#  ⚠️ START: THE CRITICAL ENVIRONMENT FIX ⚠️
# ==============================================================================
current_dir = os.path.dirname(os.path.abspath(__file__))
adk_path = os.path.join(current_dir, 'agent-development-kit', 'adk-python', 'src')
sys.path.insert(0, adk_path)
# ==============================================================================

# --- CONFIGURATION ---
GCP_PROJECT_ID = "adk-hackathon-project"
GCP_LOCATION = "us-central1"
CREDENTIALS_PATH = "google_credentials.json"
hackathon_topic = "The Impact of onlyfans on content creation"

# --- INITIALIZE VERTEX AI ---
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = CREDENTIALS_PATH
try:
    vertexai.init(project=GCP_PROJECT_ID, location=GCP_LOCATION)
    print("✅ Vertex AI Initialized")
except Exception as e:
    print(f"❌ Vertex AI Initialization failed: {e}")
    exit()

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    print(f"\n--- Starting workflow for topic: '{hackathon_topic}' ---")
    
    # --- STEP 1: RUN WRITER AGENT ---
    print("\n--- STEP 1: Running Writer Agent ---")
    writer_agent = WriterAgent(name="writer_agent")
    article_text = writer_agent.execute({"topic": hackathon_topic})
    
    if article_text:
        print("\n--- ARTICLE GENERATED ---")
        print(article_text[:400] + "...\n")
        
        # --- STEP 2: RUN VISUAL AGENT ---
        print("--- STEP 2: Running Visual Creator Agent ---")
        visual_agent = VisualCreatorAgent(name="visual_agent")
        
        # <<< THIS IS THE CORRECTED LINE >>>
        # We now send a dictionary with the key 'topic', which the agent expects.
        image_bytes = visual_agent.execute({"topic": hackathon_topic})
        
        if image_bytes:
            output_filename = "output_image.png"
            with open(output_filename, "wb") as f:
                f.write(image_bytes)
            print(f"✅ Image saved as '{output_filename}'")
        
        # --- STEP 3: RUN SOCIAL AGENT ---
        print("\n--- STEP 3: Running Social Media Agent ---")
        social_agent = SocialAgent(name="social_agent")
        social_posts = social_agent.execute({"article_text": article_text})

        if social_posts:
            print("\n=== GENERATED SOCIAL POSTS ===")
            print(json.dumps(social_posts, indent=2))
            
        print("\n--- ✅ All agents finished. ---")
            
    else:
        print("❌ Writer Agent failed. Halting workflow.")