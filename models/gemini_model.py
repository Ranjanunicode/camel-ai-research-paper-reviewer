from camel.messages import BaseMessage
from core.congfig import GOOGLE_API_KEY
from camel.models.gemini_model import GeminiModel
from camel.configs.gemini_config import GeminiConfig

class GeminiChatModel(GeminiModel):
    def __init__(self, model_type: str = "gemini-2.0-flash-lite", api_key=GOOGLE_API_KEY, **kwargs):
        config = GeminiConfig(
            temperature=0.7,
            max_tokens=1024,
            **kwargs
        )
        super().__init__(
            model_type=model_type,
            model_config_dict=config.as_dict(),
            api_key=api_key
        )

    def run(self, messages: list[BaseMessage], **kwargs):
        # CAMEL expects OpenAI-compatible format – it handles conversion internally
        openai_messages = [msg.to_openai_message() for msg in messages]
        resp = self._run(openai_messages, **kwargs)
        # _run returns either a ChatCompletion or stream; normalize:
        return resp.choices[0].message.content if hasattr(resp, "choices") else resp