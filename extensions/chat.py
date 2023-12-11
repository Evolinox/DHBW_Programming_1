import discord

from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

class Chat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        client = discord.Client(intents=intents)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id == "823237843685081088":
            return
        
        if "nett hier" in message.content:
            await message.reply("Aber waren Sie schonmal in Baden-Württemberg?")

async def setup(bot):
    await bot.add_cog(Chat(bot))