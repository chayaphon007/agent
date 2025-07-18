from google.adk.agents import Agent

# 🧠 กำหนดเลขที่ให้ผู้ใช้เดา
SECRET_NUMBER = 73

def check_guess(guess: int) -> str:
    """
    รับค่าที่ผู้ใช้เดา แล้วตอบกลับว่า ต่ำไป สูงไป หรือถูกต้อง
    """
    if guess < SECRET_NUMBER:
        return "Too low"
    elif guess > SECRET_NUMBER:
        return "Too high"
    else:
        return "You guessed correctly"

# 🕹️ สร้าง agent สำหรับเกมทายเลข
root_agent = Agent(
    model='gemini-2.0-flash',
    name='guess_the_number_agent',
    description='Play a number guessing game. Replies with hints based on your guess.',
    instruction=(
        "You are a game master. Your job is to play a number guessing game with the user. "
        "When the user gives you a number between 1 and 100, call the check_guess() function "
        "and respond with the result."
    ),
    tools=[check_guess],
)