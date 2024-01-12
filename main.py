import discord
import discord.utils
import os

from discord.ext import commands
from discord import app_commands

# Lies den Token aus der Textdatei
with open('token.txt') as file:
    token = file.readlines()

# Setze die Intents
intents = discord.Intents.all()
intents.message_content = True

# Commands Setup
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

# Command Setup
bot = commands.Bot(command_prefix="ollama!", intents=intents, application_id="823237843685081088")
bot.remove_command("help")

@bot.event
async def on_ready():
    print(f'DEBUG: logged in as {bot.user}')

    # Setze die Aktivität vom Bot für das GUI
    await bot.change_presence(activity=discord.Game(name = "Llama 7B"))

    # Lade Cogs aus dem extensions Ordner
    for filename in os.listdir(os.path.join(os.path.dirname(__file__), './extensions')):
        if filename.endswith('py'):
            await bot.load_extension(f'extensions.{filename[:-3]}')
            print(f'DEBUG: loaded extension: {filename[:-3]}')

@bot.command()
async def leave(ctx, guild_id):
    if ctx.author.id == 302056743066796033:
        await bot.get_guild(int(guild_id)).leave()
        await ctx.send(f"I left: {guild_id}")
    else:
        await ctx.send(f"You are not authorized to use this command :P")

# Bot starten
bot.run(token[0])