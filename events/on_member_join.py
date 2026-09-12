import discord
from discord.ext import commands


class OnMemberJoinEvent(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        if member.guild.system_channel is None:
            return

        embed = discord.Embed(
            title="👋 Nowy czlonek!",
            description=f"Witaj na serwerze **{member.guild.name}**, {member.mention}!",
            color=discord.Color.green(),
        )
        embed.set_thumbnail(url=member.display_avatar.url)
        embed.add_field(name="Nr konta", value=member.created_at.strftime("%d.%m.%Y"), inline=True)
        embed.add_field(name="Czlonek nr", value=str(member.guild.member_count), inline=True)
        await member.guild.system_channel.send(embed=embed)


async def setup(bot):
    await bot.add_cog(OnMemberJoinEvent(bot))
