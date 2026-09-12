import discord
from discord.ext import commands


class TimeoutCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="timeout")
    @commands.has_permissions(moderate_members=True)
    async def timeout_cmd(self, ctx, member: discord.Member = None, minutes: int = None, *, reason=None):
        if member is None or minutes is None:
            return await ctx.send("Uzycie: `!timeout <@uzytkownik> <minuty> [powod]`")

        if minutes < 1 or minutes > 40320:
            return await ctx.send("Podaj czas od 1 do 40320 minut (28 dni).")

        if member.top_role >= ctx.author.top_role:
            return await ctx.send("Nie mozesz wyciszyc kogos z wyzsza lub rowna role.")

        duration = discord.utils.utcnow() + __import__("datetime").timedelta(minutes=minutes)

        await member.timeout(duration, reason=f"Timeout przez {ctx.author} | {reason or 'Brak powodu'}")

        embed = discord.Embed(
            title="🔇 Timeout",
            description=f"**{member}** zostal wyciszony na **{minutes}** minut.",
            color=discord.Color.greyple(),
        )
        embed.add_field(name="Powod", value=reason or "Brak powodu", inline=False)
        embed.set_footer(text=f"Wykonane przez {ctx.author}", icon_url=ctx.author.display_avatar.url)
        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(TimeoutCommand(bot))
