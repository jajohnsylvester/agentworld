import os
import uvicorn
from google.adk.api.fast_api import create_app
from my_agent.agent import root_agent

# Initialize the ADK FastAPI application
app = create_app(agents=[root_agent])

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)
