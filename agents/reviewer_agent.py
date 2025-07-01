from camel.agents import ChatAgent
from camel.typing import RoleType
from camel.configs import ChatGPTConfig

def get_reviewer_agent():
    return ChatAgent(
        role=RoleType.USER,
        name="Reviewer",
        system_message=(
            "You are a meticulous scientific reviewer. "
            "Read the paper and provide a clear, structured summary, covering abstract, methodology, results, and conclusions."
        ),
        model_config=ChatGPTConfig(model="gpt-4")
    )
