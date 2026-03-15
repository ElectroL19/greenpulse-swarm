from google.adk.agents import LlmAgent, SequentialAgent

# Standard 2026 Model ID for the Gemini 3 Flash series
MODEL_ID = "gemini-3-flash-preview"

# 1. Weather Agent (ClimateScout)
# This agent extracts weather-specific risks from the location string or history
scout = LlmAgent(
    name="ClimateScout",
    model=MODEL_ID,
    instruction="""You are a weather specialist. Extract specific climate risks 
    (floods, drought, high humidity) for the farmer's location. 
    Focus on impact to crops.""",
    output_key="weather_intel"
)

# 2. Research Agent (BioSentry)
# This agent analyzes technical text (like your PDF summary) for pest risks
sentry = LlmAgent(
    name="BioSentry",
    model=MODEL_ID,
    instruction="""You are a biological risk specialist. Analyze the agricultural 
    data provided and identify specific pest or disease threats. 
    Reference the names of insects or diseases found.""",
    output_key="bio_intel"
)

# 3. Final Synthesis Agent (Strategist)
# This is an LLM agent that reads the state variables created by Scout and Sentry
final_strategist = LlmAgent(
    name="FinalStrategist",
    model=MODEL_ID,
    instruction="""You are a master agricultural strategist. 
    Synthesize the following intelligence into a 7-day tactical farm plan:
    - Weather Risks: {weather_intel}
    - Biological/Pest Risks: {bio_intel}
    
    Provide specific, numbered action steps for planting, spraying, and irrigation."""
)

# 4. The Orchestrator (strategist_swarm)
# SequentialAgent manages the flow but DOES NOT take an 'instruction' itself.
# It simply executes sub_agents in the order provided.
strategist_swarm = SequentialAgent(
    name="HarvestStrategistSwarm",
    sub_agents=[scout, sentry, final_strategist]
)