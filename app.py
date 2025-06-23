
import os
import streamlit as st
from pipeline import run_content_pipeline, initialize_vertexai

# --- Page Configuration ---
st.set_page_config(
    page_title="Neuroscribe AI",
    page_icon="🤖",
    layout="wide"
)

# --- Initialization ---
@st.cache_resource
def init_gcp():
    # Point to your credentials file
    credentials_path = "google_credentials.json"
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials_path
    
    # Now initialize Vertex AI
    initialize_vertexai()

init_gcp()

# --- UI Components ---
st.title("🤖 Neuroscribe AI Content Generator")
st.markdown("Enter a topic below and let the AI agents create a full content package for you.")

# User input
topic = st.text_input("Enter your content topic:", placeholder="e.g., The Future of Artificial Intelligence")

# Generate button
if st.button("✨ Generate Content", type="primary"):
    if not topic:
        st.warning("Please enter a topic to generate content.")
    else:
        # Use st.status to show progress
        with st.status("🚀 Launching AI agents...", expanded=True) as status:
            st.write("Calling Writer Agent to draft the article...")
            article, image, social_posts = run_content_pipeline(topic)
            
            if article:
                status.update(label="✅ Content Generation Complete!", state="complete", expanded=False)
            else:
                status.update(label="❌ Error during generation.", state="error")

        # --- Display Results ---
        if article:
            st.success("Your content package has been generated successfully!")
            
            # Create two columns for the article and the image
            col1, col2 = st.columns([2, 1])

            with col1:
                st.subheader("📝 Generated Article")
                st.markdown(article)

            with col2:
                if image:
                    st.subheader("🖼️ Generated Image")
                    st.image(image, caption=f"AI-generated image for: {topic}")
                else:
                    st.warning("Image could not be generated.")

            if social_posts:
                st.subheader("📱 Generated Social Media Posts")
                st.json(social_posts)
            else:
                st.warning("Social posts could not be generated.")
        else:
            st.error("Failed to generate content. Please check the logs or try a different topic.")
