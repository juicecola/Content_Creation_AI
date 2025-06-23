
import streamlit as st
import json
import os
from pipeline import run_content_pipeline
from pipeline import initialize_vertexai

# --- Page Configuration ---
st.set_page_config(
    page_title="Neuroscribe AI",
    page_icon="🤖",
    layout="wide"
)

# --- Initialization ---
@st.cache_resource
def init_gcp():
    # Reconstruct the credentials from individual secrets
    creds_dict = {
        "type": st.secrets.gcp_service_account.type,
        "project_id": st.secrets.gcp_service_account.project_id,
        "private_key_id": st.secrets.gcp_service_account.private_key_id,
        "private_key": st.secrets.gcp_service_account.private_key.replace('\\n', '\n'),
        "client_email": st.secrets.gcp_service_account.client_email,
        "client_id": st.secrets.gcp_service_account.client_id,
        "auth_uri": st.secrets.gcp_service_account.auth_uri,
        "token_uri": st.secrets.gcp_service_account.token_uri,
        "auth_provider_x509_cert_url": st.secrets.gcp_service_account.auth_provider_x509_cert_url,
        "client_x509_cert_url": st.secrets.gcp_service_account.client_x509_cert_url
    }

    # Write the reconstructed dictionary to the temp file as a valid JSON string
    with open("temp_credentials.json", "w") as f:
        json.dump(creds_dict, f)

    # Point the environment variable to the new file
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "temp_credentials.json"
    
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
