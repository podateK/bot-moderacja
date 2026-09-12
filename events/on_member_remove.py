import discord
from discord.ext import commands


class OnMemberRemoveEvent(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        if member.guild.system_channel is None:
            return

        embed = discord.Embed(
            title="👋 Czlonek opuscil serwer",
            description=f"**{member}** opuscil serwer **{member.guild.name}**.",
            color=discord.Color.red(),
        )
        embed.set_thumbnail(url=member.display_avatar.url)
        embed.add_field(name="Pozostali", value=str(member.guild.member_count), inline=True)
        await member.guild.system_channel.send(embed=embed)


async def setup(bot):
    await bot.add_cog(OnMemberRemoveEvent(bot))
