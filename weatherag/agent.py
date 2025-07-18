from google.adk.agents import Agent
from google.adk.tools.google_search_tool import GoogleSearchTool

# สร้าง agent ที่ใช้ Google Search เป็น grounding แทน weather API
root_agent = Agent(
    model="gemini-2.0-flash",
    name="grounded_weather_agent",
    description="ตอบคำถามสภาพอากาศปัจจุบัน โดยค้นหาข้อมูลจาก Google Search",
    instruction=(
        "You are a weather assistant. "
        "When the user asks about current weather in any city, "
        "use GoogleSearchTool to fetch real-time weather info and cite sources."
    ),
    tools=[GoogleSearchTool()],
)
