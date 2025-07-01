from camel.agents import ChatAgent
from camel.typing import RoleType
from camel.configs import ChatGPTConfig

def get_methodology_agent():
    return ChatAgent(
        role=RoleType.ASSISTANT,
        name="Methodology Analyst",
        system_message=(
            "You are an expert in experimental design. Your task is to critique the methodology used in the paper — including sample sizes, data integrity, reproducibility, and evaluation metrics."
        ),
        model_config=ChatGPTConfig(model="gpt-4")
    )
