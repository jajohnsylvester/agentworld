from google.adk.agents import Agent

# Define the primary agent
root_agent = Agent(
    model='gemini-2.0-flash',  # Use a valid model name
    name='render_sample_agent',
    description='A helpful assistant for answering general questions.',
    instruction='You are a professional assistant. Keep answers brief and helpful.'
)
