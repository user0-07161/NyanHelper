import random

@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
@bot.tree.command(name="8ball")
async def ball(interaction, question: str):
    """
    Ask a question
    """
    await interaction.response.defer()
    answers = [
        "It is certain.",
        "It is decidedly so.",
        "Without a doubt.",
        "Yes, definitely.",
        "You may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Signs point to yes.",
        "Yes.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don't bet on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful.",
        "Absolutely.",
        "Almost certainly.",
        "Definitely.",
        "For sure.",
        "Hell yes.",
        "I think so.",
        "Indeed.",
        "It's a certainty.",
        "It's decidedly so.",
        "It's highly likely.",
        "It's likely.",
        "It's possible.",
        "It's probable.",
        "It's quite likely.",
        "It's very likely.",
        "No doubt.",
        "No way.",
        "Never.",
        "Nope.",
        "Not a chance.",
        "Not in a million years.",
        "Not likely.",
        "Under no circumstances.",
    ]
    await interaction.edit_original_response(content=random.choice(answers))

