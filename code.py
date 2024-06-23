import discord
from discord.ext import commands
from datetime import timedelta

intents = discord.Intents.all()
intents.members = True
intents.guilds = True

artemis = commands.Bot(command_prefix='+', intents=intents)

@artemis.event
async def on_ready():
    print(f'Logged in as {artemis.user}')
