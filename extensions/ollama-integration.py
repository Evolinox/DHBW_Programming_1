import discord
import requests
import json
import asyncio
import textwrap

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

    # Slashbefehl um das LLM Modell zu ändern
    @app_commands.command(name = "set_llm_model", description = "Set the Model for Llama")
    @app_commands.describe(model = "Change the active LLM Model")
    @app_commands.choices(model = [
        discord.app_commands.Choice(name = "Llama2", value = "llama2"),
        discord.app_commands.Choice(name="Codellama", value="codellama"),
        discord.app_commands.Choice(name="Discollama", value="discollama")
    ])
    async def set_llm_model(self, interaction: discord.Interaction, model: discord.app_commands.Choice[str]):
        # wtf is goin here?
        llmModel = model
        await self.bot.change_presence(activity=discord.Game(name = model))
        await interaction.response.send_message("Changed the LLM Model to: " + model)

    # Slashbefehl um die Frage einzugeben und an Ollama lokal zu senden
    @app_commands.command(name = "prompt", description = "Ask Llama something")
    async def promp(self, interaction: discord.Interaction, question: str):
        answer = ""
        questionModel = json.dumps({
            "model" : llmModel.lower(), # Das LLM Modell, was genutzt werden soll
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

        # Wait a second, who are you?!
        await asyncio.sleep(1)
        
        # String Formatter
        contentLength = int(len(answer)/1000)+1
        splittedAns = textwrap.wrap(answer, 1000, replace_whitespace=False)

        # Embed
        promptEmbed = discord.Embed(title="Llama Prompt Command", description="The parser still needs some work, there might be some stupid formatting going on\n", color=0xe91e63)
        promptEmbed.add_field(name="LLM Model", value=llmModel, inline=True)
        promptEmbed.add_field(name="Prompt", value=question, inline=True)
        promptEmbed.add_field(name="Request", value=f"{len(answer)} characters", inline=True)
        promptEmbed.add_field(name="Answer", value="", inline=False)
        for i in range(contentLength):
            promptEmbed.add_field(name="" ,value=splittedAns[i], inline=False)
        await interaction.followup.send(embed=promptEmbed)

async def setup(bot):
    await bot.add_cog(Ollama(bot))