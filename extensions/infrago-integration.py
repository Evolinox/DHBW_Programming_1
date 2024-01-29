import discord
import requests
import json
import asyncio
import textwrap

from discord.ext import commands
from discord import app_commands
import xml.etree.ElementTree as ET

# Lies die API Daten aus der Textdatei
with open('token.txt') as file:
    textfile = file.readlines()
    dbApiId = ""
    dbApiSecret = ""

class Infrago(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("DEBUG: Infrago cog loaded")

    # Slashbefehl um die Frage einzugeben und an Ollama lokal zu senden
    @app_commands.command(name = "timetable", description = "Get arrivals and departures from a Station")
    @app_commands.describe(eva = "Station Number")
    @app_commands.choices(eva = [
        discord.app_commands.Choice(name="Mosbach (Baden)", value="8004094"),
        discord.app_commands.Choice(name="Mosbach-Neckarelz", value="8000264"),
        discord.app_commands.Choice(name="Bad Friedrichshall", value="8000017"),
        discord.app_commands.Choice(name="Heilbronn Hauptbahnhof", value="8000157"),
        discord.app_commands.Choice(name="Osterburken", value="8000295"),
        discord.app_commands.Choice(name="Eberbach", value="8000369")
    ])
    async def infra(self, interaction: discord.Interaction, eva: discord.app_commands.Choice[str], date: str, time: str):

async def setup(bot):
    await bot.add_cog(Infrago(bot))