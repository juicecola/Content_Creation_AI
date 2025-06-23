graph TD;
    subgraph "User Interaction"
        User[👤 User]
    end

    subgraph "Application Frontend"
        UI[💻 Streamlit Web UI]
    end

    subgraph "Application Backend (Python)"
        Pipeline[⚙️ Pipeline Logic]
        WriterAgent[✍️ Writer Agent]
        VisualAgent[🎨 Visual Agent]
        SocialAgent[📱 Social Agent]
    end

    subgraph "Google Cloud Services"
        VertexAI[☁️ Vertex AI]
        Gemini[🧠 Gemini Model]
        Imagen[🖼️ Imagen Model]
    end

    %% --- Define The Connections ---
    User -- "Submits Topic" --> UI;
    UI -- "Triggers Pipeline" --> Pipeline;
    
    Pipeline -- "Calls" --> WriterAgent;
    Pipeline -- "Calls" --> VisualAgent;
    Pipeline -- "Calls" --> SocialAgent;

    WriterAgent -- "Generates Text via" --> Gemini;
    SocialAgent -- "Uses Text for Posts" --> WriterAgent

    VisualAgent -- "Generates Image via" --> Imagen;

    Gemini --> VertexAI;
    Imagen --> VertexAI;
    
    %% --- Styling (Optional) ---
    style User fill:#cde4ff
    style UI fill:#e1d5e7,stroke:#9656a1,stroke-width:2px
    style VertexAI fill:#f9f,stroke:#333,stroke-width:4px
