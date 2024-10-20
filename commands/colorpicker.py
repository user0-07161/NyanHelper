import random
from typing import Literal
import requests
import json 
import re

@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
@bot.tree.command(name="color")
async def color(interaction, color: str):
    """
    Get a color from a hex value
    """
    await interaction.response.defer()
    colorhex = color.replace("#", "")
    print(colorhex)
    hexval = re.search(r'^(?:[0-9a-fA-F]{3}){1,2}$', colorhex)
    print(hexval)
    if not hexval:
        await interaction.edit_original_response(content="Please input a valid hex vaule.")
        return
    embed = discord.Embed(title="Color Picker")
    embed.set_image(url=f"https://singlecolorimage.com/get/{colorhex}/250x250")
    embed.set_footer(text="Powered by singlecolorimage.com")
    await interaction.edit_original_response(embed=embed)

