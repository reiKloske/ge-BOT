import discord
from discord.ext import commands

enabled_commands = {
    'ban': True,
    'unban': True,
    'mute': True,
    'unmute': True,
    'kick': True,
    'warn': True,
    'hello': True,
    'ge': True,
    'findme': True
}


async def is_admin_or_role(ctx):
    admin_role = "Admin"
    if ctx.author.guild_permissions.administrator or discord.utils.get(ctx.author.roles, name=admin_role):
        return True
    else:
        await ctx.send('You do not have permission to execute this command')
        return False


def command_enabled(command_name):
    async def predicate(ctx):
        # Check if the command is in the dictionary
        if command_name not in enabled_commands:
            # If not in the dictionary, treat it as enabled
            return True

        # If the command is in the dictionary, return its value (True/False)
        if enabled_commands.get(command_name):
            return True
        else:
            await ctx.send(f"{command_name} is not enabled.")
            return False

    return commands.check(predicate)
