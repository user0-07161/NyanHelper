@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
@bot.tree.command(name="qr")
async def qr(interaction, string: str):
    """
    Get a QR-Code
    """
    await interaction.response.defer()
    embed = discord.Embed(title="QR code")
    embed.set_image(url=f"""https://api.qrserver.com/v1/create-qr-code/?size=256x256&data={'%20'.join(string.split(' '))}""")
    await interaction.edit_original_response(embed=embed)

