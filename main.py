import os
import uvicorn
from google.adk.cli.fast_api import get_fast_api_app
from my_agent.agent import root_agent

app = get_fast_api_app(
    agents_dir=os.path.dirname(os.path.abspath(__file__)),
    web=True
)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)
