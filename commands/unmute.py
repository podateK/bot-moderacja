import discord
from discord.ext import commands


class UnmuteCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="unmute")
    @commands.has_permissions(manage_roles=True)
    async def unmute_cmd(self, ctx, member: discord.Member = None, *, reason=None):
        if member is None:
            return await ctx.send("Uzycie: `!unmute <@uzytkownik> [powod]`")

        muted_role = discord.utils.get(ctx.guild.roles, name="Muted")

        if muted_role is None:
            return await ctx.send("Rola `Muted` nie istnieje na tym serwerze.")

        if muted_role not in member.roles:
            return await ctx.send(f"**{member}** nie jest wyciszony.")

        await member.remove_roles(muted_role, reason=f"Odciszony przez {ctx.author} | {reason or 'Brak powodu'}")

        embed = discord.Embed(
            title="🔊 Odciszono",
            description=f"**{member}** zostal odciszony.",
            color=discord.Color.green(),
        )
        embed.add_field(name="Powod", value=reason or "Brak powodu", inline=False)
        embed.set_footer(text=f"Wykonane przez {ctx.author}", icon_url=ctx.author.display_avatar.url)
        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(UnmuteCommand(bot))
