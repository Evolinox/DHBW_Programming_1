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

def fetchLine(train):
    if train[1].attrib.get("l") is None:
        return train[0].attrib.get("n")
    else:
        return train[1].attrib.get("l")

def fetchTime(timecode):
    timecode = f"{timecode[6]+timecode[7]}:{timecode[8]+timecode[9]} Uhr"
    return timecode

def fetchPath(train):
    # Base Variables
    arrival = train.find("ar")
    departure = train.find("dp")
    path = []

    # Check, if Train (1) starts here, (2) ends here or (3) has a stop here.
    if arrival is None and departure is not None:
        # Get Terminus
        pathAfter = departure.attrib.get("ppth")
        pathAfter = pathAfter.split("|")
        path.append(pathAfter[len(pathAfter)-1])

    elif arrival is not None and departure is None:
        # Get first Station
        pathBefore = arrival.attrib.get("ppth")
        pathBefore = pathBefore.split("|")
        path.append(pathBefore[0])

    elif arrival is not None and departure is not None:
        # Get first Station
        pathBefore = arrival.attrib.get("ppth")
        pathBefore = pathBefore.split("|")
        path.append(pathBefore[0])

        # Get Terminus
        pathAfter = departure.attrib.get("ppth")
        pathAfter = pathAfter.split("|")
        path.append(pathAfter[len(pathAfter)-1])

    # Return the Linepath
    return path

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
        
        infraGoUrl = f"https://apis.deutschebahn.com/db-api-marketplace/apis/timetables/v1/plan/{eva.value}/{date}/{time}"

        headers = {
            "DB-Client-Id": dbApiId,
            "DB-Api-Key": dbApiSecret,
            "accept": "application/xml"
        }
        
        await interaction.response.defer()
        await asyncio.sleep(1)

        response = requests.get(infraGoUrl, headers=headers)
        data = ET.fromstring(response.text)

        timetable = []

        timetable.append(data.get("station"))

        # Wait a second, who are you?!
        await asyncio.sleep(1)

        for s in data:
            for t in s:
                train = [
                    [
                        [s[0].attrib.get("c"), fetchLine(s)],
                        s[1].attrib.get("pp"),
                        fetchTime(s[1].attrib.get("pt"))
                ],
            fetchPath(s[1].attrib.get("ppth")),
            fetchPath(s[2].attrib.get("ppth"))
        ]
        timetable.append(train)

async def setup(bot):
    await bot.add_cog(Infrago(bot))