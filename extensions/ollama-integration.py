import discord

from discord.ext import commands
from discord import app_commands

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

class Ollama(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

@tree.command(name = "ask", description = "Ask Llama something", guild=discord.Object(id=1179106176915480686))
async def slash_command(interaction: discord.Interaction):
    await interaction.response.send_message("you asked me something, but my LLM isnt working at the moment!")

async def setup(bot):
    await bot.add_cog(Ollama(bot))