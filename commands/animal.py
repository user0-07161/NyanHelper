import random
from typing import Literal
import requests
import json 

@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
@bot.tree.command(name="animal")
async def animal(interaction, animal: Literal["Dog", "Cat", "Fox"]):
    """
    Get an image of an animal
    """
    await interaction.response.defer()
    if animal == "Fox":
        content = requests.get("https://randomfox.ca/floof").json()['image']
    if animal == "Cat":
        content = f"https://cataas.com/cat/{requests.get("https://cataas.com/cat?json=true").json()['_id']}"
    if animal == "Dog":
        content = requests.get("https://dog.ceo/api/breeds/image/random").json()['message']
    await interaction.edit_original_response(content=content)

