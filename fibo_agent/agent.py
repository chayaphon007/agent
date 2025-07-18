from google.adk.agents import Agent
 
def fibonacci(n: int) -> int:
    """Return the nth Fibonacci number (0-indexed)."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
 
root_agent = Agent(
    name="fibonacci",
    model="gemini-2.0-flash",
    description="Agent that answers Fibonacci questions, plays a guessing game, uses Google Search, and executes Python code.",
    instruction=(
        "You are a helpful agent who can:\n"
        "- Answer Fibonacci questions (assume '77th number' means F(76) using fibonacci function)\n"
    ),
    tools=[fibonacci]
)