import platform
import discord
from discord.ext import commands
import discord.ext

yes = True
no = False


def setup(client):
    client.add_cog(Polls(client))


class Polls(commands.Cog):
    def __init__(self, client):
        self.client = client
        self._last_member = None

    @commands.command()
    async def poll(self, ctx, poll_type: str = None, *, question: str = None):
        if poll_type == "yn":
            emojis = ['<:yes:783492704226508811>', '<:no:783492704352600095>']
            if not question:
                await ctx.send("Please give me a question to make into a poll.")
            else:
                poll = discord.Embed(title="Poll!", color=0x0CF574)
                poll.description = question
                msg = await ctx.send(embed=poll)
                for emoji in emojis:
                    await msg.add_reaction(emoji)
        if poll_type == "abc":
            emojis = ['🇦', '🇧', '🇨']
            if not question:
                await ctx.send("Please give me a question to make into a poll.")
            else:
                poll = discord.Embed(title="Poll!", color=0x0CF574)
                poll.description = question
                msg = await ctx.send(embed=poll)
                for emoji in emojis:
                    await msg.add_reaction(emoji)