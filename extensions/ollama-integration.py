import discord

from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

class Ollama(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        client = discord.Client(intents=intents)

async def setup(bot):
    await bot.add_cog(Ollama(bot))