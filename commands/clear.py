import discord
from discord.ext import commands


class ClearCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="clear")
    @commands.has_permissions(manage_messages=True)
    async def clear_cmd(self, ctx, amount: int = None):
        if amount is None:
            return await ctx.send("Uzycie: `!clear <ilosc>`")

        if amount < 1 or amount > 100:
            return await ctx.send("Podaj liczbe od 1 do 100.")

        deleted = await ctx.channel.purge(limit=amount + 1)

        msg = await ctx.send(f"🗑️ Usunieto **{len(deleted) - 1}** wiadomosci.")
        await msg.delete(delay=3)


async def setup(bot):
    await bot.add_cog(ClearCommand(bot))
