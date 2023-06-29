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
    print (f'Successfully Loaded All Cogs!')

# Config Loader
def configLoader():
    with open ('config.json', 'r') as f:
        config = json.load(f)
    return config

if __name__ == "__main__":
    config = configLoader()
    discordToken = config[constants.DISCORD_TOKEN]

bot.run(discordToken)
