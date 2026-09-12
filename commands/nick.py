import discord
from discord.ext import commands


class NickCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="nick")
    @commands.has_permissions(manage_nicknames=True)
    async def nick_cmd(self, ctx, member: discord.Member = None, *, nickname=None):
        if member is None:
            return await ctx.send("Uzycie: `!nick <@uzytkownik> <nowy_nickname>`")

        if nickname is None:
            await member.edit(nick=None)
            return await ctx.send(f"✅ Nickname **{member}** zostal zresetowany.")

        await member.edit(nick=nickname)
        await ctx.send(f"✅ Nickname **{member}** zostal zmieniony na **{nickname}**.")


async def setup(bot):
    await bot.add_cog(NickCommand(bot))
