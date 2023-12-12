import discord
import requests
import json
import asyncio

from discord.ext import commands
from discord import app_commands

ollamaUrl = "http://127.0.0.1:11434/api/generate"
llmModel = "llama2"

setLlmModelLocal = "Set LLM Model"

class Ollama(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("DEBUG: Ollama cog loaded")

    # Alle Slashbefehle mit Server synchronisieren
    @commands.command()
    async def sync(self, ctx) -> None:
        slashcommandtree = await ctx.bot.tree.sync(guild=ctx.guild)
        await ctx.send(f'Synced {len(slashcommandtree)} commands.')
        print("DEBUG: synced Command Tree")

    # Slashbefehl um das LLM Modell zu ändern
    @app_commands.command(name = "set_llm_model", description = "Set the Model for Llama (Llama 2 | Codellama | Discollama)")
    async def set_llm_model(self, interaction: discord.Interaction, model: str):
        llmModel = model.lower()
        await self.bot.change_presence(activity=discord.Game(name = model))
        await interaction.response.send_message("Changed the LLM Model to: " + model)

    # Slashbefehl um die Frage einzugeben und an Ollama lokal zu senden
    @app_commands.command(name = "prompt", description = "Ask Llama something")
    async def promp(self, interaction: discord.Interaction, question: str):
        answer = "The question was: " + question + "\n"
        questionModel = json.dumps({
            "model" : llmModel,         # Das LLM Modell, was genutzt werden soll
            "prompt" : question,        # Der Prompt vom User
            "stream": True              # Ob es als Stream ausgegeben werden soll
        })
        
        await interaction.response.defer()
        await asyncio.sleep(1)

        # Code von Leo angepasst :)
        with requests.post(url=ollamaUrl, data=questionModel, stream=True) as response:
            for line in response.iter_lines():
                if line:
                    answer += json.loads(line)["response"]
        
        await asyncio.sleep(1)
        await interaction.followup.send(answer)

async def setup(bot):
    await bot.add_cog(Ollama(bot), guilds = [discord.Object(id=1179106176915480686), discord.Object(id=635480321541931029)])