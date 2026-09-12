import discord
from discord.ext import commands


class OnMemberUpdateEvent(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        if before.guild is None:
            return
        if before.guild.system_channel is None:
            return

        added_roles = set(after.roles) - set(before.roles)
        removed_roles = set(before.roles) - set(after.roles)

        if added_roles:
            embed = discord.Embed(
                title="🎭 Dodano role",
                description=f"**{before.mention}** otrzymal role: {', '.join(r.mention for r in added_roles)}",
                color=discord.Color.green(),
            )
            embed.set_thumbnail(url=before.display_avatar.url)
            await before.guild.system_channel.send(embed=embed)

        if removed_roles:
            embed = discord.Embed(
                title="🎭 Usunieto role",
                description=f"**{before.mention}** stracil role: {', '.join(r.mention for r in removed_roles)}",
                color=discord.Color.red(),
            )
            embed.set_thumbnail(url=before.display_avatar.url)
            await before.guild.system_channel.send(embed=embed)


async def setup(bot):
    await bot.add_cog(OnMemberUpdateEvent(bot))
