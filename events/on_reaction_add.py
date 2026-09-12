import discord
from discord.ext import commands


class OnReactionAddEvent(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        if user.bot:
            return
        if reaction.message.guild is None:
            return
        if reaction.message.guild.system_channel is None:
            return
        if reaction.message.channel == reaction.message.guild.system_channel:
            return

        embed = discord.Embed(
            title="😀 Dodano reakcje",
            description=f"**{user.mention}** dodal reakcje {reaction.emoji} do [wiadomosci]({reaction.message.jump_url})",
            color=discord.Color.purple(),
        )
        embed.add_field(name="Kanal", value=reaction.message.channel.mention, inline=True)
        embed.set_thumbnail(url=user.display_avatar.url)
        await reaction.message.guild.system_channel.send(embed=embed)


async def setup(bot):
    await bot.add_cog(OnReactionAddEvent(bot))
