import discord
import requests
import json

from discord.ext import commands
from discord import app_commands

ollamaUrl = "http://127.0.0.1:11434/api/generate"
llmModel = "llama2"

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

    @app_commands.command(name = "set_llm_model", description = "Set the Model for Llama (Llama 2 | Codellama | Discollama)")
    async def set_llm_model(self, interaction: discord.Interaction, model: str):
        llmModel = model.lower()
        await self.bot.change_presence(activity=discord.Game(name = model))
        await interaction.response.send_message("Changed the LLM Model to: " + model)


    @app_commands.command(name = "ask", description = "Ask Llama something")
    async def ask(self, interaction: discord.Interaction, question: str):
        answer = "The question was: " + question + "\n"
        questionModel = json.dumps({
            "model" : llmModel,
            "prompt" : f"{question}",
            "stream": True
        })
        with requests.post(url=ollamaUrl, data=questionModel, stream=True) as response:
            for line in response.iter_lines():
                if line:
                    answer += json.loads(line)["response"]
        await interaction.response.send_message(answer)

async def setup(bot):
    await bot.add_cog(Ollama(bot), guilds = [discord.Object(id=1179106176915480686), discord.Object(id=635480321541931029)])