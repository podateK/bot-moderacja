import discord
from discord.ext import commands


class UnbanCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="unban")
    @commands.has_permissions(ban_members=True)
    async def unban_cmd(self, ctx, *, member_name=None):
        if member_name is None:
            return await ctx.send("Uzycie: `!unban <nazwa_uzytkownika>`")

        banned_users = [entry async for entry in ctx.guild.bans()]
        target = None

        for ban_entry in banned_users:
            user = ban_entry.user
            if f"{user.name}#{user.discriminator}" == member_name or user.name == member_name:
                target = user
                break

        if target is None:
            return await ctx.send(f"Nie znaleziono zbanowanego uzytkownika o nazwie: `{member_name}`")

        await ctx.guild.unban(target)

        embed = discord.Embed(
            title="🔓 Odbanowano",
            description=f"**{target}** zostal odbanowany.",
            color=discord.Color.green(),
        )
        embed.set_footer(text=f"Wykonane przez {ctx.author}", icon_url=ctx.author.display_avatar.url)
        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(UnbanCommand(bot))
