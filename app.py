from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType
from camel.configs import GeminiConfig
# from camel.agents import ChatAgent
from core.congfig import GEMINI_API_KEY
from agents.reviewer_agent import get_reviewer_agent
from agents.citation_agent import get_citation_verifier_agent
from agents.methodology_agent import get_methodology_agent
from agents.feedback_agent import get_feedback_agent
import fitz
import gradio as gr


def extract_text_from_pdf(file):
    doc = fitz.open(file.name)
    return "\n".join([page.get_text() for page in doc])


model = ModelFactory.create(
    model_platform=ModelPlatformType.GEMINI,
    model_type=ModelType.GEMINI_2_0_FLASH_LITE,
    model_config_dict=GeminiConfig(temperature=0.2).as_dict(),
    api_key=GEMINI_API_KEY
)

agent_1 = get_reviewer_agent(model)
agent_2 = get_citation_verifier_agent(model)
agent_3 = get_methodology_agent(model)
agent_4 = get_feedback_agent(model)

def review_paper(pdf_file):
    paper_text = extract_text_from_pdf(pdf_file)
    response_get_reviewer_agent = agent_1.step(paper_text)
    response_get_citation_verifier_agent = agent_2.step(paper_text)
    response_get_methodology_agent = agent_3.step(paper_text)
    response_get_feedback_agent = agent_4.step(paper_text)
    
    final_response = f"""
    *********************************************
    <--------- 1. Reviewer ------>
    *********************************************
    
    1. Reviewer: 
    {response_get_reviewer_agent.msgs[0].content}
    
    *********************************************
    <--------- 2. Citation Check ------>
    *********************************************
    
    2. Citation Validation: 
    {response_get_citation_verifier_agent.msgs[0].content}
    
    *********************************************
    <--------- 3. Methodology Check ------>
    *********************************************    
    
    3. Methodology: 
    {response_get_methodology_agent.msgs[0].content}
    
    *********************************************
    <--------- 4. Feedback ------>
    *********************************************
    
    4. Feedback: 
    {response_get_feedback_agent.msgs[0].content}
    """
    
    return final_response


demo = gr.Interface(
    fn=review_paper,
    inputs=gr.File(file_types=[".pdf"], label="Upload Research Paper"),
    outputs=gr.Textbox(label="AI-Powered Peer Review", lines=25),
    title="🧠 CAMEL-AI Research Paper Reviewer",
    description="Upload a PDF research paper to get a multi-agent AI peer review with citation verification."
)

if __name__ == "__main__":
    demo.launch()