from google.adk.agents import Agent
from google.adk.types import LlmRequest

def change_model_callback(request: LlmRequest, context):
    """
    Intercepts the request and changes the model based on session metadata.
    """
    # Look for a specific model override in the session state
    model_override = context.session.state.get("selected_model")
    if model_override:
        request.model = model_override
    return request

# Define the agent with the callback
root_agent = Agent(
    model='gemini-2.0-flash',  # Default model
    name='render_sample_agent',
    description='A helpful assistant with dynamic model switching.',
    instruction='You are a professional assistant.',
    before_model_callback=change_model_callback # Register the callback
)
