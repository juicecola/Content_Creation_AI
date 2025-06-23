 AI Multi-Agent Content Pipeline
![alt text](https://img.shields.io/badge/python-3.9+-blue.svg)

![alt text](https://img.shields.io/badge/Built%20with-Google%20Cloud-blueviolet)

![alt text](https://img.shields.io/badge/License-MIT-green.svg)

Neuroscribe is an automated content creation pipeline that demonstrates a powerful multi-agent system. Built with the Google Agent Development Kit (ADK) for Python and powered by Google Cloud's Vertex AI, it transforms a single topic into a complete content package.

The system coordinates a team of specialist AI agents to research a topic, write a detailed article, design a feature image, and draft promotional social media posts.

✨ Core Features
Automated End-to-End Workflow: From a single topic, generate a blog post, image, and social content without manual intervention.

Modular Agent Architecture: Each agent has a specific role, making the system easy to maintain, test, and extend.

Research-Driven Content: An initial research step ensures the generated article is well-informed.

AI-Powered Generation: Leverages state-of-the-art models from Vertex AI (Gemini for text, Imagen for images).

Scalable Framework: Built on the Google ADK, providing a solid foundation for more complex agentic workflows.

⚙️ How It Works: The Agent Assembly Line
The entire process is managed by the orchestrator_agent.py, which executes a sequence of specialist agents, passing the state from one to the next.

Topic Input: The workflow begins with a user-defined topic (e.g., "The Future of Renewable Energy").

research_agent.py:

Role: The Analyst.

Action: Takes the topic and performs preliminary information gathering to create a foundation of facts or key points.

writer_agent.py:

Role: The Author.

Action: Receives the topic and research findings, then uses a powerful language model (Gemini) to write a comprehensive and engaging article.

visual_agent.py:

Role: The Illustrator.

Action: Takes the original topic and generates a high-quality, relevant feature image using a text-to-image model (Imagen).

social_agent.py:

Role: The Marketer.

Action: Reads the final generated article and creates a series of short, engaging social media posts to promote it on platforms like Twitter or LinkedIn.

🛠️ Tech Stack
Core Framework: Google Agent Development Kit (ADK) for Python

AI Platform: Google Cloud Vertex AI

Language Models: Gemini Pro or Flash

Image Generation: Imagen

Language: Python 3.9+

🚀 Getting Started
Follow these steps to set up and run the pipeline in your own environment.

1. Prerequisites
A Google Cloud Platform (GCP) project with the Vertex AI API enabled.

The gcloud command-line tool installed and authenticated.

Python 3.9 or newer.

2. Installation
Clone the Repository

Generated bash
git clone https://github.com/juicecola/Content_Creation_AI.git
cd Content_Creation_AI
Use code with caution.
Bash
Set Up a Python Virtual Environment

Generated bash
python3 -m venv venv
source venv/bin/activate
Use code with caution.
Bash
Install Dependencies
First, create a requirements.txt file with the necessary libraries:

Generated txt
# requirements.txt
google-cloud-aiplatform
google-generativeai
Use code with caution.
Txt
Now, install them:

Generated bash
pip install -r requirements.txt
# If the adk-python is a local copy, install it in editable mode
pip install -e adk-python
Use code with caution.
Bash
3. Configuration and Authentication
Authenticate Your Local Environment
This command links your local machine to your GCP account, allowing the script to use the Vertex AI API securely.

Generated bash
gcloud auth application-default login
Use code with caution.
Bash
Set Your Project Configuration
Open the orchestrator_agent.py file (or a central main.py/config.py) and update the GCP project details:

Generated python
# In orchestrator_agent.py or your main script
GCP_PROJECT_ID = "your-gcp-project-id"  # <-- IMPORTANT: CHANGE THIS
GCP_LOCATION = "us-central1"           # Or your preferred region
Use code with caution.
Python
▶️ How to Run
Execute the orchestrator agent from your terminal. It will trigger the entire pipeline and print the progress and final outputs to the console.

Generated bash
python orchestrator_agent.py
Use code with caution.
Bash
Upon successful execution, you will see:

The generated article text.

A new image file (e.g., output_image.png) in your directory.

A JSON object containing the social media posts.

⚖️ License
This project is distributed under the MIT License. See the LICENSE file for more information.
