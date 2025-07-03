from camel.agents import ChatAgent
from camel.messages import BaseMessage
import textwrap

def get_methodology_agent(model):
    # model = GeminiModel(model_type = "gemini-2.0-flash-lite", api_key=GOOGLE_API_KEY, model_config_dict=GeminiConfig().as_dict())

    msg_content = textwrap.dedent(
        "You are a research methodology expert. Review the experimental setup, evaluation methods, and data handling of the paper. "
        "Point out flaws, missing validations, or biases in the methods."
    )

    sys_msg = BaseMessage.make_assistant_message(
        role_name="Methodology Expert",
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
    #         "You are a research methodology expert. Review the experimental setup, evaluation methods, and data handling of the paper. "
    #         "Point out flaws, missing validations, or biases in the methods."
    #     ),
    #     message_window_size=10,
    #     model=model
    # )