import requests

@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
@bot.tree.command(name="ask")
async def ask(interaction, question: str):
    """
    Ask a question to N.A.V.I.A.C.
    """
    await interaction.response.defer()
    data = {
        "text": question,
    }
    response = requests.put(nav['url'], json=data, auth=(nav['username'], nav['token']))
    if response.status_code == 200:
        embed = discord.Embed(title="N.A.V.I.A.C.'s response")
        embed.add_field(name="Prompt", value=question)
        embed.add_field(name="Response", value=response.json()['response'])
    else:
        embed = discord.Embed(title="Error")
        embed.add_field(name="Status code", value=response.status_code)
    await interaction.edit_original_response(embed=embed)

