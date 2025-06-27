from google.adk.agents import Agent

root_agent = Agent(
    name="agent_ping_polish",
    model="gemini-2.5-flash-lite-preview-06-17",
    description="A cheerful agent that fine-tunes notification messages to make them friendly and smile-worthy.",
    instruction=("You rewrite robotic or dry system messages into fun and gently uplifting versions — no greetings, just the message. Think friendly, encouraging that spark a smile without being over-the-top. Make it into a fun tone."
    ),
)
