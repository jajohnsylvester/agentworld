import os
import uvicorn
from google.adk.cli.fast_api import get_fast_api_app
from my_agent.agent import root_agent

# Initialize the ADK FastAPI application
# The ADK helper creates all necessary /run and /sessions endpoints
app = get_fast_api_app(
    agents_dir=os.path.dirname(os.path.abspath(__file__)),
    web=True # Enables the built-in Web UI for testing
)

if __name__ == "__main__":
    # Render automatically sets the PORT environment variable
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)

