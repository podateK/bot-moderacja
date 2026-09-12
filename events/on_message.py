import discord
from discord.ext import commands
from collections import defaultdict
import time


class OnMessageEvent(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.message_history = defaultdict(list)
        self.SPAM_THRESHOLD = 5
        self.SPAM_WINDOW = 5

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        if message.content.lower() in ("siema", "witam"):
            try:
                await message.add_reaction("👋")
            except discord.Forbidden:
                pass

        now = time.time()
        user_messages = self.message_history[message.author.id]
        user_messages.append(now)

        self.message_history[message.author.id] = [
            t for t in user_messages if now - t < self.SPAM_WINDOW
        ]

        if len(self.message_history[message.author.id]) > self.SPAM_THRESHOLD:
            try:
                muted_role = discord.utils.get(message.guild.roles, name="Muted")
                if muted_role is None:
                    muted_role = await message.guild.create_role(
                        name="Muted", reason="Auto-mute za spam"
                    )
                    for ch in message.guild.text_channels:
                        await ch.set_permissions(muted_role, send_messages=False)

                await message.author.add_roles(muted_role, reason="Auto-mute za spam")

                embed = discord.Embed(
                    title="🔇 Auto-Mute za spam",
                    description=f"**{message.author}** zostal automatycznie wyciszony za spam.",
                    color=discord.Color.orange(),
                )
                await message.channel.send(embed=embed)

                self.message_history[message.author.id].clear()
            except discord.Forbidden:
                pass


async def setup(bot):
    await bot.add_cog(OnMessageEvent(bot))
