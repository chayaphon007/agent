from google.adk.agents import Agent
from google.adk.code_executors import BuiltInCodeExecutor

code_agent = Agent(
    name="code_agent",
    model=MODEL,
    description="A coding assistant that can write and debug Python code.",
    instruction="You are a coding assistant. Write and execute python code to solve the user's problem.",
    tools=[BuiltInCodeExecutor()],
    generate_content_config=types.GenerateContentConfig(
        temperature=0.2,
    ),
)