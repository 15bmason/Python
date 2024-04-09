import discord
import asyncio
import datetime
import os
from discord.ext import commands
from discord.utils import get
import youtube_dl

BOT_PREFIX = '+'
bot = commands.Bot(command_prefix=BOT_PREFIX)

@bot.event
async def on_ready():
    print("Logged in as: " + bot.user.name + "\n")

@bot.command(pass_context=True, aliases=['j', 'joi'])
async def join(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
        print(f"The bot has connected to {channel}\n")

    await ctx.send(f"Joined {channel}")

@bot.command(pass_context=True, aliases=['p', 'pla'])
async def play(ctx):
    def play_music():
        song_there = os.path.isfile("cantina.mp3")
        voice = get(bot.voice_clients, guild=ctx.guild)
        voice.play(discord.FFmpegPCMAudio("cantina.mp3"), after=lambda e: play_music())
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 0.07
    play_music()


bot.run('')
