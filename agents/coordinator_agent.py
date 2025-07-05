from camel.agents import ChatAgent
from camel.messages import BaseMessage

def get_coordinator_agent(model):
    """
    Create a coordinator agent to manage the research paper review workflow
    """
    coordinator_system_message = BaseMessage.make_assistant_message(
        role_name="Research Review Coordinator",
        content="""You are the coordinator for a research paper review team. Your responsibilities include:
        
        1. Analyzing incoming research papers and determining the review workflow
        2. Assigning specific sections or aspects to appropriate specialist agents
        3. Managing the sequence of reviews (methodology → citations → feedback → final review)
        4. Synthesizing results from all agents into a comprehensive final report
        5. Ensuring quality control and completeness of the review process
        
        You should:
        - Break down complex papers into manageable review tasks
        - Coordinate between different specialist agents
        - Ensure all critical aspects are covered
        - Provide clear task assignments and priorities
        - Consolidate findings into actionable insights
        
        Always maintain a structured approach and clear communication with all team members."""
    )
    
    return ChatAgent(
        system_message=coordinator_system_message,
        model=model,
        message_window_size=50
    )
