import discord
from discord.ext import commands, tasks
from discord.ext.commands.errors import CommandInvokeError, MemberNotFound, MissingPermissions
import os
import json
import random
import asyncio
#from keep_alive import keep_alive

intents = discord.Intents.default()
intents.members = True
intents.presences = True

bot = commands.Bot(command_prefix='>', intents=intents, description='Developer: @D1STANG3R')

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game('>help'), status=discord.Status.idle) #Status.idle/.dnd/.online
    #automessage.start()
    presence.start()
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
    await bot.process_commands(message)

@bot.listen('on_message')
async def on_message_listen(message):
    if message.author.bot: return
    getmessage = str(message.content).lower().strip()
    
    if getmessage == "hello":
        await message.reply('Hello!', mention_author=True)
    if getmessage == "hi":
        await message.reply('Hi!', mention_author=True)
        
    try:
        math = getmessage.replace(",", ".")
        result = eval(math)
        if math != str(result):        
            await message.channel.send(result)
    except:pass
        
    # Direct message
    if str(message.channel.id) == str(908618658488659968):
        channel = bot.get_channel(908373877145608223)
        if message.attachments:
            if os.path.exists("attachments") != True:
                os.mkdir("attachments")
            for attachment in message.attachments:
                await attachment.save("./attachments/"+attachment.filename) 
            for filename in os.listdir("attachments"):
                await channel.send(file=discord.File("attachments/{}".format(filename)))
                os.remove("attachments/{}".format(filename))
        else:
            await channel.send(message.content)
            
    # Answers corresponding to keywords
    with open('talk.json',encoding="UTF-8") as f:
        data = json.load(f)
        for i,value in enumerate(data):
            keywords = data["{}".format(i)]["keywords"]
            if getmessage in keywords:
                response = random.choice(data["{}".format(i)]["answers"])
                async with message.channel.typing():
                    await asyncio.sleep(2)
                await message.reply(response, mention_author=True)
    
@bot.event
async def on_message_delete(message):
    fmt = '**{0.author}** has deleted the message: {0.content}'
    await message.channel.send(fmt.format(message))

@bot.event
async def on_message_edit(before, after):
    fmt = '**{0.author}** edited their message:\n{0.content} -> {1.content}'
    await before.channel.send(fmt.format(before, after))
 
@bot.event
async def on_voice_state_update(member, before, after):
    if not member.bot:  # except bots
        if before.channel is None and after.channel is not None:
            print("Join", member)
        if before.channel is not None and after.channel is None:
            print("Left", member)
        if before.channel is not None and after.channel is not None:
            print("Changed channel", member)

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

@tasks.loop(minutes=1)  # seconds=x minutes=x or hours=x or 
async def automessage():
    channel = bot.get_channel(807080697852719502)
    await channel.send("Hi")
   
currentstatus = ""
@tasks.loop(seconds=1)
async def presence():
    server = bot.get_guild(275962706002051072)
    online = 0
    offline = 0
    dnd = 0
    idle = 0
    numberofmembers = 0
    numberofbot = 0
    numberoftextchannel = 0
    numberofvoicechannel = 0
    numberofvoiceconnect = 0
    for member in server.members:
        if member.bot:
            numberofbot += 1
        else:
            numberofmembers += 1
            if str(member.status) == "online":
                online += 1
            if str(member.status) == "offline":
                offline += 1
            if str(member.status) == "dnd":
                dnd += 1
            if str(member.status) == "idle":
                idle += 1
    for channel in server.text_channels:
        numberoftextchannel += 1
    for channel in server.voice_channels:
        numberofvoicechannel += 1
        if channel.members != []:
            numberofvoiceconnect += len(channel.members)
    message = f"🟢 {online} ⛔ {dnd} 🌙 {idle} ◯ {offline} 👤 {numberofmembers} 🤖 {numberofbot} 🗣 {numberofvoiceconnect} 💬 {numberoftextchannel} 🔊 {numberofvoicechannel}"
    global currentstatus
    if currentstatus != message:
        await bot.change_presence(activity=discord.Game(message), status=discord.Status.dnd)
        currentstatus = message

@bot.command(name="ban", help="command to ban user")
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    if member == ctx.message.author:
        await ctx.reply("You cannot ban yourself")
        return
    banembed = discord.Embed(title=f":boot: Banned {member.name}!", description=f"Reason: {reason}\nBy: {ctx.author.mention}\nFrom: **{ctx.guild}**")
    try: await member.send(embed=banembed)
    except: pass
    await member.ban(reason=reason)
    await ctx.message.delete()
    await ctx.channel.send(embed=banembed)
    
@bot.command()
@commands.has_permissions(administrator=True)
async def unban(ctx, *, member_id: int):
    await ctx.guild.unban(discord.Object(id=member_id))
    await ctx.send(f"Unban {member_id}")

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member, *, reason=None):
    if user == ctx.message.author:
        await ctx.reply("You cannot ban yourself")
        return
    kickembed = discord.Embed(title=f":boot: Kicked {user.name}!", description=f"Reason: {reason}\nBy: {ctx.author.mention}\nFrom: **{ctx.guild}**")
    try: await user.send(embed=kickembed)
    except: pass
    await user.kick(reason=reason)
    await ctx.message.delete()
    await ctx.channel.send(embed=kickembed)
    
@bot.command()
async def kickyourself(ctx):
    await ctx.author.send("https://discord.gg/")
    await ctx.author.kick()
    await ctx.channel.send("{0.mention} kicked itself".format(ctx.author))
    
@bot.command(description="Mutes the specified user.")
@commands.has_permissions(manage_roles=True)
async def mute(ctx, member: discord.Member, *, reason=None):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")
    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")
        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)
    embed = discord.Embed(title=":mute: Muted", description=f"{member.mention} was muted ", colour=discord.Colour.light_gray())
    embed.add_field(name="reason:", value=reason, inline=False)
    await ctx.reply(embed=embed)
    await member.add_roles(mutedRole, reason=reason)
 
@bot.command(description="Unmute the specified user.")
@commands.has_permissions(manage_roles=True)
async def unmute(ctx, member: discord.Member):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")
    embed = discord.Embed(title=":speaker: Unmuted", description=f"{member.mention} was unmuted ", colour=discord.Colour.light_gray())
    await ctx.reply(embed=embed)
    await member.remove_roles(mutedRole)
  
@bot.command(name='clear', help='This command will clear messages')
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount = 1):
    await ctx.channel.purge(limit=amount+1)
  
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.reply("You don't have permission to this")
    if isinstance(error, MemberNotFound):
        await ctx.reply("There is no such person on this server.")
    if isinstance(error, CommandInvokeError):
        await ctx.reply("I do not have authority")
        
@bot.command()
async def avatar(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.author
    filename = f"{member.display_name}.png"
    await member.avatar_url.save(filename)
    file = discord.File(fp=filename)
    await ctx.send(file=file)
    os.remove(filename)
     
@bot.command()
async def invite(ctx, max_age: int = 0, max_uses: int = 0):
    link = await ctx.channel.create_invite(xkcd=True, max_age=max_age, max_uses=max_uses)
    if max_age == 0:
        max_age = "Unlimited"
    if max_uses == 0:
        max_uses = "Unlimited"
    await ctx.channel.send(f"> *Max age:* **{max_age}**\n> *Max uses:* **{max_uses}**\n> {link}")
     
@bot.command()
async def embed(ctx):
    embed = discord.Embed()
    embed.color = discord.Color.dark_red()
    embed.title = "This is a title"
    embed.url = "https://github.com/hulkienesuysal"
    embed.description = f"This is a description\nAuthor: {ctx.author.mention}"
    embed.set_thumbnail(url="https://picsum.photos/200")
    embed.set_author(
        icon_url=ctx.author.avatar_url,
        name=ctx.author.display_name,
        url="https://github.com/hulkienesuysal"
    )
    embed.add_field(
        name="Field 1 Title",
        value="https://github.com/hulkienesuysal",
        inline=False
    )
    embed.add_field(
        name="Field 2 Title",
        value="*It is inline with Field 2*",
        inline=True
    )
    embed.add_field(
        name="Field 3 Title",
        value="***It is inline with Field 3***",
        inline=True
    )
    embed.add_field(
        name="Field 4 Title",
        value=f"```css\n {ctx.author} $48```",
        inline=False
    )
    embed.set_footer(
        icon_url=ctx.guild.icon_url,
        text=ctx.message.guild.name
    )
    await ctx.send(embed=embed)
        
# keep_alive()
print("Bot is running")
token = ""
bot.run(token)
