import discord
from discord.ext import commands
import discord.ext
import json
import pymongo
import math
import random
import asyncio

T = True
F = False


def setup(client):
    client.add_cog(Economy(client))


def com_ize(num):
    return "{:,}".format(num)


with open("creds.json") as creds:
    creds = json.load(creds)
mc = pymongo.MongoClient(creds["MONGO_URI"])


def open_account(user: discord.Member, o_bal: int = None):
    db = mc.users
    if not o_bal:
        o_bal = 1000
        db[f"{user.id}"].insert_one({"_id": "balance",
                                     "wallet": o_bal,
                                     "bank": 0
                                     })
    else:
        db[f"{user.id}"].insert_one({"_id": "balance",
                                     "wallet": o_bal,
                                     "bank": 0
                                     })


class Economy(commands.Cog):
    def __init__(self, client):
        self.client = client
        self._last_member = None

    @commands.command(aliases=['balance'])
    async def bal(self, ctx, user: discord.Member = None):
        if not user:
            user = ctx.author
        db = mc.users
        col_list = db.list_collection_names()
        em = discord.Embed(name=f"{user.name}'s Balance", color=0x3ABEFF)
        em.set_author(name=f"Balance of {user.name}#{user.discriminator}", icon_url=user.avatar_url)
        if str(user.id) in col_list:
            usr = db[f"{user.id}"].find_one({"_id": "balance"})
            wallet = usr["wallet"]
            bank = usr["bank"]
            em.description = f"""
**Wallet:** {com_ize(wallet)}
**Bank**: {com_ize(bank)}
**Total:** {com_ize(int(bank + wallet))}"""
            # em.set_footer(text="Buy coins at shop.snekbot.me.")
            await ctx.send(embed=em)
        elif user == ctx.author:
            open_account(ctx.author)
            usr = db[f"{ctx.author.id}"].find_one({"_id": "balance"})
            wallet = usr["wallet"]
            bank = usr["bank"]
            em.description = f"""
            **Wallet:** {com_ize(wallet)}
            **Bank**: {com_ize(bank)}
            **Total:** {com_ize(bank + wallet)}"""
            # em.set_footer(text="shop.snekbot.me")
            await ctx.send(embed=em)
        else:
            await ctx.send("This user has no account yet!")

    @commands.cooldown(rate=1, per=1800)
    @commands.command()
    async def work(self, ctx):
        db = mc.users
        col_list = db.list_collection_names()
        if not str(ctx.author.id) in col_list:
            embed = discord.Embed(name="Oops!", color=0xEE6352)
            embed.description = "You don't have an account yet!\nRun `snek bal` to open one."
            await ctx.send(embed=embed)
        else:
            usr = db[f"{ctx.author.id}"].find_one({"_id": "balance"})
            wallet = usr["wallet"]

            rng = random.randint(1, 100)
            def numcheck(message):
                if message.author.id == ctx.author.id:
                    try:
                        int(message.content)
                    except TypeError:
                        return "NOT_INT"
                    else:
                        if int(message.content) == rng:
                            return "NUM"
                        if not int(message.content) == rng:
                            return "NOT_NUM"


            await ctx.send("I'm thinking of a random number between 1 and 100.")
            response = await self.client.wait_for('message', check=numcheck)
            if numcheck(response) == "NUM":
                em = discord.Embed(name="Job finished!", color=0x3EC300)
                em.description = """**You guessed the number right!**
`500` credits have been deposited in your wallet."""
                db[f"{ctx.author.id}"].update_one({"_id": "balance"},
                                                  {"$set": {"_id": "balance",
                                                            "wallet": int(wallet) + 500,
                                                            "bank": usr['bank']
                                                            }}, True)
                await ctx.send(f"{ctx.author.mention}", embed=em)
            elif numcheck(response) == "NOT_NUM":
                em = discord.Embed(name="Job failed!", color=0xFF1D15)
                em.description = f"""**You guessed the number incorrectly!**
`250` credits have been deposited in your wallet.
The number was {rng}."""
                db[f"{ctx.author.id}"].update_one({"_id": "balance"},
                                                  {"$set": {"_id": "balance",
                                                            "wallet": int(wallet) + 250,
                                                            "bank": usr['bank']
                                                            }}, True)
                await ctx.send(f"{ctx.author.mention}", embed=em)
            elif numcheck(response) == "NOT_INT":
                em = discord.Embed(name="Job failed!", color=0xFF1D15)
                em.description = f"""**That's not a number, silly!**
You get no money.
The number was {rng}."""
                await ctx.send(f"{ctx.author.mention}", embed=em)
    @work.error
    async def work_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send("You have already worked within the last 30 minutes. Come back later.")


    @commands.command(aliases=['st'])
    async def stonks(self, ctx, amt):
        db = mc.users
        col_list = db.list_collection_names()
        usr = db[f"{ctx.author.id}"].find_one({"_id": "balance"})
        wallet = usr["wallet"]
        if amt == "all" or amt == "max":
            amt = int(wallet)
        else:
            amt = int(amt)
        if amt is None:
            await ctx.send("How much stonks are you trying to buy?")
        if int(wallet) == 0:
            await ctx.send(f"You have nothing in your wallet.")
        elif int(amt) > int(wallet):
            await ctx.send(f"You cannot buy that much stonks, you only have `{wallet}` credits available.")
        elif int(amt) <= int(wallet):
            if not str(ctx.author.id) in col_list:
                await ctx.send("You do not have an account yet. Please run `snek bal` to get started.")
            else:
                em = discord.Embed(name="Stonks get!", color=0x2CEAA3)
                def stonks():
                    stonk_market = random.randint(1,2)
                    if stonk_market == 1:
                        return "NOT_STONKS"
                    elif stonk_market == 2:
                        return "STONKS"
                if stonks == "STONKS":
                    stonk_rate = random.randint(1,100)
                    db[f"{ctx.author.id}"].update_one({"_id": "balance"},
                                                  {"$set": {"_id": "balance",
                                                            "wallet": int(wallet) + int(amt*stonk_rate),
                                                            "bank": int(bank)
                                                            }}, True)
                    em.description = f"""**Big stonks!**
Your stonks multiplied by `{stonk_rate}%`.
You sold them for a total of `${amt*stonk_rate}`."""
                    await ctx.send(ctx.author.mention, embed=em)
                if stonks == "NOT_STONKS":
                    db[f"{ctx.author.id}"].update_one({"_id": "balance"},
                                                  {"$set": {"_id": "balance",
                                                            "wallet": int(wallet) - int(amt),
                                                            "bank": int(bank)
                                                            }}, True)
                    em.description = f"""**Not stonks :(**
Your stonks died and you lost {amt}."""
                    await ctx.send(ctx.author.mention, embed=em)

    @commands.command(name="with", aliases=['withdraw'])
    async def withdraw(self, ctx, amt: str = None):
        db = mc.users
        col_list = db.list_collection_names()
        usr = db[f"{ctx.author.id}"].find_one({"_id": "balance"})
        wallet = usr["wallet"]
        bank = usr["bank"]
        if amt == "all" or amt == "max":
            amt = int(bank)
        else:
            amt = int(amt)
        if amt is None:
            await ctx.send("How much are you trying to withdraw?")
        if int(bank) == 0:
            await ctx.send(f"You have nothing in your bank.")
        elif int(amt) > int(bank):
            await ctx.send(f"You cannot withdraw that much, you only have `{bank}` credits available.")
        elif int(amt) <= int(bank):
            if not str(ctx.author.id) in col_list:
                await ctx.send("You do not have an account yet. Please run `snek bal` to get started.")
            else:
                db[f"{ctx.author.id}"].update_one({"_id": "balance"},
                                                  {"$set": {"_id": "balance",
                                                            "wallet": int(wallet + int(amt)),
                                                            "bank": (int(bank) - int(amt))
                                                            }}, True)
                await ctx.send(f"`{amt} credits withdrawn from your bank.`")
        else:
            await ctx.send("I have no idea what happened.\n`0 conditions were met.`")

    @commands.command(name="dep", aliases=['deposit'])
    async def deposit(self, ctx, amt: str = None):
        db = mc.users
        col_list = db.list_collection_names()
        usr = db[f"{ctx.author.id}"].find_one({"_id": "balance"})
        wallet = math.trunc(int(usr["wallet"]))
        bank = math.trunc(int(usr["bank"]))
        if amt == "all" or amt == "max":
            amt = int(wallet)
        else:
            amt = int(amt)
        if not amt:
            await ctx.send("How much are you trying to deposit?")
        elif int(wallet) == 0:
            await ctx.send(f"You have nothing in your wallet.")
        elif int(amt) > int(wallet):
            await ctx.send(f"You cannot deposit that much, you only have `{wallet}` credits available.")
        elif int(amt) <= int(wallet):
            if not str(ctx.author.id) in col_list:
                db[f"{ctx.author.id}"].update_one({"_id": "balance"},
                                                  {"$set": {"_id": "balance",
                                                            "wallet": (int(wallet) - int(amt)),
                                                            "bank": (int(bank) + int(amt))
                                                            }}, True)
                await ctx.send(f"`{amt} credits deposited into your bank.`")

            else:
                db[f"{ctx.author.id}"].update_one({"_id": "balance"},
                                                  {"$set": {"_id": "balance",
                                                            "wallet": (int(wallet) - int(amt)),
                                                            "bank": (int(bank) + int(amt))
                                                            }}, True)
                await ctx.send(f"`{amt} credits deposited into your bank.`")
