import discord

from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

class Scotland(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        client = discord.Client(intents=intents)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        elif "scotland" in message.content.lower():
            await message.reply("https://media.tenor.com/FGME0yGf0QcAAAAM/scotland-forever.gif")

async def setup(bot):
    await bot.add_cog(Scotland(bot))