import discord
from discord.ext import commands


class OnGuildUpdateEvent(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_update(self, before, after):
        if after.system_channel is None:
            return

        changes = []

        if before.name != after.name:
            changes.append(f"**Nazwa:** `{before.name}` -> `{after.name}`")
        if before.icon != after.icon:
            changes.append("**Ikona:** zostala zmieniona")
        if before.owner != after.owner:
            changes.append(f"**Wlasciciel:** {before.owner.mention} -> {after.owner.mention}")
        if before.default_message_notifications != after.default_message_notifications:
            changes.append("**Powiadomienia:** zostaly zmienione")
        if before.verification_level != after.verification_level:
            changes.append(f"**Poziom weryfikacji:** `{before.verification_level}` -> `{after.verification_level}`")

        if not changes:
            return

        embed = discord.Embed(
            title="⚙️ Zmieniono ustawienia serwera",
            description="\n".join(changes),
            color=discord.Color.blue(),
        )
        embed.set_thumbnail(url=after.icon.url if after.icon else discord.Embed.Empty)
        await after.system_channel.send(embed=embed)


async def setup(bot):
    await bot.add_cog(OnGuildUpdateEvent(bot))
