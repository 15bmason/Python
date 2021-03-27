from discord import *

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run('NzA1NTE2NjcwNzQ3Mjc5NDQw.Xqs1_A.sH1UNEpucjZu9vPBTeXu7KxXNAc')
