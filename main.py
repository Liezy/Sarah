from dotenv import load_dotenv
import os

load_dotenv()
import discord
from discord.ext import commands
from keep_alive import keep_alive
from sarah.core import get_sarah_response

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

my_secret = os.environ['DISCORD_TOKEN']


@bot.command()
async def sarah(ctx, *, question):
  response = get_sarah_response(question)
  await ctx.send(response)


keep_alive()
bot.run(my_secret)
