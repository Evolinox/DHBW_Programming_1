import discord

from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

class Voicechannel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        client = discord.Client(intents=intents)

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, after, before):
        
        # Get current Guild
        guild = member.guild

async def setup(bot):
    await bot.add_cog(Voicechannel(bot))