import streamlit as st
from crew import WorkflowCrew
import time
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Set page configuration for professional SaaS look
st.set_page_config(
    page_title="Agentic Workflow Builder V2",
    page_icon="🔮",
    layout="wide"
)

# Load ENV and configure genai for chat
load_dotenv(override=True)
api_key = os.getenv("GEMINI_API_KEY")
if api_key:
    genai.configure(api_key=api_key)

# Custom CSS for styling (Glassmorphism & Gradients)
st.markdown("""
<style>
    /* Main Background & Font */
    body, .stApp {
        background: linear-gradient(135deg, #f1f5f9 0%, #e2e8f0 100%);
        font-family: 'Inter', sans-serif;
    }
    
    /* Premium Header Styling */
    .main-header {
        text-align: center;
        padding: 3rem 2rem;
        background: linear-gradient(135deg, rgba(30, 58, 138, 0.9), rgba(59, 130, 246, 0.9));
        backdrop-filter: blur(10px);
        color: white;
        border-radius: 16px;
        margin-bottom: 2rem;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        border: 1px solid rgba(255,255,255,0.2);
    }
    .main-header h1 {
        font-weight: 800;
        letter-spacing: -0.5px;
        margin-bottom: 0.5rem;
    }
    .main-header p {
        font-size: 1.2rem;
        opacity: 0.9;
        font-weight: 300;
    }
    
    /* Glassmorphic Cards */
    .stCard {
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        padding: 2rem;
        border-radius: 16px;
        box-shadow: 0 8px 32px rgba(31, 38, 135, 0.07);
        border: 1px solid rgba(255, 255, 255, 1);
        margin-bottom: 1.5rem;
    }
    
    /* Input Area */
    .stTextInput>div>div>input {
        border-radius: 12px;
        border: 2px solid #cbd5e1;
        padding: 14px;
        font-size: 1.1rem;
        transition: border-color 0.3s;
    }
    .stTextInput>div>div>input:focus {
        border-color: #3b82f6;
    }
    
    /* Buttons */
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #2563eb, #1d4ed8);
        color: white;
        border: None;
        border-radius: 12px;
        padding: 14px 24px;
        font-size: 1.1rem;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(37, 99, 235, 0.3);
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(37, 99, 235, 0.4);
    }
</style>
""", unsafe_allow_html=True)

# Initialize Session State
if 'workflow_result' not in st.session_state:
    st.session_state.workflow_result = None
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Header Section
st.markdown("""
<div class="main-header">
    <h1>🔮 AI Workflow & Tool Recommender V2</h1>
    <p>Powered by Multi-Agent Architecture (CrewAI & Google Gemini)</p>
</div>
""", unsafe_allow_html=True)

# Tabs Layout
tab1, tab2 = st.tabs(["🚀 Workflow Generator", "💬 Interactive Q&A"])

with tab1:
    with st.container():
        st.markdown('<div class="stCard">', unsafe_allow_html=True)
        st.subheader("What do you want to build?")
        use_case = st.text_input("Enter your use case (e.g., 'Build a startup landing page', 'Create a RAG chatbot'):")
        
        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            generate_btn = st.button("Generate Workflow ⚡")
        st.markdown('</div>', unsafe_allow_html=True)

    if generate_btn:
        if not use_case.strip():
            st.error("Please enter a valid use case.")
        else:
            with st.status("🤖 Agents are collaborating (Research, Writing, & Cost Analysis)...", expanded=True) as status:
                st.write("🔍 Research Agent is gathering tools...")
                st.write("✍️ Writer Agent is constructing step-by-step workflow...")
                st.write("💰 Cost Analyst Agent is calculating pricing & tech flow...")
                try:
                    start_time = time.time()
                    crew_system = WorkflowCrew(use_case)
                    result = crew_system.run()
                    st.session_state.workflow_result = result
                    # Reset chat history for new workflow
                    st.session_state.chat_history = [] 
                    duration = round(time.time() - start_time, 2)
                    status.update(label=f"Workflow generated successfully in {duration} seconds! 🎉", state="complete", expanded=False)
                except Exception as e:
                    status.update(label="An error occurred.", state="error", expanded=False)
                    st.error(f"Error details: {str(e)}")

    if st.session_state.workflow_result:
        st.markdown('<div class="stCard">', unsafe_allow_html=True)
        st.subheader("📋 Final Execution Plan, Pricing & Impact")
        st.markdown(st.session_state.workflow_result)
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown("### 📥 Export")
        st.info("Copy the full workflow report using the button inside the code block below:")
        st.code(st.session_state.workflow_result, language='markdown')

with tab2:
    st.markdown('<div class="stCard">', unsafe_allow_html=True)
    st.subheader("💬 Ask questions about your Workflow")
    if not st.session_state.workflow_result:
        st.info("Please generate a workflow first in the 'Workflow Generator' tab before asking questions.")
    else:
        st.write("You can ask specific questions about the tech flows, how to deploy, or code generation related to the workflow above.")
        
        # Display chat messages from history on app rerun
        for message in st.session_state.chat_history:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # Accept user input
        if prompt := st.chat_input("Ask a follow-up question here..."):
            with st.chat_message("user"):
                st.markdown(prompt)
            st.session_state.chat_history.append({"role": "user", "content": prompt})

            with st.chat_message("assistant"):
                message_placeholder = st.empty()
                if not api_key:
                    message_placeholder.markdown("⚠️ GEMINI_API_KEY is not configured.")
                else:
                    try:
                        # Construct prompt with context
                        system_context = f"You are an expert AI architect. Answer the user's question perfectly in context to this generated workflow:\\n\\n{st.session_state.workflow_result}"
                        
                        # We use Gemini flash for lightning fast chat responses
                        model = genai.GenerativeModel('gemini-2.5-flash')
                        
                        # Generate response
                        full_prompt = f"{system_context}\\n\\nUser Question: {prompt}"
                        response = model.generate_content(full_prompt)
                        
                        message_placeholder.markdown(response.text)
                        st.session_state.chat_history.append({"role": "assistant", "content": response.text})
                    except Exception as e:
                        message_placeholder.markdown(f"An error occurred during chat: {str(e)}")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("""
<div style='text-align: center; margin-top: 50px; color: #64748b;'>
    <small>Agentic System Design V2 · Premium UI · CrewAI · Streamlit · Google Gemini</small>
</div>
""", unsafe_allow_html=True)
