import discord
from discord.ext import commands


class KickCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="kick")
    @commands.has_permissions(kick_members=True)
    async def kick_cmd(self, ctx, member: discord.Member = None, *, reason=None):
        if member is None:
            return await ctx.send("Uzycie: `!kick <@uzytkownik> [powod]`")

        if member.id == ctx.author.id:
            return await ctx.send("Nie mozesz siebie wykopac.")

        if member.top_role >= ctx.author.top_role:
            return await ctx.send("Nie mozesz wykopac kogos z wyzsza lub rowna role.")

        if not member.kickable:
            return await ctx.send("Nie moge wykopac tego uzytkownika (brak uprawnien).")

        await member.kick(reason=f"Wykopany przez {ctx.author} | {reason or 'Brak powodu'}")

        embed = discord.Embed(
            title="👢 Wykopano",
            description=f"**{member}** zostal wykopany z serwera.",
            color=discord.Color.orange(),
        )
        embed.add_field(name="Powod", value=reason or "Brak powodu", inline=False)
        embed.set_footer(text=f"Wykonane przez {ctx.author}", icon_url=ctx.author.display_avatar.url)
        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(KickCommand(bot))
