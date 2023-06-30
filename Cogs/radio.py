import os
import discord
import datetime

from discord.ext import commands
from discord import FFmpegPCMAudio
from datetime import datetime

class Radio(commands.Cog):
    
    def __init__ (self, bot):
        self.bot = bot
        self.voice_client = None
    


    @commands.command(aliases = ['Lbc', 'lbc'])
    async def LBC(self, ctx):
        if ctx.author.voice is None:
            await ctx.send("You Must Join A VC!")
            return

        if self.voice_client is not None and self.voice_client.is_connected():
            await self.voice_client.move_to(ctx.author.voice.channel)
        else:
            self.voice_client = await ctx.author.voice.channel.connect()

        if not self.voice_client.is_playing():
            source = discord.FFmpegPCMAudio("https://media-ice.musicradio.com/LBC973MP3Low")
            self.voice_client.play(source)

        await ctx.send("Now Playing: LBC Radio")



    @commands.command(aliases = ['LOFI', 'lofi', 'Lofi'])
    async def LoFi(self, ctx):
        if ctx.author.voice is None:
            await ctx.send("You Must Join A VC!")
            return
        
        if self.voice_client is not None and self.voice_client.is_connected():
            await self.voice_client.move_to(ctx.author.voice.channel)
        else:
            self.voice_client = await ctx.author.voice.channel.connect()

        if not self.voice_client.is_playing():
            source = discord.FFmpegPCMAudio("http://usa9.fastcast4u.com/proxy/jamz?mp=/1")
            self.voice_client.play(source)

        await ctx.send("Now Playing: LoFi Radio")



    @commands.command(aliases = ['Jazz', 'jazz'])
    async def JAZZ(self, ctx):
        if ctx.author.voice is None:
            await ctx.send("You Must Join A VC!")
            return
        
        if self.voice_client is not None and self.voice_client.is_connected():
            await self.voice_client.move_to(ctx.author.voice.channel)
        else:
            self.voice_client = await ctx.author.voice.channel.connect()

        if not self.voice_client.is_playing():
            source = discord.FFmpegPCMAudio("https://stream.zeno.fm/00rt0rdm7k8uv")
            self.voice_client.play(source)

        await ctx.send("Now Playing: Jazz Radio")
    


    @commands.command(aliases = ['Gator', 'gator'])
    async def GATOR(self, ctx):
        if ctx.author.voice is None:
            await ctx.send("You Must Join A VC!")
            return
        
        if self.voice_client is not None and self.voice_client.is_connected():
            await self.voice_client.move_to(ctx.author.voice.channel)
        else:
            self.voice_client = await ctx.author.voice.channel.connect()

        if not self.voice_client.is_playing():
            source = discord.FFmpegPCMAudio("https://24413.live.streamtheworld.com/WWGR_FM.mp3")
            self.voice_client.play(source)

            await ctx.send ("Now Playing: Gator Country 101.9")

    
    
    @commands.command(aliases = ['leave', 'dc'])
    async def disconnect(self, ctx):
        voice = ctx.message.guild.voice_client
        
        await voice.disconnect()
        self.voice_client = None

    @commands.command(aliases = ["Radio", "radio"])
    async def RADIO(self, ctx):
        embed = discord.Embed(title="Ethanol Bot Radio Commands",
                      description="Radio Commands For Ethanol Bot and all of other bots by Ethanol\n\nDM Ethanol With Suggestions for Radio Stations",
                      colour=0xaae43f,
                      timestamp=datetime.now())

        embed.add_field(name="Jazz",
                value="Jazz Radio")
        embed.add_field(name="LoFi",
                value="LoFi Radio")
        embed.add_field(name="Gator",
                value="Gator Country 101.9")
        embed.add_field(name="LBC",
                value="LBC Radio (British Political Radio)")

        embed.set_footer(text="DM Ethanol For Help")

        await ctx.send(embed=embed)
async def setup(bot):
    await bot.add_cog(Radio(bot))
