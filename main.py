import discord
import discord.utils
import os

from discord.ext import commands

# Lies den Token aus der Textdatei
with open('token.txt') as file:
    token = file.readlines()

# Setze die Intents
intents = discord.Intents.default()
intents.message_content = True

# Command Setup
bot = commands.Bot(command_prefix="f!", intents=intents)
bot.remove_command("help")

@bot.event
async def on_ready():
    print(f'DEBUG: logged in as {bot.user}')

    # Setze die Aktivität vom Bot für das GUI
    await bot.change_presence(activity=discord.Game(name = "Mistral 7B"))

    # Lade Cogs aus dem extensions Ordner
    for filename in os.listdir(os.path.join(os.path.dirname(__file__), './extensions')):
        if filename.endswith('py'):
            await bot.load_extension(f'extensions.{filename[:-3]}')
            print(f'DEBUG: loaded extension: {filename[:-3]}')

# Bot starten
bot.run(token[0])