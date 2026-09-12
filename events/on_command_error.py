import discord
from discord.ext import commands


class OnCommandErrorEvent(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            missing = ", ".join(error.missing_permissions)
            await ctx.send(f"❌ Brak uprawnien. Potrzebne: `{missing}`")

        elif isinstance(error, commands.BotMissingPermissions):
            missing = ", ".join(error.missing_permissions)
            await ctx.send(f"❌ Bot nie ma uprawnien: `{missing}`")

        elif isinstance(error, commands.MemberNotFound):
            await ctx.send("❌ Nie znaleziono uzytkownika.")

        elif isinstance(error, commands.UserNotFound):
            await ctx.send("❌ Nie znaleziono uzytkownika.")

        elif isinstance(error, commands.ChannelNotFound):
            await ctx.send("❌ Nie znaleziono kanalu.")

        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"❌ Brakujacy argument: `{error.param.name}`")

        elif isinstance(error, commands.BadArgument):
            await ctx.send("❌ Nieprawidlowy argument.")

        elif isinstance(error, commands.CommandNotFound):
            return

        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"⏳ Komenda na cooldownie. Sprobuj za {error.retry_after:.1f}s")

        else:
            await ctx.send(f"❌ Wystapil nieoczekiwany blad: {error}")
            raise error


async def setup(bot):
    await bot.add_cog(OnCommandErrorEvent(bot))
