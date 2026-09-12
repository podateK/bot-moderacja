import discord
from discord.ext import commands


class UnlockCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="unlock")
    @commands.has_permissions(manage_channels=True)
    async def unlock_cmd(self, ctx, channel: discord.TextChannel = None):
        channel = channel or ctx.channel

        overwrite = channel.overwrites_for(ctx.guild.default_role)
        overwrite.send_messages = None
        await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)

        embed = discord.Embed(
            title="🔓 Kanal odblokowany",
            description=f"Kanal {channel.mention} zostal odblokowany.",
            color=discord.Color.green(),
        )
        embed.set_footer(text=f"Wykonane przez {ctx.author}", icon_url=ctx.author.display_avatar.url)
        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(UnlockCommand(bot))
