import discord
from discord.ext import commands
from utils.checks import is_admin_or_role
from utils.checks import command_enabled


class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    # Check if user executing the command has admin perms or has an admin role.
    @commands.check(is_admin_or_role)
    @command_enabled('ban')
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'{member.mention} has been banned for: {reason}')

    @commands.command()
    # Check if user executing the command has admin perms or has an admin role.
    @commands.check(is_admin_or_role)
    @command_enabled('unban')
    async def unban(self, ctx, *, username):
        # Unbans a user by their exact username.
        # Retrieve all bans asynchronously
        async for ban_entry in ctx.guild.bans():
            user = ban_entry.user

            if user.name == username:
                await ctx.guild.unban(user)
                await ctx.send(f'{user.mention} has been unbanned.')
                return

        await ctx.send(f'User {username} was not found in the banned list.')

    # Command that users can use
    @commands.command()
    # Check if user executing the command has admin perms or has an admin role.
    @commands.check(is_admin_or_role)
    @command_enabled('mute')
    async def mute(self, ctx, member: discord.Member):
        mute_role = discord.utils.get(ctx.guild.roles, name="Muted")
        if not mute_role:
            mute_role = await ctx.guild.create_role(name="Muted")
            for channel in ctx.guild.channels:
                await channel.set_permissions(mute_role, speak=False, send_messages=False)
        await member.add_roles(mute_role)
        await ctx.send(f'{member.mention} has been muted.')

    @commands.command()
    # Check if user executing the command has admin perms or has an admin role.
    @commands.check(is_admin_or_role)
    @command_enabled('unmute')
    async def unmute(self, ctx, member: discord.Member):
        mute_role = discord.utils.get(ctx.guild.roles, name="Muted")
        if mute_role in member.roles:
            await member.remove_roles(mute_role)
            await ctx.send(f'{member.mention} has been unmuted.')
        else:
            await ctx.send(f'{member.mention} has been unmuted.')

    @commands.command()
    # Check if user executing the command has admin perms or has an admin role.
    @commands.check(is_admin_or_role)
    @command_enabled('kick')
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'{member.mention} has been kicked for: {reason}')

    @commands.command()
    # Check if user executing the command has admin perms or has an admin role.
    @commands.check(is_admin_or_role)
    @command_enabled('warn')
    async def warn(self, ctx, member: discord.Member, *, reason=None):
        await ctx.send(f'{member.mention} has been warned for: {reason}')


async def setup(bot):
    await bot.add_cog(Moderation(bot))
