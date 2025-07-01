import gradio as gr
from agents.reviewer_agent import get_reviewer_agent
from agents.citation_agent import get_citation_verifier_agent
from agents.methodology_agent import get_methodology_agent
from agents.feedback_agent import get_feedback_agent
from camel.agents import RolePlaying
# from utils.semantic_scholar import search_papers_by_claim
import fitz

def extract_text_from_pdf(file):
    doc = fitz.open(file.name)
    return "\n".join([page.get_text() for page in doc])

def review_paper(pdf_file):
    paper_text = extract_text_from_pdf(pdf_file)

    # Instantiate agents with input-aware citation verifier
    reviewer = get_reviewer_agent()
    citation_verifier = get_citation_verifier_agent(paper_text)
    methodology = get_methodology_agent()
    feedback = get_feedback_agent()

    agents = [reviewer, citation_verifier, methodology, feedback]

    society = RolePlaying(
        agents=agents,
        task_prompt="You are a team of AI reviewers. Analyze this paper and generate a peer review."
    )

    result = society.run(input=paper_text, max_steps=8)
    return result.output

demo = gr.Interface(
    fn=review_paper,
    inputs=gr.File(file_types=[".pdf"], label="Upload Research Paper"),
    outputs=gr.Textbox(label="AI-Powered Peer Review", lines=25),
    title="🧠 CAMEL-AI Research Paper Reviewer",
    description="Upload a PDF research paper to get a multi-agent AI peer review with citation verification."
)

if __name__ == "__main__":
    demo.launch()
