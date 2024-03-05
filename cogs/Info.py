import platform
import discord
from discord.ext import commands
import discord.ext

T = True
F = False


def setup(client):
    client.add_cog(Info(client))


class Info(commands.Cog):
    def __init__(self, client):
        self.client = client
        self._last_member = None

    @commands.command()
    async def help(self, ctx):
        em = discord.Embed(name="Snek", color=0x3ABEFF)
        em.add_field(name="Help",
                     value="Here are some quicklinks.\n[**All Commands**](https://snekbot.me/commands)\n[**Snek Website**](https://snekbot.me/)\n[**Support Server**](https://discord.gg/jUd88az)")
        await ctx.send(f"{ctx.author.mention}, I've sent you a DM containing help info.")
        await ctx.author.send(embed=em)

    @commands.command()
    async def vote(self, ctx):
        """ Vote for the bot! """
        embedVar = discord.Embed(title="Vote for Snek!", color=0xD741A7)
        embedVar.description = """
        • [top.gg](https://top.gg/bot/690747778455830559/vote)
        • [DBL](https://discordbotlist.com/bots/snek/upvote)
        • [botlist.space](https://botlist.space/bot/690747778455830559/upvote)
        • [BFD](https://botsfordiscord.com/bot/690747778455830559/vote)"""
        await ctx.send(embed=embedVar)

    @commands.command()
    async def info(self, ctx):
        em = discord.Embed(color=0x337357)
        the_bot = self.client.get_user(690747778455830559)
        em.add_field(name="Bot Version", value="2021.2", inline=T)
        em.add_field(name="Library", value="discord.py", inline=T)
        em.add_field(name="Python Version", value=platform.python_version(), inline=T)
        em.add_field(name="Servers", value=str(len(self.client.guilds)), inline=T)
        em.add_field(name="Users", value=str(len(self.client.users)), inline=T)
        em.add_field(name="Website", value="[SnekBot.me](https://snekbot.me)", inline=T)
        em.add_field(value="• Knuckles#0002\n• Timanttikuutio#0001", name="Creators", inline=F)
        em.add_field(name="Support Server", value="[discord.gg/jUd88az](https://discord.gg/jUd88az)", inline=T)
        em.add_field(name="Invite", value="[SnekBot.me/invite](https://snekbot.me/invite)", inline=T)
        em.set_author(name="Snek",
                      icon_url=f"{the_bot.avatar_url}")
        await ctx.send(embed=em)
