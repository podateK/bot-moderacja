import discord
from discord.ext import commands


class OnReadyEvent(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Zalogowano jako: {self.bot.user} (ID: {self.bot.user.id})")
        print(f"Serwery: {len(self.bot.guilds)}")
        print("Bot jest gotowy!")
        await self.bot.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.watching,
                name=f"{len(self.bot.guilds)} serwerow | !pomoc",
            )
        )


async def setup(bot):
    await bot.add_cog(OnReadyEvent(bot))
