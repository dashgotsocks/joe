import discord
import random 
import aiohttp
import sys
import asyncio
import hashlib
from discord import message
import requests
import traceback

from discord.ext import commands
from discord.ext.commands import bot
from discord.ext.commands.core import has_permissions
from discord.ext import commands
from discord.ext import flags, commands
from discord.ext.commands.core import has_permissions
from discord.ext import menus
from discord.ext.commands.errors import ExtensionAlreadyLoaded 
from discord.ext.commands import BucketType


from io import BytesIO
from discord.ext import commands



class Funcmds(commands.Cog):



    def __init__(self, bot):
        bot.client = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("funcmds cog loaded...")

#bully command
    @commands.command()
    async def bully(self, ctx, member:discord.Member):
     bully_messages = [
     f'{member.mention} you are a twat ', 
    f'{member.mention} end your life ',
    f'{member.mention} kys kiddy',
    f'{member.mention} you smell like poop ',
    f'{member.mention} die innit ',
    f'{member.mention} no one likes you my guy ',
    f'{member.mention} you have a small peen ',
    
    ]
     await ctx.send(random.choice(bully_messages))

#poll command

    @commands.command()
    async def poll(self, ctx,* ,message):
        embed=discord.Embed(title="Poll!", description=f"{message}")
        message=await ctx.channel.send(embed=embed)
        await message.add_reaction('👍')
        await message.add_reaction('👎')



    @commands.command()
    async def av(self, ctx, user: discord.Member):
        avatar = user.avatar_url_as(static_format='png', size=1024)
        embed = discord.Embed(title="your mentioned avatar!")
        embed.set_image(url=f"{avatar}")
        await ctx.channel.send(embed=embed)


    @commands.command()
    async def sus(self, ctx):
        embed = discord.Embed(title="When the impostor is sus", description="")
        embed.set_image(
            url="https://nyc3.digitaloceanspaces.com/memecreator-cdn/media/__processed__/2da/template-when-the-imposter-is-sus-sus-jerma-1568-0c6db91aec9c.png")


        msg = await ctx.send(embed=embed)

    @commands.command()
    async def coinflip(self, ctx):
        coinflip = ("https://images-na.ssl-images-amazon.com/images/I/81+37SxRZfL._AC_UL600_SR600,600_.png","https://bjc.edc.org/June2017/bjc-r/img/5-algorithms/img_flipping-a-coin/Tails.png")
                    
        coinflip = random.choice(coinflip)
        
        await ctx.send(coinflip)


   
    @commands.command()
    async def rpsi(self, ctx):
        await ctx.send("")

    @commands.command()
    async def cat(self, ctx):
        """Shows a random cat"""
        # Watch Nero spam this command until the bot crashes
        await ctx.channel.trigger_typing()
        cat = requests.get("https://api.thecatapi.com/v1/images/search",)
        url = cat.json()[0]["url"]
        await ctx.send(url)

    @commands.command()
    async def rolldice(self, ctx):
        """Roll some die"""
        await ctx.send("You rolled a {}!".format(random.randint(1, 6)))
    
    @commands.command()
    async def dog(self, ctx):
        """Shows a random dog"""
        # Watch Nero spam this command until the bot crashes
        await ctx.channel.trigger_typing()
        dog = requests.get("https://api.thedogapi.com/v1/images/search",)
        url = dog.json()[0]["url"]
        await ctx.send(url)
    

    
    

    

    @commands.command()
    async def whois(self, ctx):
	    "Shows the nick, global name, and user id of @mentioned users."
	    mentions = ctx.message.mentions
	    if mentions:
		    await ctx.send('\n'.join("{0} is {0} on this server, {1} globally, and has id {2}.".format(
				member.nick or member.name, member.name + "#" + member.discriminator, member.id)
				for member in mentions)
		)
	    else:
		    await ctx.message.add_reaction("⚠")
		    await ctx.send("Who is ... who?")


    @commands.command(aliases=['8ball'])
    async def eightballs(self, ctx, *, question):
        responses = [
        'Hell no.',
        'Prolly not.',
        'Idk bro.',
        'Prolly.',
        'Hell yeah my dude.',
        'It is certain.',
        'It is decidedly so.',
        'Without a Doubt.',
        'Yes - Definitaly.',
        'You may rely on it.',
        'As i see it, Yes.',
        'Most Likely.',
        'Outlook Good.',
        'Yes!',
        'No!',
        'Signs a point to Yes!',
        'Reply Hazy, Try again.',
        'Better not tell you know.',
        'Cannot predict now.',
        'Concentrate and ask again.',
        "Don't Count on it.",
        'My reply is No.',
        'My sources say No.',
        'Outlook not so good.',
        'Very Doubtful']

        await ctx.send(f' question: {question}\n :8ball: Answer: {random.choice(responses)}')

    
        


    
            




def setup(bot): 
    bot.add_cog(Funcmds(bot))
