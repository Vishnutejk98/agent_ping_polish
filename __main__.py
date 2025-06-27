import logging

import click
import uvicorn

from a2a.server.apps import A2AStarletteApplication
from a2a.server.request_handlers import DefaultRequestHandler
from a2a.server.tasks import InMemoryTaskStore
from a2a.types import (
    AgentCapabilities,
    AgentCard,
    AgentSkill,
)
from agent import root_agent as agent_ping_polish
from agent_executor import ADKAgentExecutor
from dotenv import load_dotenv


load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class MissingAPIKeyError(Exception):
    """Exception for missing API key."""


@click.command()
@click.option("--host", default="localhost")
@click.option("--port", default=10002)
def main(host, port):

    # Agent card (metadata)
    agent_card = AgentCard(
        name=agent_ping_polish.name,
        description=agent_ping_polish.description,
        version="1.0.0",
        url="http://localhost:10002/",
        defaultInputModes=["text", "text/plain"],
        defaultOutputModes=["text", "text/plain"],
        capabilities=AgentCapabilities(streaming=True),
        skills=[
            AgentSkill(
                id="tune_notifications",
                name="Polish Notifications",
                description="Transforms bland or robotic notifications into friendly, positive, and smile-inducing messages.",
                tags=["notifications", "tone", "smile", "friendly"],
                examples=[
                    "Polish this: 'Battery low.'",
                    "Rewrite to sound nicer: 'Your session has expired.'",
                    "Make this friendlier: 'You have been logged out due to inactivity.'",
                    "Cheer this up: 'Upload complete.'",
                    "Lighten the tone: 'Meeting starts in 5 minutes.'",
                ],
            )
        ],
    )

    request_handler = DefaultRequestHandler(
        agent_executor=ADKAgentExecutor(
            agent=agent_ping_polish,
        ),
        task_store=InMemoryTaskStore(),
    )

    server = A2AStarletteApplication(
        agent_card=agent_card, http_handler=request_handler
    )

    uvicorn.run(server.build(), host=host, port=port)


if __name__ == "__main__":
    main()