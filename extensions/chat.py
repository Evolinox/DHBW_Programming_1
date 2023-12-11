import discord

from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

class Chat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        client = discord.Client(intents=intents)

    @commands.Cog.listener()
    async def on_message(message):
        if message.author.id == "823237843685081088":
            return

        if "fahrstuhl" in message.content:
            await message.channel.send('Ich bin der Fahrstuhl Bot, ich sorge für wunderschöne Musik, während ihr im Fahrstuhl chilled :) (Ich gehöre Pascal, falls es Probleme gibt)')

        if "nett hier" in message.content:
            await message.channel.send('...aber waren Sie schon mal in Baden-Württemberg?')

        if "Hallo Fahrstuhl" in message.content:
            await message.channel.send(f'Hey @{message.author.id}, wie gehts')


async def setup(bot):
    await bot.add_cog(Chat(bot))