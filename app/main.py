import sys
import os
import streamlit as st
from dotenv import load_dotenv

# 1. Setup Environment
load_dotenv()
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

from agents.strategist import strategist_swarm 
from tools.pdf_processor import process_agricultural_pdf

st.set_page_config(page_title="GreenPulse Agro-Swarm", page_icon="🌾", layout="wide")

# 2. Correct Session State Initialization
if "session_service" not in st.session_state:
    st.session_state.session_service = InMemorySessionService()

# 3. Initialize the Runner using the service directly from session_state
# FIX: Removed the extra .session_state that caused the AttributeError
runner = Runner(
    agent=strategist_swarm, 
    app_name="GreenPulseAgro", 
    session_service=st.session_state.session_service,
    auto_create_session=True,   # <- key fix
)

st.title("🌾 GreenPulse: Agro-Intelligence Swarm")

col1, col2 = st.columns(2)
with col1:
    location = st.text_input("📍 Farmer's Location:", "Nakuru, Kenya")
with col2:
    uploaded_file = st.file_uploader("📂 Agricultural Research (PDF)", type="pdf")

if st.button("🚀 Run Intelligence Swarm"):
    if uploaded_file is not None:
        with st.spinner("Swarm agents are coordinating..."):
            # Process the PDF
            with open("temp_research.pdf", "wb") as f:
                f.write(uploaded_file.getbuffer())
            
            research_summary = process_agricultural_pdf("temp_research.pdf")
            
            # 4. FIX: Corrected F-String Syntax (Line 72 area)
            weather_ctx = f"Location: {location}. Conditions: High humidity/rain."
            full_prompt_text = f"Process this data. Weather: {weather_ctx}. Research: {research_summary}"
            
            user_message = types.Content(
                role="user",
                parts=[types.Part(text=full_prompt_text)]
            )

            # 5. Run the swarm
            # Using session_id "default" to ensure the service finds it
            st.session_state.session_service.create_session(
                app_name="GreenPulseAgro",
                user_id="farmer_1",
                session_id="default",
            )

            events = runner.run(
                user_id="farmer_1",
                session_id="default",
                new_message=user_message,
            )

            final_plan = ""
            for event in events:
                # Catching any content emitted by the final strategist
                if event.content and event.content.parts:
                    final_plan = event.content.parts[0].text

            if final_plan:
                st.success("Analysis Complete!")
                st.markdown("---")
                st.markdown(final_plan)
            else:
                st.error("The swarm was unable to synthesize a plan. Please try again.")
    else:
        st.warning("Please upload a research PDF.")