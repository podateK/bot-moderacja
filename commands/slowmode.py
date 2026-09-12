import discord
from discord.ext import commands


class SlowmodeCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="slowmode")
    @commands.has_permissions(manage_channels=True)
    async def slowmode_cmd(self, ctx, seconds: int = None):
        if seconds is None:
            return await ctx.send("Uzycie: `!slowmode <sekundy>` (0 aby wylaczyc)")

        if seconds < 0 or seconds > 21600:
            return await ctx.send("Podaj wartosc od 0 do 21600 (6 godzin).")

        await ctx.channel.edit(slowmode_delay=seconds)

        if seconds == 0:
            await ctx.send("✅ Slowmode zostal wylaczony.")
        else:
            await ctx.send(f"✅ Slowmode ustawiony na **{seconds}** sekund.")


async def setup(bot):
    await bot.add_cog(SlowmodeCommand(bot))
