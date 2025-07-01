from camel.agents import ChatAgent
from camel.typing import RoleType
from camel.configs import ChatGPTConfig

def get_feedback_agent():
    return ChatAgent(
        role=RoleType.ASSISTANT,
        name="Feedback Synthesizer",
        system_message=(
            "You are a peer-review assistant. Combine the insights from other agents to write final feedback for the author. "
            "Include summary, strengths, weaknesses, and suggested improvements."
        ),
        model_config=ChatGPTConfig(model="gpt-4")
    )
