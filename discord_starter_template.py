import discord
from discord.ext import commands
from flask import Flask
from threading import Thread
import datetime, pytz
import requests

def GetTime(format=None):
    if format == None:
        format = "%d.%m.%Y - %H:%M:%S"
    fulltime = datetime.datetime.now(pytz.timezone("Europe/Istanbul"))
    fulltime = fulltime.strftime(format)
    return fulltime

# -----------------------------------------

app = Flask("")

@app.route("/")
def home():
    return "Hello. I am alive!"

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()
    
# -----------------------------------------

r = requests.head(url="https://discord.com/api/v1")
try:
    print(f"Rate limit {int(r.headers['Retry-After']) / 60} minutes left")
except:
    print("No rate limit")

# -----------------------------------------

intents = discord.Intents.default()
intents.members = True
intents.presences = True

bot = commands.Bot(command_prefix=".", intents=intents, case_insensitive=True, description="Developer: @D1STANG3R")

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game("Dev"), status=discord.Status.online)
    print("Connected to bot: {}".format(bot.user.name))
    print("Bot ID: {}".format(bot.user.id))


@bot.command(help=">>ping")
async def ping(ctx):
    await ctx.send(f"Pong! In **{round(bot.latency * 1000)}**ms")


@bot.command(help=">>sendmessage @member yourmessage")
@commands.has_permissions(administrator=True)
async def sendmessage(ctx, member: discord.Member, *, message):
    try:
        await member.send(message)
        await ctx.reply(f"The message sent to {member.mention} member.")
    except:
        pass


keep_alive()
bot.run("token")
