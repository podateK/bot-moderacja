import discord
from discord.ext import commands


class LockCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="lock")
    @commands.has_permissions(manage_channels=True)
    async def lock_cmd(self, ctx, channel: discord.TextChannel = None):
        channel = channel or ctx.channel

        overwrite = channel.overwrites_for(ctx.guild.default_role)
        overwrite.send_messages = False
        await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)

        embed = discord.Embed(
            title="🔒 Kanal zablokowany",
            description=f"Kanal {channel.mention} zostal zablokowany.",
            color=discord.Color.red(),
        )
        embed.set_footer(text=f"Wykonane przez {ctx.author}", icon_url=ctx.author.display_avatar.url)
        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(LockCommand(bot))
