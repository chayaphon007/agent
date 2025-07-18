import random
from google.adk.agents import Agent
from google.adk.tools import ToolContext

def check_guess(guess: int, tool_context: ToolContext) -> str:
    """
    ตรวจสอบการเดาของผู้เล่น และอัปเดต session state
    """
    state = tool_context.state

    # ถ้ายังไม่มีเลขลับใน state ให้สุ่มและเก็บไว้
    if "secret_number" not in state:
        state["secret_number"] = random.randint(1, 100)
        state["guess_count"] = 0

    secret = state["secret_number"]
    count = state.get("guess_count", 0) + 1
    state["guess_count"] = count

    if count > 10:
        return f"You've used all 10 guesses! The number was {secret}."

    if guess < secret:
        return f"Guess #{count}: Too low"
    elif guess > secret:
        return f"Guess #{count}: Too high"
    else:
        # รีเซ็ตเกมเมื่อทายถูก
        state.pop("secret_number", None)
        state.pop("guess_count", None)
        return f"Guess #{count}: You guessed correctly! 🎉 Starting a new game..."

# 🧠 สร้าง agent ที่ใช้ ToolContext และ session state
root_agent = Agent(
    model="gemini-2.0-flash",
    name="guess_the_number_agent",
    description="Play a number guessing game with memory across turns.",
    instruction=(
        "You are a game master. Think of a secret number between 1 and 100. "
        "When the user guesses a number, call check_guess() to evaluate it. "
        "Remember the secret number and guess count using session state."
    ),
    tools=[check_guess],
)
