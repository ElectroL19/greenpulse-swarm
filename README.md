# 🌾 GreenPulse Agro-Intelligence Swarm
**Strategic Intelligence for Small-Scale Sustainable Farming**

## 📝 Problem Statement
Small-scale farmers in developing regions are facing unprecedented climate volatility. While raw data (weather forecasts, pest research) exists, it is often locked in dense, unstructured PDF reports or complex scientific databases. Farmers lack an "Intelligence layer" to synthesize this data into immediate tactical actions, leading to avoidable crop failures.

## 🏗️ System Architecture
The system utilizes a **SequentialAgent** workflow where specialized agents collaborate to bridge the gap between technical research and field action.

1. **ClimateScout (Weather Agent):** Analyzes real-time climate data to identify immediate physical risks like flooding or drought.
2. **BioSentry (Research Agent):** Processes academic PDF research to extract biological threats (pests/diseases) relevant to the context.
3. **FinalStrategist (Orchestrator):** Synthesizes weather and biological data into a numbered, 7-day tactical farm plan.

## 📁 Project Structure
- `/app`: Contains `main.py` (The Streamlit interface).
- `/agents`: Contains `strategist.py` (Swarm logic and Agent definitions).
- `/tools`: Contains `pdf_processor.py` (PDF text extraction and analysis).
- `requirements.txt`: Project dependencies.

## 🚀 Getting Started
1. Clone the repo.
2. Install dependencies: `pip install -r requirements.txt`.
3. Set your `GOOGLE_API_KEY` in a `.env` file.
4. Run the app: `python -m streamlit run app/main.py`.

## 🌍 UN Sustainable Development Goal (SDG) Alignment
* **Goal 2: Zero Hunger**
* **Goal 13: Climate Action**

### Impact Reason
GreenPulse converts unstructured global climate data into hyper-local "Field Intelligence." By identifying pest risks and weather shifts before they happen, we provide a safety net for food security and promote climate-resilient farming practices.

## 🤖 Agent Profiles & Responsibilities
Our solution uses a triple-agent architecture orchestrated via the **Google ADK**:
1.  **Climate Scout (Meteorological Analyst):** Monitors real-time weather and analyzes 30-day seasonal forecast PDFs.
2.  **Bio-Sentry (Agronomy Researcher):** Scours academic databases for emerging pest threats and crop disease patterns.
3.  **Harvest Strategist (Swarm Coordinator):** The "Brain" that performs the final reasoning. It cross-references Scout and Sentry data to produce a 7-day Tactical Farm Plan.

## 🧠 Chain-of-Thought (CoT) Logic
The swarm utilizes **Thought Signatures** to maintain context. 
* **Re-Planning:** If the "Climate Scout" fails to find a local weather station via API, it triggers a "Plan B" sequence: searching regional news via the Search Tool to infer conditions.
* **Validation:** The Strategist will not issue a recommendation unless it finds a correlation in the "Blackboard" from both sub-agents.

## 🛡️ Security & Guardrails
* **Output Hardening:** All agents are restricted to returning valid JSON or Markdown to prevent prompt injection from affecting the UI.
* **Safety Filter:** A hard-coded "Safe-Pesticide List" prevents the agent from recommending chemicals banned by international environmental standards.

## 📈 Success Metrics
* **Synthesis Efficiency:** Ability to compress 200+ pages of unstructured data into a 300-word tactical brief.
* **Accuracy:** 90%+ alignment with expert agronomist recommendations in test scenarios.

## 🚀 Technical Innovation
Unlike a simple RAG chatbot, GreenPulse is **agentic**. It doesn't just retrieve information; it **reasons** over conflicting data. If weather data says "Dry" but pest data says "Humid Pests," the Harvest Strategist autonomously initiates a third research task to resolve the discrepancy before answering the user.

## 🛠️ Google ADK Implementation
* **APIs:** Grounding with Google Search, OpenWeatherMap API.
* **Files:** Local PDF processing for university agricultural guidelines.
* **Model:** Powered by **Gemini 3 Flash** for low-latency multi-agent reasoning.

## 🛠 System Architecture Diagram
The following diagram, generated via NotebookLM and Mermaid, illustrates the data flow between our specialized agents:

```mermaid
graph TD
graph TD
    %% Input Node
    Input([Farmer Input: Location & PDF]) --> Scout

    %% The Orchestrator Box
    subgraph Swarm ["HarvestStrategistSwarm (SequentialAgent)"]
        Scout[<b>1. ClimateScout</b><br/>Weather & Climate Risks]
        Scout -- "weather_intel" --> Sentry
        
        Sentry[<b>2. BioSentry</b><br/>Pest & Disease Identification]
        Sentry -- "bio_intel" --> Strategist
        
        Strategist[<b>3. FinalStrategist</b><br/>Intelligence Synthesis]
    end

    %% Output Node
    Strategist --> Output([7-Day Tactical Farm Plan])

    %% Uniform Plain Styling
    classDef plain fill:#ffffff,stroke:#333333,stroke-width:1px,color:#000000;
    class Input,Scout,Sentry,Strategist,Output plain;
    
    style Swarm fill:none,stroke:#333333,stroke-dasharray: 5 5,color:#000000
