import discord
from discord.ext import commands, tasks
import os

token = ""
bot = commands.Bot(command_prefix='>', description='Developer: @D1STANG3R')

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game('>help'))
    automessage.start()
    print('Connected to bot: {}'.format(bot.user.name))
    print('Bot ID: {}'.format(bot.user.id))

@bot.command()
async def ping(ctx):
    await ctx.send('pong!')

@bot.command()
async def sum(ctx, args1, args2):
    await ctx.send(int(args1)+int(args2))

@bot.command()
async def sendfile(ctx):
    for filename in os.listdir("folder_name"):
        await ctx.send(file=discord.File("folder_name/{}".format(filename)))

@tasks.loop(minutes=1)  # minutes=x or hours=x
async def automessage():
    channel = bot.get_channel(807080697852719502)
    await channel.send("Hi")

# keep_alive()
print("Bot is running")
bot.run(token)

""" 
import datetime
import pytz
fulltime = datetime.datetime.now(pytz.timezone('Europe/Istanbul'))
fulltime = fulltime.strftime("%d.%m.%Y %H:%M:%S")
print(fulltime)
"""
