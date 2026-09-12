import discord
from discord.ext import commands


class OnGuildRoleDeleteEvent(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_role_delete(self, role):
        if role.guild.system_channel is None:
            return

        embed = discord.Embed(
            title="➖ Usunieto role",
            description=f"Rola **{role.name}** zostala usunieta.",
            color=discord.Color.red(),
        )
        embed.add_field(name="Nazwa", value=role.name, inline=True)
        embed.add_field(name="Kolor", value=str(role.color), inline=True)
        await role.guild.system_channel.send(embed=embed)


async def setup(bot):
    await bot.add_cog(OnGuildRoleDeleteEvent(bot))
