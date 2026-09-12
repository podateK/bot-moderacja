import discord
from discord.ext import commands


class OnVoiceStateUpdateEvent(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if member.guild.system_channel is None:
            return
        if member.bot:
            return

        if before.channel is None and after.channel is not None:
            embed = discord.Embed(
                title="🔊 Dolaczono do kanalu glosowego",
                description=f"**{member.mention}** dolaczyl do {after.channel.mention}",
                color=discord.Color.green(),
            )
            await member.guild.system_channel.send(embed=embed)

        elif before.channel is not None and after.channel is None:
            embed = discord.Embed(
                title="🔇 Opuisciono kanal glosowy",
                description=f"**{member.mention}** opuscil {before.channel.mention}",
                color=discord.Color.red(),
            )
            await member.guild.system_channel.send(embed=embed)

        elif before.channel != after.channel:
            embed = discord.Embed(
                title="🔀 Zmieniono kanal glosowy",
                description=f"**{member.mention}** przeniesl sie z {before.channel.mention} do {after.channel.mention}",
                color=discord.Color.blue(),
            )
            await member.guild.system_channel.send(embed=embed)


async def setup(bot):
    await bot.add_cog(OnVoiceStateUpdateEvent(bot))
