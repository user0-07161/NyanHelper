import discord
from discord.ext import commands, application_checks
import json
import os
import pathlib
from dotenv import load_dotenv

tagdb = {}
bot = commands.Bot(intents=discord.Intents.all(), command_prefix="ny!")
load_dotenv()

for command in os.listdir(pathlib.PurePath("command")):
    fullpath = pathlib.PurePath("commands", command)
    if os.path.isfile(fullpath):
        with open(fullpath, "r", encoding="utf-8") as script:
            exec(script.read())
@bot.event
async def on_ready():
    await bot.change_presence(activity=nextcord.Game(name=f"Protecting {str(len(bot.guilds))} servers"))
    print(f"Logged in as \"{bot.user}\"")
    
bot.run(os.getenv("TOKEN_DSC"))
    
    
