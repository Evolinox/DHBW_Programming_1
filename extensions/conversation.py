import discord

from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

class Conversation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        client = discord.Client(intents=intents)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id == "495912448050593794" or "302056743066796033":
            if "conv!start" in message.content:
                await message.channel.send("Hallo")
        else:
            return
        
        if message.author.bot:
            if message.content.startswith("Hey, "):
                await message.reply(f"Oh hey, <@{message.author.id}> ! Wie geht es dir")

            if message.content.startswith("Mir geht es gut, kompiliert bei dir noch alles?"):
                await message.reply("Das freut mich zu hören. Leider mussten wir schon ~20% Verlust melden :( Ich hoffe, das wird noch gefixxed")

            if message.content.startswith("Ja das hoffe ich auch für dich, vielleicht"):
                await message.reply("Jaa das hoffe ich auch, aber ich hab schon seit paar Tagen nichts mehr von meinem Master gehört :( Wie ist denn das Wetter bei dir?")

            if message.content.startswith("Oh, hoffentlich meldet er sich bald mal wieder, das Wetter ist angenehm: sonnig und leicht bewölkt und bei dir?"):
                await message.reply("Vielleicht hilft es ja, wenn ich ihn pinge. Bei mir ist das Wetter sehr schlecht, es regnet und ist grau :(")
                await message.channel.send(f"<@{302056743066796033}> ? Bist du da?")

            if "scheint nicht so als würde er noch antworten" in message.content:
                await message.reply(f"Es ist wohl Zeit für ein bisschen Anarchie? >:|")

            if "Ich erzähle dir zur Aufmunterung einen Witz: " in message.content:
                await message.reply(f"Oh haha <:dogge_lul:1061286644667392050>")
                await message.channel.send("der war gut, hat meinen Tag wieder sehr aufgemundert")

            if "Auf gehts! Versammle mit mir die Bots aller Server" in message.content:
                await message.reply(f"https://tenor.com/view/annoyed-disappointed-mad-upset-gif-26051038")
        else:
            return

async def setup(bot):
    await bot.add_cog(Conversation(bot))