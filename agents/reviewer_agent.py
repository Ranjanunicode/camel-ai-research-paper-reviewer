from camel.agents import ChatAgent
from camel.messages import BaseMessage
import textwrap

# model = "gemini-2.0-flash-lite"

def get_reviewer_agent(model):
    
    msg_content = textwrap.dedent(
        "You are a meticulous scientific reviewer. Read the provided research paper and summarize key sections "
        "like abstract, methodology, results, and conclusion in a structured format."
    )

    sys_msg = BaseMessage.make_assistant_message(
        role_name="Reviewer",
        content=msg_content,
    )
    
    # model = GeminiModel(model_type = "gemini-2.0-flash-lite", api_key=GOOGLE_API_KEY, model_config_dict=GeminiConfig().as_dict())
    agent = ChatAgent(
        system_message=sys_msg,
        message_window_size=10,
        model=model
    )
    return agent

# def get_reviewer_agent():
#     model = GeminiModel(model_type = "gemini-2.0-flash-lite", api_key=GOOGLE_API_KEY, model_config_dict=GeminiConfig().as_dict())
#     return ChatAgent(
#         role=RoleType.USER,
#         name="Reviewer",
#         system_message=(
#             "You are a meticulous scientific reviewer. Read the provided research paper and summarize key sections "
#             "like abstract, methodology, results, and conclusion in a structured format."
#         ),
#         model=model
#     )