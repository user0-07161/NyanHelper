import discord
from discord.ext import commands
from discord import app_commands
import json
import os
import pathlib
from dotenv import load_dotenv

tagdb = {}
bot = commands.Bot(intents=discord.Intents.all(), command_prefix="ny!")
load_dotenv()
try:
    with open("tagdb.json", "r") as f:
        tagdb = json.load(f)
except Exception as e:
    pass

nav = {
    "url": "https://naviac-api.onrender.com/generate-response",
    "username": os.getenv("UNAME_NAV"),
    "token": os.getenv("TOKEN_NAV"),
}
for command in os.listdir(pathlib.PurePath("commands")):
    fullpath = pathlib.PurePath("commands", command)
    if os.path.isfile(fullpath):
        with open(fullpath, "r", encoding="utf-8") as script:
            exec(script.read())
@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"Logged in as \"{bot.user}\"")
    
bot.run(os.getenv("TOKEN_DSC"))
    
    
