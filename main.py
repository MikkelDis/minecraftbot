import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import subprocess

load_dotenv()
token = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_message(message):
    if message.author == bot.user:\
        return
    await bot.process_commands(message)

@bot.command()
async def server_status(ctx):
    result = subprocess.run(["sudo", "systemctl", "is-active", "minecraft"], capture_output=True)
    print(result.stdout)

bot.run(token)