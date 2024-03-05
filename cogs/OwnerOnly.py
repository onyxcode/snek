import discord
import requests
from discord.ext import commands


class OwnerOnly(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.is_owner()
    @commands.command()
    async def restart(self, ctx):
        await ctx.send("Sending API call `Reboot Server` to panel.")
        url = 'https://panel.onyxcode.net/api/client/servers/4ceac58a/power'
        myobj = {'signal': 'restart'}
        requests.post(url, json = myobj, headers = {"Authorization": "Bearer vyRvOeHWlBvcSr9R29k1P7n7bhjXZHPgZMlkZW9jkKB94W7l", "Content-Type": "application/json", "Accept": "application/json"})

def setup(bot):
    bot.add_cog(OwnerOnly(bot))
