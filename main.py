import time
import json
import datetime
import time
import discord
import discord.utils
import os
import sys

from sys import argv
from discord.ext import commands
from discord.utils import get
from datetime import datetime

# Lies den Token aus der Textdatei
with open('token.txt') as file:
    token = file.readlines()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="f!", intents=intents)
bot.remove_command("help")

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="fahrstuhlmusik"))

    for filename in os.listdir(os.path.join(os.path.dirname(__file__), './escalator')):
        if filename.endswith('py'):
            bot.load_extension(f'escalator.{filename[:-3]}')
            print(f'DEBUG: loaded extension: {filename[:-3]}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('fahrstuhl'):
        await message.channel.send('Ich bin der Fahrstuhl Bot, ich sorge für wunderschöne Musik, während ihr im Fahrstuhl chilled :) (Ich gehöre Pascal, falls es Probleme gibt)')

    if message.content.startswith('Nett hier'):
        await message.channel.send('...aber waren Sie schon mal in Baden-Württemberg?')

bot.run(token[0])