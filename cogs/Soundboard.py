import asyncio

import discord
import discord.ext
from discord.ext import commands


def setup(client):
    client.add_cog(Soundboard(client))


class Soundboard(commands.Cog):
    def __init__(self, client):
        self.client = client
        self._last_member = None

    @commands.command(pass_context=True)
    async def oof(self, ctx):
        """ I'm dead """
        vc = await ctx.author.voice.channel.connect()
        server = ctx.message.guild.voice_client
        await asyncio.sleep(0.25)
        vc.play(discord.FFmpegPCMAudio("sounds/oof.mp3"))
        await asyncio.sleep(2)
        await server.disconnect()

    @oof.error
    async def oof_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send("You are not currently in a voice channel! Please join a voice channel first!")

    @commands.command(pass_context=True)
    async def hey(self, ctx):
        """ Hey, listen! """
        vc = await ctx.author.voice.channel.connect()
        server = ctx.message.guild.voice_client
        await asyncio.sleep(0.25)
        vc.play(discord.FFmpegPCMAudio("sounds/hey_listen.mp3"))
        await asyncio.sleep(2.25)
        await server.disconnect()

    @hey.error
    async def hey_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send("You are not currently in a voice channel! Please join a voice channel first!")

    @commands.command(pass_context=True)
    async def bruh(self, ctx):
        """ BRUH """
        vc = await ctx.author.voice.channel.connect()
        server = ctx.message.guild.voice_client
        await asyncio.sleep(0.25)
        vc.play(discord.FFmpegPCMAudio("sounds/bruh.mp3"))
        await asyncio.sleep(2)
        await server.disconnect()

    @bruh.error
    async def bruh_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send("You are not currently in a voice channel! Please join a voice channel first!")

    @commands.command(pass_context=True)
    async def nope(self, ctx):
        """ Hard pass """
        vc = await ctx.author.voice.channel.connect()
        server = ctx.message.guild.voice_client
        await asyncio.sleep(0.25)
        vc.play(discord.FFmpegPCMAudio("sounds/nope.mp3"))
        await asyncio.sleep(0.75)
        await server.disconnect()

    @nope.error
    async def nope_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send("You are not currently in a voice channel! Please join a voice channel first!")

    @commands.command(pass_context=True)
    async def gamecube(self, ctx):
        """ That was very 2000's of you """
        vc = await ctx.author.voice.channel.connect()
        server = ctx.message.guild.voice_client
        await asyncio.sleep(0.25)
        vc.play(discord.FFmpegPCMAudio("sounds/gamecube_intro.mp3"))
        await asyncio.sleep(7.75)
        await server.disconnect()

    @gamecube.error
    async def gamecube_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send("You are not currently in a voice channel! Please join a voice channel first!")

    @commands.command(pass_context=True)
    async def violin(self, ctx):
        """ Very sad, but also very meme'd """
        vc = await ctx.author.voice.channel.connect()
        server = ctx.message.guild.voice_client
        await asyncio.sleep(0.25)
        vc.play(discord.FFmpegPCMAudio("sounds/sad-violin.mp3"))
        await asyncio.sleep(4.5)
        await server.disconnect()

    @violin.error
    async def violin_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send("You are not currently in a voice channel! Please join a voice channel first!")

    @commands.command(pass_context=True)
    async def fail(self, ctx):
        """ We'll get em' next time """
        vc = await ctx.author.voice.channel.connect()
        server = ctx.message.guild.voice_client
        await asyncio.sleep(0.25)
        vc.play(discord.FFmpegPCMAudio("sounds/mission-failed.mp3"))
        await asyncio.sleep(3.5)
        await server.disconnect()

    @fail.error
    async def fail_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send("You are not currently in a voice channel! Please join a voice channel first!")

    @commands.command(pass_context=True)
    async def sixtysix(self, ctx):
        """ The Senate is hungry """
        vc = await ctx.author.voice.channel.connect()
        server = ctx.message.guild.voice_client
        await asyncio.sleep(0.25)
        vc.play(discord.FFmpegPCMAudio("sounds/order66.mp3"))
        await asyncio.sleep(4.25)
        await server.disconnect()

    @sixtysix.error
    async def sixtysix_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send("You are not currently in a voice channel! Please join a voice channel first!")

    @commands.command(pass_context=True)
    async def notif(self, ctx):
        """ Ghost ping! """
        vc = await ctx.author.voice.channel.connect()
        server = ctx.message.guild.voice_client
        await asyncio.sleep(0.25)
        vc.play(discord.FFmpegPCMAudio("sounds/discord-notification.mp3"))
        await asyncio.sleep(1)
        await server.disconnect()

    @notif.error
    async def notif_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send("You are not currently in a voice channel! Please join a voice channel first!")

    @commands.command(pass_context=True)
    async def deez(self, ctx):
        """ Gotem """
        vc = await ctx.author.voice.channel.connect()
        server = ctx.message.guild.voice_client
        await asyncio.sleep(0.25)
        vc.play(discord.FFmpegPCMAudio("sounds/deez-nuts.mp3"))
        await asyncio.sleep(7.75)
        await server.disconnect()

    @deez.error
    async def deez_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send("You are not currently in a voice channel! Please join a voice channel first!")

    @commands.command(pass_context=True)
    async def drums(self, ctx):
        """ Kinda stupid but hey, it still gets the point across """
        vc = await ctx.author.voice.channel.connect()
        server = ctx.message.guild.voice_client
        await asyncio.sleep(0.25)
        vc.play(discord.FFmpegPCMAudio("sounds/ba-dum-tiss.mp3"))
        await asyncio.sleep(3.25)
        await server.disconnect()

    @drums.error
    async def drums_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send("You are not currently in a voice channel! Please join a voice channel first!")

    @commands.command()
    async def saber(self, ctx):
        await ctx.send("<a:peepo_beat_saber:698737381737627710> Pew pew. Wait...")

    @commands.command(pass_context=True)
    async def yeet(self, ctx):
        """ *Throws unidentified object* """
        vc = await ctx.author.voice.channel.connect()
        server = ctx.message.guild.voice_client
        await asyncio.sleep(0.25)
        vc.play(discord.FFmpegPCMAudio("sounds/yeet.mp3"))
        await asyncio.sleep(1.5)
        await server.disconnect()

    @yeet.error
    async def yeet_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send("You are not currently in a voice channel! Please join a voice channel first!")

    @commands.command(pass_context=True)
    async def mch(self, ctx):
        """ I'm dead but Minecraft """
        vc = await ctx.author.voice.channel.connect()
        server = ctx.message.guild.voice_client
        await asyncio.sleep(0.25)
        vc.play(discord.FFmpegPCMAudio("sounds/classic_hurt.mp3"))
        await asyncio.sleep(1.5)
        await server.disconnect()

    @mch.error
    async def mch_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send("You are not currently in a voice channel! Please join a voice channel first!")

    @commands.command(pass_context=True)
    async def wxp(self, ctx):
        """Task failed successfully """
        vc = await ctx.author.voice.channel.connect()
        server = ctx.message.guild.voice_client
        await asyncio.sleep(0.25)
        vc.play(discord.FFmpegPCMAudio("sounds/erro.mp3"))
        await asyncio.sleep(1.5)
        await server.disconnect()

    @wxp.error
    async def wxp_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send("You are not currently in a voice channel! Please join a voice channel first!")

    @commands.command(pass_context=True)
    async def nine(self, ctx):
        """ It's over 9000 """
        vc = await ctx.author.voice.channel.connect()
        server = ctx.message.guild.voice_client
        await asyncio.sleep(0.25)
        vc.play(discord.FFmpegPCMAudio("sounds/over9000.swf.mp3"))
        await asyncio.sleep(3.75)
        await server.disconnect()

    @nine.error
    async def nine_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send("You are not currently in a voice channel! Please join a voice channel first!")

    @commands.command(pass_context=True)
    async def succ(self, ctx):
        vc = await ctx.author.voice.channel.connect()
        server = ctx.message.guild.voice_client
        await asyncio.sleep(0.25)
        vc.play(discord.FFmpegPCMAudio("sounds/succ.mp3"))
        await asyncio.sleep(3.25)
        await server.disconnect()

    @succ.error
    async def succ_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send("You are not currently in a voice channel! Please join a voice channel first!")

    @commands.command(pass_context=True)
    async def shrek(self, ctx):
        """ EXPLAIN YOURSELF """
        vc = await ctx.author.voice.channel.connect()
        server = ctx.message.guild.voice_client
        await asyncio.sleep(0.25)
        vc.play(discord.FFmpegPCMAudio("sounds/what-are-you-doing-in-my-swamp-.mp3"))
        await asyncio.sleep(4.5)
        await server.disconnect()

    @shrek.error
    async def shrek_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send("You are not currently in a voice channel! Please join a voice channel first!")

    @commands.command(pass_context=True)
    async def lose(self, ctx):
        """ The opposite of winning """
        vc = await ctx.author.voice.channel.connect()
        server = ctx.message.guild.voice_client
        await asyncio.sleep(0.25)
        vc.play(discord.FFmpegPCMAudio("sounds/the-price-is-right-losing-horn.mp3"))
        await asyncio.sleep(1.5)
        await server.disconnect()

    @lose.error
    async def lose_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send("You are not currently in a voice channel! Please join a voice channel first!")

    @commands.command(pass_context=True)
    async def jeff(self, ctx):
        """ That's his name"""
        vc = await ctx.author.voice.channel.connect()
        server = ctx.message.guild.voice_client
        await asyncio.sleep(0.25)
        vc.play(discord.FFmpegPCMAudio("sounds/ringtone_20.mp3"))
        await asyncio.sleep(2.75)
        await server.disconnect()

    @jeff.error
    async def jeff_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send("You are not currently in a voice channel! Please join a voice channel first!")

    @commands.command(pass_context=True)
    async def fart(self, ctx):
        """ Somebody cut the cheese """
        vc = await ctx.author.voice.channel.connect()
        server = ctx.message.guild.voice_client
        await asyncio.sleep(0.25)
        vc.play(discord.FFmpegPCMAudio("sounds/perfect-fart.mp3"))
        await asyncio.sleep(1)
        await server.disconnect()

    @fart.error
    async def fart_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send("You are not currently in a voice channel! Please join a voice channel first!")

    @commands.command(pass_context=True)
    async def airhorn(self, ctx):
        """ The MLG one """
        vc = await ctx.author.voice.channel.connect()
        server = ctx.message.guild.voice_client
        await asyncio.sleep(0.25)
        vc.play(discord.FFmpegPCMAudio("sounds/mlg-airhorn.mp3"))
        await asyncio.sleep(3.5)
        await server.disconnect()

    @airhorn.error
    async def airhorn_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send("You are not currently in a voice channel! Please join a voice channel first!")

    @commands.command(pass_context=True)
    async def inception(self, ctx):
        """ Skeppy intro noise """
        vc = await ctx.author.voice.channel.connect()
        server = ctx.message.guild.voice_client
        await asyncio.sleep(0.25)
        vc.play(discord.FFmpegPCMAudio("sounds/inceptionbutton.mp3"))
        await asyncio.sleep(4)
        await server.disconnect()

    @inception.error
    async def inception_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send("You are not currently in a voice channel! Please join a voice channel first!")

    @commands.command(pass_context=True)
    async def stop(self, ctx):
        """ Disconnects the bot from your channel """
        server = ctx.message.guild.voice_client
        await server.disconnect()