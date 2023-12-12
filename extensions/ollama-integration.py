import discord

from discord.ext import commands
from discord import app_commands

class Ollama(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("DEBUG: Ollama cog loaded")

    @commands.command()
    async def sync(self, ctx) -> None:
        slashcommandtree = await ctx.bot.tree.sync(guild=ctx.guild)
        await ctx.send(f'Synced {len(slashcommandtree)} commands.')
        print("DEBUG: synced Command Tree")

    @app_commands.command(name = "ask", description = "Ask Llama something")
    async def ask(self, interaction: discord.Interaction, question: str):
        await interaction.response.send_message("you asked me something, but my LLM isnt working at the moment! Your question was: " + question)

async def setup(bot):
    await bot.add_cog(Ollama(bot), guilds = [discord.Object(id=1179106176915480686), discord.Object(id=635480321541931029)])