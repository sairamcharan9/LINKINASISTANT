from google.adk.agents import SequentialAgent, LlmAgent

# Agent 1: Draft Writer
writer = LlmAgent(
    name="DraftWriter",
    instruction="Write a short, professional LinkedIn post about AI and Automation trends in 2025.",
    output_key="draft_text"
)

# Agent 2: Reviewer
reviewer = LlmAgent(
    name="Reviewer",
    instruction="Review the LinkedIn post in state key 'draft_text' for clarity, engagement, and factual accuracy. Output the improved post.",
    output_key="final_post"
)

# Sequential pipeline: writer -> reviewer
multi_agent_pipeline = SequentialAgent(
    name="LinkedInMultiAgentPipeline",
    sub_agents=[writer, reviewer]
)

if __name__ == "__main__":
    # Run the pipeline (ADK CLI or web UI can also be used)
    result = multi_agent_pipeline.run({})
    print("Final LinkedIn Post:\n", result.get("final_post"))

