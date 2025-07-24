from livekit.agents import (
    Agent,
    AgentSession,
    JobContext,
    RunContext,
    WorkerOptions,
    cli,
    function_tool,
)
from livekit.plugins import groq, silero

from dotenv import load_dotenv

load_dotenv(dotenv_path=".env.local")

@function_tool
async def lookup_weather(
    context: RunContext,
    location: str,
):
    """Used to look up weather information."""

    return {"weather": "sunny", "temperature": 70}


async def entrypoint(ctx: JobContext):
    await ctx.connect()

    agent = Agent(
        instructions="""
            You are a friendly voice assistant built by LiveKit.
            Start every conversation by greeting the user.
            Only use the `lookup_weather` tool if the user specifically asks for weather information.
            Never assume a location or provide weather data without a request.
            """,
        tools=[lookup_weather],
    )
    session = AgentSession(
        vad=silero.VAD.load(),
        # any combination of STT, LLM, TTS, or realtime API can be used
        stt=groq.STT(),  
        llm=groq.LLM(model="llama-3.3-70b-versatile"),
        tts=groq.TTS(model="playai-tts"), 
    )

    await session.start(agent=agent, room=ctx.room)
    await session.generate_reply(instructions="Say hello, then ask the user how their day is going and how you can help.")

if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint))
