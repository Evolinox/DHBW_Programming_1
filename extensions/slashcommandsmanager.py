import discord

from discord.ext import commands

class SlashcommandManager(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("DEBUG: Slashcommand Manager cog loaded")

    # Alle Slashbefehle mit Server synchronisieren
    @commands.command()
    async def sync(self, ctx) -> None:
        slashcommandtree = await ctx.bot.tree.sync()
        await ctx.send(f'Synced {len(slashcommandtree)} commands.')
        print("DEBUG: synced Command Tree")

async def setup(bot):
    await bot.add_cog(SlashcommandManager(bot))