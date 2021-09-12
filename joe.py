import discord 
import os
import subprocess
import json
import aiohttp
import asyncio
import random 
import datetime
import sys
import time
import discord, random
import math
from random import choice
from discord.ext import commands
from discord.ext import flags, commands
from discord.ext.commands.core import bot_has_guild_permissions, has_permissions
from discord.ext import menus
from discord.ext.commands.errors import ExtensionAlreadyLoaded











bot = discord.Client()

token = "" 

bot = commands.Bot(command_prefix = ".")


@bot.command()
async def load(ctx, extention):
    bot.load_extension(f'cogs.{extention}')

@bot.command()
async def unload(ctx, extention):
    bot.unload_extension(f'cogs.{extention}')

bot.remove_command('help')

@bot.command()
async def serverinfo(ctx):
    role_count = len(ctx.guild.roles)
    list_of_bots = [bot.mention for bot in ctx.guild.members if bot.bot]
    serverinfoEmbed = discord.Embed(timestamp=ctx.message.created_at, color=ctx.author.color)
    serverinfoEmbed.add_field(name='Name', value=f"{ctx.guild.name}", inline=False)
    serverinfoEmbed.add_field(name='Member Count', value=ctx.guild.member_count, inline=False)
    serverinfoEmbed.add_field(name='Verification level', value=str(ctx.guild.verification_level), inline=False)
    serverinfoEmbed.add_field(name='Highest Role',value=ctx.guild.roles[-2], inline=False)
    serverinfoEmbed.add_field(name='Number of Roles', value=str(role_count), inline=False)
    serverinfoEmbed.add_field(name='Bots', value=', '.join(list_of_bots), inline=False)
    

    
    await ctx.send(embed = serverinfoEmbed)


@bot.command()
@commands.has_permissions(administrator=True)
async def dm(ctx, user_id=None, *, args=None):
    await ctx.message.delete()
    if user_id != None and args != None:
        try:
            target = await bot.fetch_user(user_id)
            await target.send(args)
            em = discord.Embed(description=f"Message sent to User: **{target.name}**")
            await ctx.send(embed=em)

        except:
            em = discord.Embed(description=f"Message Couldn't be sent")
            await ctx.send(embed=em)

    else:
        em = discord.Embed(description=f"Didnt Provide Message or User's ID")
        await ctx.send(embed=em)


    def restart_program():
        python = sys.executable
        os.execl(python, python, * sys.argv)


def restart_bot(): 
  os.execv(sys.executable, ['python'] + sys.argv)

@bot.command(name= 'restart')
async def restart(ctx):
  await ctx.send("Restarting bot...")
  restart_bot()



def sub(x: float, y:float):
    return x - y 

def add(x: float, y: float):
    return x + y 

def div(x: float, y: float):
    return x / y

def rando(x: int, y: int):
    return random.radint(x, y)
 

def sqrt(x: int):
    return math.sqrt(x)


@bot.command()
async def mathadd(ctx, x: float, y: float):
    res = add(x, y)
    await ctx.send(res)


@bot.command()
async def mathsub(ctx, x: float, y: float):
    res = sub(x , y)
    await ctx.send(res)

@bot.command()
async def mathdiv(ctx, x: float, y: float):
    res = div(x, y)
    await ctx.send(res)

@bot.command()
async def mathrandom(ctx, x: int, y: int):
    res = rando(x, y)
    await ctx.send(res)

@bot.command()
async def mathsqrt(ctx, x: int):
    res = sqrt(x)
    await ctx.send(res)
 



for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

extensions = ['cogs.administrator'],['cogs.verification'],['cogs.funcmds'],['cogs.menu'],['cogs.img_manipulation']











    








bot.run(token)
