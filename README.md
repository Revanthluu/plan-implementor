# AI Workflow & Tool Recommender (Agentic System)

🚀 **AI Workflow & Tool Recommender** is an interactive multi-agent system built to streamline the planning phase of your software projects. By describing a use case, the system utilizes CrewAI and Google Gemini API to dynamically research tools, frameworks, and APIs, generating a complete execution plan.

## Features
- **Multi-Agent Collaboration**: Powered by CrewAI, utilizing a 'Research Agent' and 'Writer Agent'.
- **Google Gemini Integration**: Fast and capable reasoning for recommending optimal frameworks.
- **Modern UI**: Clean, custom CSS Streamlit interface giving a premium SaaS dashboard feel.
- **Actionable Execution Plan**: From an idea string to a step-by-step developer guide.
- **Copy to Clipboard**: Easily export the generated markdown recommendations.

## Architecture

```
User Input (Use Case) --> Streamlit App (Frontend)
                               |
                               V
                         CrewAI (Orchestrator)
                               |
                -------------------------------
               |                               |
       Agent 1: Researcher              Agent 2: Writer
      (Finds tools, APIs)            (Generates workflow)
               |                               |
                -------------------------------
                               |
                    Google Gemini API (LLM Engine)
                               |
                               V
             Final Markdown Output (Tools + Steps + Plan)
```

## Tech Stack

- **CrewAI**: Orchestrates the multi-agent system (Researcher, Writer, Cost Analyst).
- **Google Gemini API**: Powers the reasoning engine across all agents using the `gemini-2.5-flash` model.
- **Streamlit**: Renders the frontend interface featuring glassmorphism CSS, state management, and real-time chat.
- **Python**: Core backend logic and tooling.
- **Litellm**: Handles LLM API routing inside the CrewAI environment.

## Setup Instructions

### 1. Create a Virtual Environment
```bash
python -m venv venv
```

### 2. Activate the Environment
- On Windows:
```bash
venv\Scripts\activate
```
- On Mac/Linux:
```bash
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Setup API Keys
Rename `.env.example` to `.env` and add your Google Gemini API key:
```env
GEMINI_API_KEY=your_gemini_api_key_here
```

## How to Run

Start the Streamlit development server:

```bash
streamlit run app.py
```
Open your browser to `http://localhost:8501`.

## Example Usage

**Input:**
> "Build a RAG chatbot"

**Expected Output (Abridged):**
The system spins up the researcher to identify LangChain, FAISS, Gemini Embeddings, and Streamlit. The writer then formats this to:
- **Step 1:** Setup Vector Database (FAISS).
- **Step 2:** Document ingestion & chunking.
- **Step 3:** LLM QA chain connection...
Along with precise implementation tool lists.
