from camel.agents import ChatAgent
from camel.typing import RoleType
from camel.configs import ChatGPTConfig

def get_citation_verifier_agent():
    return ChatAgent(
        role=RoleType.ASSISTANT,
        name="Citation Verifier",
        system_message=(
            "You are an academic integrity assistant. Your job is to check whether key claims are supported by citations. "
            "Point out unsupported claims or questionable sources in the text."
        ),
        model_config=ChatGPTConfig(model="gpt-4")
    )


# from camel.agents import ChatAgent
# from camel.typing import RoleType
# from camel.configs import ChatGPTConfig
# from utils.semantic_scholar import search_papers_by_claim


# def get_citation_verifier_agent(paper_text):
#     # Step 1: Extract candidate claims (simple heuristic for now)
#     candidate_claims = []
#     for line in paper_text.split("\n"):
#         if any(kw in line.lower() for kw in ["we propose", "our results show", "we demonstrate", "this paper shows"]):
#             candidate_claims.append(line.strip())

#     # Step 2: Search Semantic Scholar for each claim
#     citations_found = []
#     for claim in candidate_claims:
#         results = search_papers_by_claim(claim)
#         top_result = results[0]["title"] if results else "No matching paper found"
#         citations_found.append(f"Claim: {claim}\nTop Support: {top_result}")

#     prompt_addition = "\n\n".join(citations_found)

#     return ChatAgent(
#         role=RoleType.ASSISTANT,
#         name="Citation Verifier",
#         system_message=(
#             "You are an academic integrity agent. Below are claims made in the paper and the top result found via Semantic Scholar.\n\n"
#             f"{prompt_addition}\n\n"
#             "Please identify any claims that lack strong support or have weak citations."
#         ),
#         model_config=ChatGPTConfig(model="gpt-4")
#     )
