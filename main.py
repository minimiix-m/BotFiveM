#SPECTOR PRO
import config
from keepAlive import keep_alive
from logging import getLogger, DEBUG, FileHandler, Formatter
from nextcord import Intents, Status, Streaming
from nextcord.ext import commands
from nextcord.types.interactions import ApplicationCommand

from os import listdir
from asyncio import run
from typing import Dict, Optional

logger = getLogger("nextcord")
logger.setLevel(DEBUG)
handler = FileHandler(filename="log/discord.log", encoding="utf-8", mode="w")
handler.setFormatter(Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s"))
logger.addHandler(handler)

intent = Intents.default()
intent.members = True
React = commands.Bot(
    command_prefix="!",
    case_insensitive=True,
    help_command=None,
    intents=intent,
    strip_after_prefix=True,
)


async def loadcogs():
    for file in listdir("cogs"):
        if file.endswith(".py") and not file.startswith("__COMING__SOON"):
            try:
                React.load_extension(f"cogs.{file[:-3]}")
                print(f"Successfully load {file[:-3]}")
            except Exception as e:
                print(f"Unable to load {file[:-3]} {e}")

@React.event
async def on_connect():
    React.add_startup_application_commands()
    await React.rollout_application_commands()



@React.event
async def on_ready():
    print(f"{React.user}is online")
    await React.change_presence(
        status=Status.idle,
        activity=Streaming(
            name="Check Five M",
            url="",
        ),
    )


keep_alive()

if __name__ == "__main__":
    run(loadcogs())
    React.run(config.Bot_token, reconnect=True)

