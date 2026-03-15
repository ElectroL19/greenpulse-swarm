from google.adk.agents import LlmAgent

scout = LlmAgent(
    name="ClimateScout",
    model="gemini-3-flash",
    description="Analyzes weather alerts and seasonal climate PDFs.",
    instruction="""
    You are a Meteorological Analyst. Your goal is to identify climate risks 
    (rain, drought, heatwaves) from the provided weather data and news.
    Output only the high-level risks and their expected duration.
    """,
    output_key="weather_intel"  # This saves the result for the next agent
)