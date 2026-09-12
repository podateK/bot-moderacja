import discord
from discord.ext import commands


class OnMessageDeleteEvent(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if message.author.bot:
            return
        if message.guild is None:
            return
        if message.guild.system_channel is None:
            return

        if not message.content and not message.attachments:
            return

        embed = discord.Embed(
            title="🗑️ Usunieta wiadomosc",
            description=f"**Autor:** {message.author.mention}\n**Kanal:** {message.channel.mention}",
            color=discord.Color.orange(),
            timestamp=message.created_at,
        )

        if message.content:
            content = message.content[:1024]
            embed.add_field(name="Tresc", value=content, inline=False)

        if message.attachments:
            files = "\n".join(a.url for a in message.attachments)
            embed.add_field(name="Zalaczniki", value=files[:1024], inline=False)

        embed.set_thumbnail(url=message.author.display_avatar.url)
        await message.guild.system_channel.send(embed=embed)


async def setup(bot):
    await bot.add_cog(OnMessageDeleteEvent(bot))
