from camel.agents import RoleAssignmentAgent
from agents.reviewer_agent import get_reviewer_agent
from agents.citation_agent import get_citation_verifier_agent
from agents.methodology_agent import get_methodology_agent
from agents.feedback_agent import get_feedback_agent

import fitz  # PyMuPDF


def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    return "\n".join([page.get_text() for page in doc])


def main():
    # Step 1: Load paper
    paper_path = "sample_paper.pdf"  # <-- Update path
    paper_text = extract_text_from_pdf(paper_path)

    # Step 2: Initialize agents
    reviewer = get_reviewer_agent()
    citation_verifier = get_citation_verifier_agent()
    methodology = get_methodology_agent()
    feedback = get_feedback_agent()

    # Step 3: RolePlaying society for collaboration
    agents = [reviewer, citation_verifier, methodology, feedback]
    roleplay = RoleAssignmentAgent(
        agents=agents,
        task_prompt="You are a team of AI reviewers. Analyze this paper and provide a comprehensive review."
    )

    # Step 4: Run agent society
    response = roleplay.run(input=paper_text, max_steps=8)

    # Step 5: Print final feedback
    print("\n=== Final Peer Review Output ===\n")
    print(response.output)


if __name__ == "__main__":
    main()
