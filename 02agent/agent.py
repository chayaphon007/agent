from google.adk.agents import Agent
from google.adk.code_executors import BuiltInCodeExecutor
from google.genai import types
 
root_agent = Agent(
    name="ag02",
    model="gemini-2.0-flash",
    description="Agent that executes Python and Java codes.",
    instruction=(
        "You are a helpful agent who can:\n"
        "You are a coding assistant. Write and execute:\n"
        "- Execute Python code to generate answers (e.g., Fibonacci or other functions)\n"
        "- Execute Java code for dynamic programming tasks (e.g., creating classes, methods, and running Java programs)\n"
    ),
    generate_content_config=types.GenerateContentConfig(
        temperature=0.2,
    ),
    code_executor=BuiltInCodeExecutor()
)