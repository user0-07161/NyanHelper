import requests

@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
@bot.tree.command(name="askidk")
async def askidk(interaction, question: str):
    """
    Ask a question to Dunno AI
    """
    await interaction.response.defer()
    data = {
        "text": question,
    }
    response = requests.get(f"{idkai}question")
    if response.status_code == 200:
        embed = discord.Embed(title="Dunno AI's response")
        embed.add_field(name="Prompt", value=question)
        embed.add_field(name="Response", value=response.json()['response'])
    else:
        embed = discord.Embed(title="Error")
        embed.add_field(name="Status code", value=response.status_code)
    await interaction.edit_original_response(embed=embed)
