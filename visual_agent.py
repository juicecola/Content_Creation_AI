# visual_agent.py

from google.adk import Agent
from vertexai.preview.vision_models import ImageGenerationModel

class VisualCreatorAgent(Agent):
    def execute(self, data: dict) -> bytes:
        topic = data.get("topic", "abstract technology")
        print(f"🎨 Visual Creator Agent received topic: '{topic}'.")
        
        # We will create a clear, concise prompt for the image model
        prompt_text = f"A high-quality, photorealistic image representing the concept of: '{topic}'"
        
        # --- NEW: LOG THE EXACT PROMPT ---
        print(f"--> Sending this prompt to Imagen API: \"{prompt_text}\"")
        
        model = ImageGenerationModel.from_pretrained("imagegeneration@006")
        try:
            response = model.generate_images(prompt=prompt_text, number_of_images=1)
            print("✅ Visual Agent successfully generated image bytes.")
            return response[0]._image_bytes
        except Exception as e:
            # --- NEW: LOG THE SPECIFIC ERROR ---
            print(f"❌ Visual Creator Agent FAILED. Error from Google API: {e}")
            return None