from camel.configs.openai_config import ChatGPTConfig
import gradio as gr
from agents.coordinator_agent import get_coordinator_agent
from agents.reviewer_agent import get_reviewer_agent
from agents.citation_agent import get_citation_verifier_agent
from agents.methodology_agent import get_methodology_agent
from agents.feedback_agent import get_feedback_agent
from camel.societies.workforce import Workforce
from camel.tasks import Task
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType
# from camel.configs.gemini_config import GeminiConfig
from agents.taskManager_agent import get_task_manager_agent
from core.congfig import GEMINI_API_KEY, OPENAI_API_KEY
# from utils.semantic_scholar import search_papers_by_claim
import fitz
# from camel.agents import ChatAgent
# from camel.types import RoleType
# from google import genai
# client = genai.Client(api_key=GEMINI_API_KEY)

def extract_text_from_pdf(file):
    doc = fitz.open(file.name)
    return "\n".join([page.get_text() for page in doc])

def review_paper(pdf_file):
    paper_text = extract_text_from_pdf(pdf_file)
    # print(paper_text)
    
    # model = ModelFactory.create(
    #     model_platform=ModelPlatformType.GEMINI,
    #     model_type=ModelType.GEMINI_2_0_FLASH_LITE,
    #     model_config_dict=GeminiConfig(temperature=0.8).as_dict(),
    #     api_key=GEMINI_API_KEY
    # )
    model = ModelFactory.create(
        model_platform=ModelPlatformType.OPENAI,
        model_type=ModelType.O4_MINI,
        model_config_dict=ChatGPTConfig(temperature=0.8).as_dict(),
        api_key=OPENAI_API_KEY
    )
    
    coordinator = get_coordinator_agent(model)
    task_manager = get_task_manager_agent(model)
    
    # Instantiate agents with input-aware citation verifier
    reviewer = get_reviewer_agent(model)
    citation_verifier = get_citation_verifier_agent(model)
    methodology = get_methodology_agent(model)
    feedback = get_feedback_agent(model)
    
    workforce = Workforce(
        description="Research Paper Reviewer Workflow",
        coordinator_agent=coordinator,
        task_agent=task_manager,
        share_memory=True
    )

    workforce.add_single_agent_worker(
        description="Manages task scheduling, dependencies, and execution flow for the review process",
        worker=task_manager,
    ).add_single_agent_worker(
        description="Conducts comprehensive review of research methodology and experimental design",
        worker=methodology,
    ).add_single_agent_worker(
        description="Verifies citations, references, and ensures academic integrity",
        worker=citation_verifier,
    ).add_single_agent_worker(
        description="Performs detailed content review and quality assessment",
        worker=reviewer,
    ).add_single_agent_worker(
        description="Generates constructive feedback and improvement recommendations",
        worker=feedback,
    )
    
    task = Task(
        content=f"""
        RESEARCH PAPER REVIEW REQUEST
        
        Paper Content:
        {paper_text}
        
        Review Requirements:
        1. Methodology Assessment: Evaluate research design, methods, and experimental approach
        2. Citation Verification: Check references, citations, and academic integrity
        3. Content Review: Assess clarity, contribution, and scientific rigor
        4. Feedback Generation: Provide constructive suggestions for improvement
        
        Expected Deliverables:
        - Comprehensive review report
        - Methodology evaluation
        - Citation audit results
        - Improvement recommendations
        - Overall quality assessment
        """,
        additional_info={
            "priority": "high",
            "review_type": "comprehensive",
            "expected_sections": ["methodology", "citations", "content", "feedback"]
        }
    )
    
    processed_task = workforce.process_task(task)
    # print(processed_task.result)
    print("Metadata")
    print(processed_task.content)
    print(processed_task.type)
    print(processed_task.additional_info)
    print(processed_task.assigned_worker_id)
    print(processed_task.state)
    
    
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
