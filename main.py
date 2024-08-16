# GET OUT BOT!!!!!!!!!
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

# Loading Token from env file
load_dotenv()
TOKEN: str = os.getenv('DISCORD_TOKEN')

# 'ge.' will be the prefix W GE-
bot = commands.Bot(command_prefix="ge.", intents=discord.Intents.all())


# Async function to load cogs/extensions
async def load_extensions():
    await bot.load_extension('commands.moderation')
    await bot.load_extension('commands.basic')
    await bot.load_extension('commands.settings')
    await bot.load_extension('commands.admin')


# Run the bot with an event to see in the console W
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    await load_extensions()


# Running bot token
bot.run(TOKEN)
