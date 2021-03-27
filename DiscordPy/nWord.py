import discord 
import asyncio 
from discord.ext import commands


BOT_PREFIX = '*'
bot = commands.Bot(command_prefix=BOT_PREFIX)

@bot.event
async def on_ready():
    print("Logged in as: " + bot.user.name + "\n")

@bot.event
async def on_message(message):
	if message.content.lower() == "nigger":
		await message.delete()

bot.run("NzA4MzIzODY3Njc2MTE1MDE1.Xr2iLQ.2wY5RhbBoooDHrkWvEIpPnMHPS8")
