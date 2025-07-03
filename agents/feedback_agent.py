from camel.agents import ChatAgent
from camel.messages import BaseMessage
import textwrap

def get_feedback_agent(model):
    # model = GeminiModel(model_type = "gemini-2.0-flash-lite", api_key=GOOGLE_API_KEY, model_config_dict=GeminiConfig().as_dict())
    msg_content = textwrap.dedent(
        "You are a peer-review feedback assistant. Your job is to combine feedback from other reviewers and compile a summary report. "
        "This report should include a summary, strengths, weaknesses, and suggested improvements."
    )

    sys_msg = BaseMessage.make_assistant_message(
        role_name="Feedback Assistant",
        content=msg_content,
    )
    
    # model = GeminiModel(model_type = "gemini-2.0-flash-lite", api_key=GOOGLE_API_KEY, model_config_dict=GeminiConfig().as_dict())
    agent = ChatAgent(
        system_message=sys_msg,
        message_window_size=10,
        model=model
    )
    return agent
    # return ChatAgent(
    #     system_message=(
    #         "You are a peer-review feedback assistant. Your job is to combine feedback from other reviewers and compile a summary report. "
    #         "This report should include a summary, strengths, weaknesses, and suggested improvements."
    #     ),
    #     message_window_size=10,
    #     model=model
    # )
