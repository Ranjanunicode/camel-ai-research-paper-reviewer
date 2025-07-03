import gradio as gr
from agents.reviewer_agent import get_reviewer_agent
from agents.citation_agent import get_citation_verifier_agent
from agents.methodology_agent import get_methodology_agent
from agents.feedback_agent import get_feedback_agent
from camel.societies.workforce import Workforce
from camel.tasks import Task
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType
from camel.configs.gemini_config import GeminiConfig
from core.congfig import GEMINI_API_KEY
# from utils.semantic_scholar import search_papers_by_claim
import fitz
# from google import genai
# client = genai.Client(api_key=GEMINI_API_KEY)

def extract_text_from_pdf(file):
    doc = fitz.open(file.name)
    return "\n".join([page.get_text() for page in doc])

def review_paper(pdf_file):
    paper_text = extract_text_from_pdf(pdf_file)
    # print(paper_text)
    
    model = ModelFactory.create(
        model_platform=ModelPlatformType.GEMINI,
        model_type=ModelType.GEMINI_2_0_FLASH_LITE,
        model_config_dict=GeminiConfig(temperature=0.8).as_dict(),
        api_key=GEMINI_API_KEY
    )
    
    # Instantiate agents with input-aware citation verifier
    reviewer = get_reviewer_agent(model)
    citation_verifier = get_citation_verifier_agent(model)
    methodology = get_methodology_agent(model)
    feedback = get_feedback_agent(model)
    
    workforce = Workforce('Research Paper Reviewer')

    workforce.add_single_agent_worker(
        description="",
        worker=reviewer,
    ).add_single_agent_worker(
        description="",
        worker=citation_verifier,
    ).add_single_agent_worker(
        description="",
        worker=methodology,
    ).add_single_agent_worker(
        description="",
        worker=feedback,
    )
    
    task = Task(
        content=paper_text,
    )
    
    processed_task = workforce.process_task(task)
    print(processed_task.result)
    
    return processed_task.result

demo = gr.Interface(
    fn=review_paper,
    inputs=gr.File(file_types=[".pdf"], label="Upload Research Paper"),
    outputs=gr.Textbox(label="AI-Powered Peer Review", lines=25),
    title="🧠 CAMEL-AI Research Paper Reviewer",
    description="Upload a PDF research paper to get a multi-agent AI peer review with citation verification."
)

if __name__ == "__main__":
    demo.launch()
