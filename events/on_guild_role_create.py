import discord
from discord.ext import commands


class OnGuildRoleCreateEvent(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_role_create(self, role):
        if role.guild.system_channel is None:
            return

        embed = discord.Embed(
            title="➕ Utworzono role",
            description=f"Rola {role.mention} zostala utworzona.",
            color=discord.Color.green(),
        )
        embed.add_field(name="Nazwa", value=role.name, inline=True)
        embed.add_field(name="Kolor", value=str(role.color), inline=True)
        embed.add_field(name="Pozycja", value=str(role.position), inline=True)
        await role.guild.system_channel.send(embed=embed)


async def setup(bot):
    await bot.add_cog(OnGuildRoleCreateEvent(bot))
