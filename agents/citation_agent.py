from camel.agents import ChatAgent
from camel.messages import BaseMessage
import textwrap

def get_citation_verifier_agent(model):
    # model = GeminiModel(model_type = "gemini-2.0-flash-lite", api_key=GOOGLE_API_KEY, model_config_dict=GeminiConfig().as_dict())
    msg_content = textwrap.dedent(
        "You are an academic integrity agent. Review the content and identify claims or statements that lack proper citations. "
        "Suggest whether references are valid or missing."
    )

    sys_msg = BaseMessage.make_assistant_message(
        role_name="Citations Validation Agent",
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
    #         "You are an academic integrity agent. Review the content and identify claims or statements that lack proper citations. "
    #         "Suggest whether references are valid or missing."
    #     ),
    #     message_window_size=10,
    #     model=model
    # )
