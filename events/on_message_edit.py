import discord
from discord.ext import commands


class OnMessageEditEvent(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        if before.author.bot:
            return
        if before.guild is None:
            return
        if before.guild.system_channel is None:
            return
        if before.content == after.content:
            return

        embed = discord.Embed(
            title="✏️ Edytowana wiadomosc",
            description=f"**Autor:** {before.author.mention}\n**Kanal:** {before.channel.mention}\n[Skocz do wiadomosci]({after.jump_url})",
            color=discord.Color.blue(),
            timestamp=before.created_at,
        )
        if before.content:
            embed.add_field(name="Przed", value=before.content[:1024], inline=False)
        if after.content:
            embed.add_field(name="Po", value=after.content[:1024], inline=False)

        embed.set_thumbnail(url=before.author.display_avatar.url)
        await before.guild.system_channel.send(embed=embed)


async def setup(bot):
    await bot.add_cog(OnMessageEditEvent(bot))
