import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix = "<")

  
@client.command()
async def kick(ctx, member : discord.Member , *, reason= None):
    await member.kick(reason=reason)


@client.command()
async def ban(ctx, member : discord.Member , *, reason= None):
    await member.ban(reason=reason)


@client.command()
async def text(ctx, member : discord.Member , *, reason= None):
    await ctx.channel.message("asdasdasdasd")

