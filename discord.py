import discord
from discord.ext import commands, tasks
import os
#from keep_alive import keep_alive

token = ""

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='>', intents=intents, description='Developer: @D1STANG3R')

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game('>help'), status=discord.Status.idle) #Status.idle/.dnd/.online
    automessage.start()
    print('Connected to bot: {}'.format(bot.user.name))
    print('Bot ID: {}'.format(bot.user.id))

# https://discord.com/developers/applications > My Application > Bot > SERVER MEMBERS INTENT (on)
@bot.event
async def on_member_join(member):
    #await member.send('Private message') #Private message
    guild = member.guild
    if guild.system_channel is not None:
        to_send = 'Welcome {0.mention} to {1.name}!'.format(member, guild)
        await guild.system_channel.send(to_send)
    
@bot.event
async def on_member_remove(member):
    #await member.send('Private message') #Private message
    guild = member.guild
    if guild.system_channel is not None:
        to_send = 'Bye Bye {0.mention} :('.format(member)
        await guild.system_channel.send(to_send)

@bot.event 
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author.bot: return

    getmessage = str(message.content).lower().strip()
    
    if getmessage == "hello":
        await message.reply('Hello!', mention_author=True)
    if getmessage == "hi":
        await message.reply('Hi!', mention_author=True)

@bot.event
async def on_message_delete(message):
    fmt = '**{0.author}** has deleted the message: {0.content}'
    await message.channel.send(fmt.format(message))

@bot.event
async def on_message_edit(before, after):
    fmt = '**{0.author}** edited their message:\n{0.content} -> {1.content}'
    await before.channel.send(fmt.format(before, after))

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
        
@bot.command()
async def getfile(ctx):
    for attachment in ctx.attachments:
        await attachment.save(attachment.filename) 
  
@bot.command()
async def members(ctx):
    with open("members.txt","a",encoding="UTF-8") as f:
        f.write("--"+str(len(ctx.guild.members))+" people in total--\n")
        for count,user in enumerate(ctx.guild.members):
            f.write(str(count+1)+"-"+str(user)+"\n")
    await ctx.send(file=discord.File("members.txt"))
    os.remove("members.txt")

@tasks.loop(minutes=1)  # minutes=x or hours=x
async def automessage():
    channel = bot.get_channel(807080697852719502)
    await channel.send("Hi")

# keep_alive()
print("Bot is running")
bot.run(token)
