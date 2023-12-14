import discord

from discord.ext import commands
from discord import app_commands

class SlashcommandManager(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("DEBUG: Slashcommand Manager cog loaded")

    # Alle Slashbefehle mit Server synchronisieren
    @commands.command()
    async def sync(self, ctx) -> None:
        slashcommandtree = await ctx.bot.tree.sync(guild=ctx.guild)
        await ctx.send(f'Synced {len(slashcommandtree)} commands.')
        print("DEBUG: synced Command Tree")

async def setup(bot):
    await bot.add_cog(SlashcommandManager(bot), guilds = [discord.Object(id=1179106176915480686), discord.Object(id=635480321541931029)])