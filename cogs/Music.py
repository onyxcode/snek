import platform
import discord
import pafy
from discord.ext import commands
import discord.ext
from bot import client

T = True
F = False


def setup(client):
    client.add_cog(Music(client))


class Music(commands.Cog):
    def __init__(self, bot):
        self.client = client
        self._last_member = None

    @commands.command()
    async def play(self, ctx, url):
        video = pafy.new(url)
        best = video.getbest()
        playurl = best.url
        vc = await ctx.author.voice.channel.connect()
        server = ctx.message.guild.voice_client
        if server is None:
            vc.play(discord.FFmpegPCMAudio(playurl))
        else:
            server.disconnect()
            vc.play(discord.FFmpegPCMAudio(playurl))

    @commands.command()
    async def lofi(self, ctx):
        url = "https://www.youtube.com/watch?v=5qap5aO4i9A"
        video = pafy.new(url)
        best = video.getbest()
        playurl = best.url
        vc = await ctx.author.voice.channel.connect()
        server = ctx.message.guild.voice_client
        if server is None:
            vc.play(discord.FFmpegPCMAudio(playurl))
        else:
            server.disconnect()
            vc.play(discord.FFmpegPCMAudio(playurl))



