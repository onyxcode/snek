import discord
import random
from discord.ext import commands


class Fun(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def randombee(self, ctx):
        f = open("assets/bee-movie.txt")
        quotes = f.readlines()
        last = len(quotes)
        rnd = random.randint(0, last)
        embed = discord.Embed(name="randombee", color=0xFFF00F)
        embed.description = f"`{quotes[rnd]}`"
        embed.set_footer(text="randombee: Providing you random lines from the Bee Movie.")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Fun(bot))
