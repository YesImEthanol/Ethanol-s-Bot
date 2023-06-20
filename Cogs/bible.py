import discord
import constants
import requests
import json

from discord.ext import commands

class Bible(commands.Cog):
    def __init__ (self, bot):
        self.bot = bot

    @commands.command()
    async def verse_search(self, ctx, version, query):
        url = f"https://api.scripture.api.bible/v1/bibles/{version}/search?q={query}"
        
        headers = {
            "api-key" : "bibleAPIKey"
        }

        response = requests.get(url, headers = headers)
        print(response.status_code)
        print(response.text)

        if response.status_code == 200:
            verse_results = response.json()["data"]

            if verse_results:
                first_verse = verse_results[0]["reference"]
                verse_text = verse_results[0]["content"]

                await ctx.send(f"{first_verse}: {verse_text}")
            else:
                await ctx.send("No Verses Found.")
        else:
            await ctx.send("Failed to retrieve Bible verses.")

    def configLoader(self):
        with open ('config.json', 'r') as f:
            config = json.load(f)
        return config

async def setup(bot):
    await bot.add_cog(Bible(bot))
