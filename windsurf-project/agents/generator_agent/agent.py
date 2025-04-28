# Generator Agent for LinkedIn Post Creation

from google.adk.agents import LlmAgent

def create_generator_agent():
    return LlmAgent(
        name="GeneratorAgent",
        instruction="Generate a LinkedIn post draft based on the provided topic and keywords.",
        output_key="draft_text"
    )
