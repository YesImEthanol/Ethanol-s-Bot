import os
import discord
import asyncio
from discord.ext import commands
from discord import FFmpegPCMAudio

class Radio(commands.Cog):
    def __init__ (self, bot):
        self.bot = bot
        self.voice_client = None

    @commands.command()
    async def LBC(self, ctx):
        if ctx.author.voice is None:
            await ctx.send("You Must Join A VC!")
            return

        if self.voice_client is None:
            self.voice_client = await ctx.author.voice.channel.connect()

        if not self.voice_client.is_playing():
            source = discord.FFmpegPCMAudio("https://media-ice.musicradio.com/LBC973MP3Low")
            self.voice_client.play(source)

        await ctx.send("Now Playing: LBC Radio")

    @commands.command()
    async def JAZZ(self, ctx):
        if ctx.author.voice is None:
            await ctx.send("You Must Join A VC!")
            return
        
        if self.voice_client is None:
            self.voice_client = await ctx.author.voice.channel.connect()

        if not self.voice_client.is_playing():
            source = discord.FFmpegPCMAudio("https://prod-3-88-59-28.wostreaming.net/ppm-jazz24mp3-ibc1?session-id=65ed6fab71ee26eb7035e44377c5e967")
            self.voice_client.play(source)

        await ctx.send("Now Playing: Jazz Radio")

    @commands.command()
    async def LOFI(self, ctx):
        if ctx.author.voice is None:
            await ctx.send("You Must Join A VC!")
            return
        
        if self.voice_client is None:
            self.voice_client = await ctx.author.voice.channel.connect()

        if not self.voice_client.is_playing():
            source = discord.FFmpegPCMAudio("http://tun.in/sfz2V")
            self.voice_client.play(source)

            await ctx.send ("Now Playing: Lofi Radio")


async def setup(bot):
    await bot.add_cog(Radio(bot))

