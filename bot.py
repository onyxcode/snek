import asyncio
import json
import os
import random
import re
import urllib
import urllib.request
from datetime import datetime
from datetime import date
import discord
import wikipedia
from discord.ext import commands



def getSRA(url):
    request = urllib.request.Request(url)
    request.add_header("User-Agent",
                       "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3")
    response = urllib.request.urlopen(request)
    data = response.read().decode("utf-8")

    x = json.loads(data)

    strX = str(x)

    translate1 = strX.translate({ord('['): None})
    translate2 = translate1.translate({ord("'"): None})
    translate3 = translate2.translate({ord(']'): None})
    return translate3


def nameFake(url):
    request = urllib.request.Request(url)
    request.add_header("User-Agent",
                       "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3")
    response = urllib.request.urlopen(request)
    data = response.read().decode("utf-8")
    x = json.loads(data)
    return x["name"]


def get_jsonparsed_data(url):
    response = urllib.request.urlopen(url)
    data = response.read().decode("utf-8")
    x = json.loads(data)
    x = x[0]
    return x["url"]

URLS = {
    "ISS_URL":"https://api.wheretheiss.at/v1/satellites/25544",
    "catURL":"https://api.thecatapi.com/v1/images/search?api_key=42c72953-0684-4728-9cb7-1c07fc9c3e80",
    "dogURL":"https://api.thedogapi.com/v1/images/search?api_key=c7f71bd8-8ad5-4bce-88ba-d11426ce2581",
    "birbURL":"http://shibe.online/api/birds?count=1&urls=true&httpsUrls=true",
    "foxURL":"https://randomfox.ca/floof/",
    "fakeNameURL":"https://api.namefake.com"
}


client = commands.AutoShardedBot(command_prefix="hey ", case_insensitive=True)

music = discord.Game("annoying sounds 24/7")

cogs = {"cogs.CommandErrorHandler",
            "cogs.Music",
            "cogs.Economy",
            "cogs.Fun",
            "cogs.OwnerOnly",
            "cogs.Info",
            "cogs.Moderation",
            "cogs.Polls",
            "cogs.Soundboard",
            "jishaku"
            }

client.remove_command("help")

for cog in cogs:
    try:
        client.load_extension(cog)
    except discord.ext.commands.ExtensionError as error:
        print(f"{cog} could not be loaded. Check the log for more details")
    else:
        print(f"{cog} has been loaded.")


@client.event
async def on_ready():
    print('{0.user} is now online'.format(client))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="SnekBot.me"))


@client.command()
async def stats(ctx):
    """ Shows current statistics of the bot """
    embedVar = discord.Embed(title="Statistics", color=0x95D7AE)
    embedVar.add_field(name="Guilds", value=str(len(client.guilds)), inline=True)
    embedVar.add_field(name="Online Users", value=str(len(client.users)), inline=True)
    embedVar.add_field(name="Channels", value=str(len([i for i in client.get_all_channels()])), inline=False)
    # embedVar.add_field(name="RAM Usage", value=f"{RAMUsage()} MB used of {totalRAM} GB", inline=False)
    await ctx.send(embed=embedVar)


@client.command()
async def say(ctx, *, args):
    """" Copycat! """
    if re.search("@everyone", args) or re.search("@here", args):
        ctx.send("")

    else:
        await ctx.send(args)


@client.command()
async def lul(ctx):
    """ Haha funny """
    await ctx.message.add_reaction("😂")


@client.command()
async def test(ctx):
    """ Testing testing 1 2 3 """
    await ctx.message.add_reaction("<:TedAha:689009497066307640>")
    await ctx.message.add_reaction("1️⃣")
    await ctx.message.add_reaction("2️⃣")


@client.command()
async def dice(ctx):
    """ Randomly rolls 2 dice with 6 sides """
    dice_rolls = 2
    dice_sum = 0
    for i in range(0, dice_rolls):
        roll = random.randint(1, 6)
        dice_sum += roll
    await ctx.send("Rolling...")
    await asyncio.sleep(1.5)
    await ctx.send(f'You rolled 2 dice, with a total of {dice_sum}')


@client.command()
async def invite(ctx):
    """ Join the revolution """
    embedVar = discord.Embed(title="Invite me!", url="https://snekbot.me/invite", color=0xF85A3E)
    await ctx.send(embed=embedVar)



@client.command(pass_context=True)
async def ping(ctx):
    """ Pong! """
    await ctx.message.reply(f"Pong! `{str(round(client.latency * 1000))}ms`")
    print(f"Ping was requested by '{ctx.author}' in '{ctx.guild.name}'.")


@client.command()
async def cc(ctx):
    """ No, this isn't real. NO, you *cannot* buy stuff with it. """
    rand4Digi = random.randint(1000, 9999)
    rand4Digi2 = random.randint(1000, 9999)
    rand4Digi3 = random.randint(1000, 9999)
    rand4Digi4 = random.randint(1000, 9999)
    expiryYear = random.randint(20, 99)
    expiryMonth = random.randint(0o1, 12)
    CVV = random.randint(111, 999)
    embedVar = discord.Embed(title="Here's your fake credit card", color=0x042A2B)
    embedVar.add_field(name="Name", value=f"{nameFake(URLS['fakeNameURL'])}", inline=False)
    embedVar.add_field(name="Number", value=f"{rand4Digi} {rand4Digi2} {rand4Digi3} {rand4Digi4}", inline=True)
    embedVar.add_field(name="CVV", value=f"{CVV}", inline=True)
    embedVar.add_field(name="Expiry Date", value=f"{expiryMonth}/20{expiryYear}", inline=True)
    await ctx.send(embed=embedVar)
    print(f"A (fake) credit card was requested by '{ctx.author}' in '{ctx.guild.name}'.")


@client.command()
async def cat(ctx):
    """ Gets a cute cat photo :3 """
    embedVar = discord.Embed(title="🐈 Do you find this a-meow-sing?", color=0xFDFCFD)
    embedVar.set_image(url=str(get_jsonparsed_data(URLS['catURL'])))
    await ctx.send(embed=embedVar)
    print(f"A cat was requested by '{ctx.author}' in '{ctx.guild.name}'.")


@client.command()
async def dog(ctx):
    """ Gets a random dog photo"""
    embedVar = discord.Embed(title="🐕 This mutt be a cute doggo", color=0x907C6E)
    embedVar.set_image(url=str(get_jsonparsed_data(URLS['dogURL'])))
    await ctx.send(embed=embedVar)
    print(f"A dog was requested by '{ctx.author}' in '{ctx.guild.name}'.")


@client.command()
async def birb(ctx):
    """ Gets a random bird photo """
    embedVar = discord.Embed(title="🐦 Floofy birb", color=0x907C6E)
    embedVar.set_image(url=str(getSRA(URLS['birbURL'])))
    await ctx.send(embed=embedVar)
    print(f"A bird was requested by '{ctx.author}' in '{ctx.guild.name}'.")


@client.command()
async def shove(ctx, member: discord.Member = None):
    """ Feeling upset? Shove somebody. """
    if not member:
        member = None
        await ctx.send(f"**{ctx.author.name} shoved air (I think they're going insane).** *[Give me a valid user!]*")
    elif member == ctx.author:
        await ctx.send("You can't shove yourself. How would that even work?")
    else:
        await ctx.send(f"'Cause when push comes to shove, {ctx.author.name} made {member.name} fall over!")

with open("creds.json") as lock:
    lock = json.load(lock)
client.run(lock["TOKEN"], reconnect=True)

