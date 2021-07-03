import discord
import random 
from discord.ext import commands
from discord.ext.commands import bot
from discord.ext.commands.core import has_permissions
from discord.ext import commands
from discord.ext import flags, commands
from discord.ext.commands.core import has_permissions
from discord.ext import menus
from discord.ext.commands.errors import ExtensionAlreadyLoaded
from discord.ext import commands
from dpymenus import Page, PaginatedMenu 

class menus(commands.Cog):

    def __init__(self, bot):
        bot.client = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("menu cog loaded...")

    
    @commands.command()
    async def help(self, ctx: commands.Context):
        page1 = Page(title='HELP ℹ️', description='this is where you can find help and commands for certain modules')
        page1.add_field(name='press the middle button exit the menu', value='press the arrow keys to turn through pages')

        page2 = Page(title='Moderation Commands 🤖', description='Here are some moderation commands!')
        page2.add_field(name='Ban', value='```.ban <username>```', inline=False)
        page2.add_field(name='Kick', value='```.kick <username>```', inline=False)
        page2.add_field(name='mute', value='```.mute <user>```', inline=False)
        page2.add_field(name='Unmute', value='```.unmute <user>```', inline=False)
        page2.add_field(name='Warn', value='```.warn <user>```', inline=False)
        page2.add_field(name='Purge', value='```.purge <number>```', inline=False)
        page2.add_field(name='Restart', value='```.restart```', inline=False)
        page2.add_field(name='Slowmode', value='```.slowmode <number>```', inline=False)
        



        page3 = Page(title='fun 🎉', description='Here are some fun commands', inline=False)
        page3.add_field(name='Bully', value='```.bully <username>```', inline=False)
        page3.add_field(name='Poll', value='```.poll <text>```', inline=False)
        page3.add_field(name='coinflip', value='```.coinflip```', inline=False)
        page3.add_field(name='sus', value='```.sus```', inline=False)
        page3.add_field(name='cat', value='```.cat```', inline=False)
        page3.add_field(name='dice', value='```.rolldice```', inline=False)
        page3.add_field(name='dog', value='```.dog```', inline=False)
        page3.add_field(name='8ball', value='```.8ball```', inline=False)
        





        page4 = Page(title='music 🎵', description='music commands', inline=False)
        page4.add_field(name='play', value='```.play <song_name>```', inline=False)
        page4.add_field(name='skip', value='```.skip ```', inline=False)
        page4.add_field(name='queue', value='```.queue ```', inline=False)
        page4.add_field(name='dc', value='```.dc ```', inline=False)




        page5 = Page(title='calculator 📒', description='math commands', inline=False)
        page5.add_field(name='add', value='```.mathadd <x> <y>```', inline=False)
        page5.add_field(name='subtract', value='```.mathsub <x> <y> ```', inline=False)
        page5.add_field(name='divide', value='```.mathdiv <x> <y> ```', inline=False)
        page5.add_field(name='square root', value='```.mathsqrt <x> ```', inline=False)
        



        menu = PaginatedMenu(ctx)
        menu.add_pages([page1, page2, page3, page4, page5])
        await menu.open()
   


    











def setup(bot): 
    bot.add_cog(menus(bot))
