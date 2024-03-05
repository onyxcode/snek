import discord
from datetime import datetime
from random import randint
from discord.ext import commands
import pymongo
import json

def setup(client):
    client.add_cog(Moderation(client))

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Code borrowed from https://github.com/Rapptz/RoboDanny
    class BannedMember(commands.Converter):
        async def convert(self, ctx, argument):
            if argument.isdigit():
                member_id = int(argument, base=10)
                try:
                    return await ctx.guild.fetch_ban(discord.Object(id=member_id))
                except discord.NotFound:
                    raise commands.BadArgument('This member has not been banned before.') from None

            ban_list = await ctx.guild.bans()
            entity = discord.utils.find(lambda u: str(u.user) == argument, ban_list)

            if entity is None:
                raise commands.BadArgument('This member has not been banned before.')
            return entity


    # END

    @commands.has_permissions(ban_members=True)
    @commands.command(pass_context=True)
    async def ban(self, ctx, member: discord.Member = None, *, reason="not specified"):
        """ Bans the specified user. {user} <reason> (Reason is optional) """
        embedVar = discord.Embed(title=f"***{member}*** was banned for **{reason}**.", color=0xEF3E36)
        if not member:
            member = None
            await ctx.send("**Error:** Please provide a valid user!")
            return
        if member.bot == True:
            await member.ban()
            await ctx.send(embed=embedVar)
            print(f"'{member}' was banned from '{ctx.guild.name}' by '{ctx.author}' for '{reason}'.")
        elif member.bot == False:
            await member.send(f"You have been banned from ***{ctx.guild.name}*** for the following reason: **{reason}**.")
            await member.ban()
            await ctx.send(embed=embedVar)
            print(f"'{member}' was banned from '{ctx.guild.name}' by '{ctx.author}' for '{reason}'.")


    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("<:error:736403830916251740> You do not have permission to run this command")


    @commands.has_permissions(ban_members=True)
    @commands.command()
    async def unban(self, ctx, member: BannedMember):
        """ Unbans a member from the server. """
        embedVar = discord.Embed(title=f'Unbanned {member.user}', color=0x99C24D)
        await ctx.guild.unban(member.user)
        await ctx.send(embed=embedVar)
        print(f"'{member}' was unbanned from '{ctx.guild.name}' by '{ctx.author}'.")


    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("<:error:736403830916251740> You do not have permission to run this command")


    @commands.has_permissions(kick_members=True)
    @commands.command(pass_context=True)
    async def kick(self, ctx, member: discord.Member = None):
        """ Kicks the specified user from the server. """
        embedVar = discord.Embed(title=f"***{member}*** was kicked.", color=0xE980FC)
        if not member:
            member = None
            await ctx.send("**Error:** Please provide a valid user!")
            return
        if member.bot == True:
            await member.kick()
            await ctx.send(embed=embedVar)
            print(f"'{member}' was kicked from '{ctx.guild.name}' by '{ctx.author}'.")
        elif member.bot == False:
            await member.send(f"You have been kicked from ***{ctx.guild.name}***.")
            await member.kick()
            await ctx.send(embed=embedVar)
            print(f"'{member}' was kicked from '{ctx.guild.name}' by '{ctx.author}'.")


    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("<:error:736403830916251740> You do not have permission to run this command")


    @commands.command()
    async def whois(self, ctx, member: discord.Member = None):
        if not member:
            member = ctx.author
        embedVar = discord.Embed(title=f"Information for {member}", color=0x826AED)
        roles = [role.mention for role in member.roles]
        roles.reverse()
        roles = ", ".join(roles[:-1])
        if roles == "":
            roles = "No Roles"
        embedVar.add_field(name="User ID", value=str(member.id), inline=True)
        embedVar.set_thumbnail(url=member.avatar_url)
        embedVar.add_field(name="Roles", value=roles, inline=False)
        if member.is_on_mobile() == True:
            embedVar.add_field(name="Is on Mobile", value="Yes", inline=True)
        elif member.is_on_mobile() == False:
            embedVar.add_field(name="Is on Mobile", value="No", inline=True)
        else:
            embedVar.add_field(name="Is on Mobile", value="Unknown", inline=True)
        embedVar.add_field(name="Joined On", value=datetime.strftime(member.joined_at, "%b %d, 20%y at %H:%M"), inline=True)
        embedVar.add_field(name="Account Created", value=datetime.strftime(member.created_at, "%b %d, 20%y at %H:%M"),
                           inline=False)
        await ctx.send(embed=embedVar)
        print(f"Information on '{member}' was requested by '{ctx.author}' in '{ctx.guild.name}'.")


    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, message_count: str = None):
        try:
            message_count = int(message_count) + 1
        except ValueError or message_count == None:
            await ctx.send("This is not a number.")
        else:
            await ctx.channel.purge(limit=message_count)
            await ctx.send(f"`{message_count - 1}` **messages purged in <#{ctx.channel.id}>.**")


#    @commands.command()
#    @commands.has_permissions()
#    async def warn(self, ctx, user: discord.Member = None, *, reason: str):
#        with open("creds.json") as creds:
#            creds = json.load(creds)
#        mc = pymongo.MongoClient(creds["MONGO_URI"])
#        warningsDB = mc['guilds'][f'{user.id}_warnings']
#        warningsDB.insert_one({"_id": "test".join(str(randint(1,999)))})
#        await ctx.send(f"```json\n{warningsDB}\n```")
#