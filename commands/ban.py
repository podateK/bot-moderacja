import discord
from discord.ext import commands


class BanCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ban")
    @commands.has_permissions(ban_members=True)
    async def ban_cmd(self, ctx, member: discord.Member = None, *, reason=None):
        if member is None:
            return await ctx.send("Uzycie: `!ban <@uzytkownik> [powod]`")

        if member.id == ctx.author.id:
            return await ctx.send("Nie mozesz siebie zbanowac.")

        if member.top_role >= ctx.author.top_role:
            return await ctx.send("Nie mozesz zbanowac kogos z wyzsza lub rowna role.")

        if not member.bannable:
            return await ctx.send("Nie moge zbanowac tego uzytkownika (brak uprawnien).")

        await member.ban(reason=f"Zbanowany przez {ctx.author} | {reason or 'Brak powodu'}")

        embed = discord.Embed(
            title="🔨 Zbanowano",
            description=f"**{member}** zostal zbanowany z serwera.",
            color=discord.Color.red(),
        )
        embed.add_field(name="Powod", value=reason or "Brak powodu", inline=False)
        embed.set_footer(text=f"Wykonane przez {ctx.author}", icon_url=ctx.author.display_avatar.url)
        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(BanCommand(bot))
