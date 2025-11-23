import discord
from discord.ext import commands

# Your discord token that you grab from:
# https://discord.com/developers/applications
# After you created the application, head over to Bot on the right sidetab 
# and select the "reset token" option so you can generate and view your token.
# After that you can simply paste it in here :)
TOKEN = "TOKEN_HERE"

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
   # This is triggered when the bot logs in successfully.

@bot.command()
async def hello(ctx):
    await ctx.send("hello world!")

bot.run(TOKEN)