import discord
from discord.ext import commands


class MuteCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="mute")
    @commands.has_permissions(manage_roles=True)
    async def mute_cmd(self, ctx, member: discord.Member = None, *, reason=None):
        if member is None:
            return await ctx.send("Uzycie: `!mute <@uzytkownik> [powod]`")

        if member.top_role >= ctx.author.top_role:
            return await ctx.send("Nie mozesz wyciszyc kogos z wyzsza lub rowna role.")

        muted_role = discord.utils.get(ctx.guild.roles, name="Muted")

        if muted_role is None:
            muted_role = await ctx.guild.create_role(
                name="Muted",
                reason="Rola do wyciszania uzytkownikow",
            )
            for channel in ctx.guild.text_channels:
                await channel.set_permissions(
                    muted_role,
                    send_messages=False,
                    add_reactions=False,
                )
            for channel in ctx.guild.voice_channels:
                await channel.set_permissions(
                    muted_role,
                    speak=False,
                )

        if muted_role in member.roles:
            return await ctx.send(f"**{member}** jest juz wyciszony.")

        await member.add_roles(muted_role, reason=f"Wyciszony przez {ctx.author} | {reason or 'Brak powodu'}")

        embed = discord.Embed(
            title="🔇 Wyciszono",
            description=f"**{member}** zostal wyciszony.",
            color=discord.Color.greyple(),
        )
        embed.add_field(name="Powod", value=reason or "Brak powodu", inline=False)
        embed.set_footer(text=f"Wykonane przez {ctx.author}", icon_url=ctx.author.display_avatar.url)
        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(MuteCommand(bot))
