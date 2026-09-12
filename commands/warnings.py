import discord
from discord.ext import commands


class WarningsCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="warnings")
    @commands.has_permissions(manage_roles=True)
    async def warnings_cmd(self, ctx, member: discord.Member = None):
        if member is None:
            return await ctx.send("Uzycie: `!warnings <@uzytkownik>`")

        warn_cog = self.bot.get_cog("WarnCommand")
        if warn_cog is None:
            return await ctx.send("Modul ostrzezen nie jest dostepny.")

        warn_list = warn_cog._get_warnings(ctx.guild.id, member.id)

        if not warn_list:
            return await ctx.send(f"**{member}** nie ma ostrzezen.")

        embed = discord.Embed(
            title=f"⚠️ Ostrzezenia - {member}",
            color=discord.Color.yellow(),
        )

        for i, w in enumerate(warn_list, 1):
            embed.add_field(
                name=f"#{i}",
                value=f"**Powod:** {w['reason']}\n**Przez:** {w['by']}",
                inline=False,
            )

        embed.set_footer(text=f"Lacznie: {len(warn_list)} ostrzezen")
        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(WarningsCommand(bot))
