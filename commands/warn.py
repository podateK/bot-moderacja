import discord
from discord.ext import commands


class WarnCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.warnings = {}

    def _get_warnings(self, guild_id, user_id):
        return self.warnings.setdefault(str(guild_id), {}).setdefault(str(user_id), [])

    @commands.command(name="warn")
    @commands.has_permissions(manage_roles=True)
    async def warn_cmd(self, ctx, member: discord.Member = None, *, reason=None):
        if member is None:
            return await ctx.send("Uzycie: `!warn <@uzytkownik> [powod]`")

        if member.id == ctx.author.id:
            return await ctx.send("Nie mozesz siebie ostrzec.")

        warn_list = self._get_warnings(ctx.guild.id, member.id)
        warn_list.append({
            "reason": reason or "Brak powodu",
            "by": str(ctx.author),
        })

        embed = discord.Embed(
            title="⚠️ Ostrzezenie",
            description=f"**{member}** zostal ostrzezony.",
            color=discord.Color.yellow(),
        )
        embed.add_field(name="Powod", value=reason or "Brak powodu", inline=False)
        embed.add_field(name="Liczba ostrzezen", value=str(len(warn_list)), inline=False)
        embed.set_footer(text=f"Wykonane przez {ctx.author}", icon_url=ctx.author.display_avatar.url)
        await ctx.send(embed=embed)

        try:
            await member.send(f"Otrzymales ostrzezenie na serwerze **{ctx.guild.name}**: {reason or 'Brak powodu'}")
        except discord.Forbidden:
            pass


async def setup(bot):
    await bot.add_cog(WarnCommand(bot))
