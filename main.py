import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import subprocess
from mcrcon import MCRcon

load_dotenv()
token = os.getenv("DISCORD_TOKEN")
rconpass = os.getenv("MCRCON_PASSWORD")

with MCRcon("127.0.0.1", rconpass, port=25575) as mcr:
    response = mcr.command("list")
    print(response)

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
    result = subprocess.run(["sudo", "systemctl", "is-active", "minecraft"], capture_output=True, text=True)
    if(result.stdout.strip() == "active"):
        await ctx.send("Minecraft serveren kører 🟢")
    else:
        await ctx.send("Minecraft serveren kører ikke 🔴")

@bot.command()
async def start_server(ctx):
    result = subprocess.run(["sudo", "systemctl", "is-active", "minecraft"], capture_output=True, text=True)
    if(result.stdout.strip() == "active"):
        await ctx.send("Minecraft serveren kører allerede")
    else:
        result = subprocess.run(["sudo", "systemctl", "start", "minecraft"], capture_output=True, text=True)
        if result.stdout:
            await ctx.send("Der skete en fejl")
        else:
            await ctx.send("Serveren kører nu 🟢")

@bot.command()
async def stop_server(ctx):
    result = subprocess.run(["sudo", "systemctl", "is-active", "minecraft"], capture_output=True, text=True)
    if (result.stdout.strip() == "active"):
        result = subprocess.run(["sudo", "systemctl", "stop", "minecraft"], capture_output=True, text=True)
        if result.stdout:
            await ctx.send("Der skete en fejl")
        else:
            await ctx.send("Serveren er nu lukket 🔴")
    else:
        await ctx.send("Serveren er allerede lukket 🔴")



bot.run(token)