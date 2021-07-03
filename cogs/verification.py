
import discord
from discord.ext import commands
from discord.ext.commands import bot
from discord.ext.commands.core import has_permissions
from discord.ext import commands
from discord.ext import flags, commands
from discord.ext.commands.core import has_permissions
from discord.ext import menus
from discord.ext.commands.errors import ExtensionAlreadyLoaded

 

class Verification(commands.Cog):

    def __init__(self, bot):
        bot.client = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("verification cog loaded.")

    @commands.command()
    async def howtoverify(self, ctx):
        embed=discord.Embed(title=".verify", url="", description="write .verify to access the rest of the server ```.verify```", color=0xFF5733)
        await ctx.send(embed=embed)
        return 
    
    @commands.command()
    async def verify(self, ctx):
        verifyRole = discord.utils.get(ctx.guild.roles, name= "verified")
        if ctx.channel.id == 854366802406801418:
            await ctx.author.add_roles(verifyRole)
            await ctx.send(f"{ctx.author.mention} you are verified")
            await ctx.channel.purge(limit = 2)
            await bot.add_roles(ctx.message.author)
        

    
    
    
                
         
           
        
        
        




        
    

        

   






























def setup(bot): 
    bot.add_cog(Verification(bot))
