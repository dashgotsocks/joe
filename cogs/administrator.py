import discord
from discord.ext import commands
from discord.ext.commands import bot
from discord.ext.commands.core import has_permissions
from discord.ext import commands
from discord.ext import flags, commands
from discord.ext.commands.core import has_permissions
from discord.ext import menus
from discord.ext.commands.errors import ExtensionAlreadyLoaded 

class Administrator(commands.Cog):

    def __init__(self, bot):
        bot.client = bot
    

    @commands.Cog.listener()
    async def on_ready(self):
        print("administrator cog loaded...")

    @commands.command()
    async def ping(self, ctx):
        await ctx.send('pong!')

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member:discord.Member):
        await member.ban()
        await ctx.send(f"{member.name} Has been banned!")

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member:discord.Member):
        await member.kick()
        await ctx.send(f"{member.name} Has been kicked!")

    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def purge(self, ctx, limit: int):
        await ctx.channel.purge(limit=limit)
        await ctx.send('Purged by {}'.format(ctx.author.mention))
        await ctx.channel.purge(limit = 1)
        await ctx.delete()

    @purge.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You cant do that!")
    
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def mute(self, ctx, member: discord.Member, *, reason=None):
        guild = ctx.guild
        mutedRole = discord.utils.get(guild.roles, name="Muted")

        if not mutedRole:
            mutedRole = await guild.create_role(name="Muted")

            for channel in guild.channels:
                await channel.set_permissions(mutedRole, send_messages=False)

        await member.add_roles(mutedRole, reason=reason)
        await ctx.send(f"Muted {member.mention} for reason {reason}")
        await member.send(f"you were muted from {guild.name} for {reason}")


    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def unmute(self, ctx, member: discord.Member):
        guild = ctx.guild
        mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

        await member.remove_roles(mutedRole)
        await ctx.send(f"Unmuted{member.mention}")
        await member.send(f"You were unmuted in the server{guild.name}")


    @commands.command()
    async def slowmode(self, ctx, seconds: int):
        await ctx.channel.edit(slowmode_delay=seconds)
        await ctx.send(f"Set the slowmode delay in this channel to {seconds} seconds!")



    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def warn(self, ctx, member: discord.Member):
        await ctx.send(f"{member.mention} has been warned")



    @commands.command(hidden=True)
    @commands.has_permissions(administrator=True)
    async def quit(self, ctx):
	    await ctx.message.add_reaction("👋")
	    await ctx.bot.logout()


    
  
    


    

    


   

def setup(bot): 
    bot.add_cog(Administrator(bot))
        
    






    

