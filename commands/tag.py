import random
from typing import Literal
import requests
import json 

@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
@bot.tree.command(name="listtags")
async def listtags(interaction):
    """
    List your tags
    """
    await interaction.response.defer()
    try:
        await interaction.edit_original_response(content=", ".join(list(tagdb[str(interaction.user.id)])))
    except:
        await interaction.edit_original_response(content="You don't have any tags.")
        pass

@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
@bot.tree.command(name="settag")
async def settag(interaction, tagname: str, tagvalue: str):
    """
    Set or replace a tag
    """
    await interaction.response.defer()
    try: 
        tagdb[str(interaction.user.id)][tagname] = tagvalue
    except:
        tagdb[str(interaction.user.id)] = {}
        tagdb[str(interaction.user.id)][tagname] = tagvalue
    with open("tagdb.json", "w") as f:
        json.dump(tagdb, f)
    await interaction.edit_original_response(content=":white_check_mark:")
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
@bot.tree.command(name="gettag")
async def gettag(interaction, tagname: str):
    """
    Get a tag
    """
    await interaction.response.defer()
    try:
        await interaction.edit_original_response(content=tagdb[str(interaction.user.id)][tagname])
    except:
        await interaction.edit_original_response(content="That tag does not exist.")
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
@bot.tree.command(name="remtag")
async def settag(interaction, tagname: str):
    """
    Delete a tag
    """
    await interaction.response.defer()
    try:
        del tagdb[str(interaction.user.id)][tagname]
    except Exception as e:
        print(e)
        await interaction.edit_original_response(content=":x: Tag doesn't exist.")
        return
    with open("tagdb.json", "w") as f:
        json.dump(tagdb, f)
    await interaction.edit_original_response(content=":white_check_mark:")

