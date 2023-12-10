import discord

from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

class Escalator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        client = discord.Client(intents=intents)

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, after, before):

        guild = member.guild

        if not str(guild.id) == 1183077178003443873:
            return
        else:
            print("aihwdoiahwdoiöaw")
            channel_exists = True
            channel_id = 1183077178003443873
            channel_category = 1183077113708945438
            if channel_id and channel_exists == True:
                channel = discord.utils.get(guild.voice_channels, id = int(channel_id))

                for user in channel.members:
                    if user == member:
                        user_name = member.display_name
                        for channelTemp in guild.voice_channels:
                            if channelTemp.name == (user_name + "'s Channel"):
                                await channelTemp.delete()

                        category = discord.utils.get(guild.categories, id=int(channel_category))
                        await guild.create_voice_channel(user_name + "'s Channel", category = category)
                        for channelTemp2 in guild.voice_channels:
                            if channelTemp2.name == (user_name + "'s Channel"):
                                await member.edit(voice_channel = channelTemp2)

            temp = "'s Channel"
            for channels in guild.voice_channels:
                if temp in channels.name:
                    if len(channels.members) == 0:
                        await channels.delete()

async def setup(bot):
    await bot.add_cog(Escalator(bot))