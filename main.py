# Imports
import discord
import json
import constants
import os

from discord.ext import commands

# Bot setup
intents = discord.Intents().all()
bot = commands.Bot(command_prefix="?", help_command = None, intents = intents)
client = discord.Client(intents = intents)  

# Startup Procedure
@bot.event
async def on_ready():
    await bot.change_presence(status = discord.Status.idle, activity = discord.Game('Nothing, Just Lurking'))
    await bot.load_extension("Cogs.radio")
    print (f'Logged on as {bot.user}!')

# Sends Messages to Terminal
@bot.event
async def on_message(message):
    print (f'Message from {message.author}: {message.content}')
    await bot.process_commands(message)

# "Ping! Pong!" Command
@bot.command()
async def ping(ctx):
     await ctx.send('Pong!')

# Config Loader
def configLoader():
    with open ('config.json', 'r') as f:
        config = json.load(f)
    return config

if __name__ == "__main__":
    config = configLoader()
    discordToken = config[constants.DISCORD_TOKEN]

bot.run(discordToken)
