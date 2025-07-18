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

# ตั้งชื่อตัวแปรว่า agent เพื่อให้ ADK CLI หาเจอ
agent = Agent(
    model='gemini-2.0-flash-001',
    name='fibonacci_agent',
    description='Compute Fibonacci numbers using a built-in Python function.',
    instruction=(
        "You are a mathematics expert. "
        "Whenever asked about the nth Fibonacci number, call the fibonacci() function."
    ),
    tools=[fibonacci],   # ใส่ฟังก์ชันโดยตรง
)