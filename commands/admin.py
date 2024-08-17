from discord.ext import commands
# Get dictionary 'enabled_commands' from checks.py file
from utils.checks import enabled_commands


class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Async functions to handle multiple tasks at once
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def disable(self, ctx, command_name: str):
        # Prevent disabling settings or help commands
        if command_name == 'settings' or command_name == 'help':
            await ctx.send(f"Command '**{command_name}**' cannot be disabled.")
            return  # If command name is found in the commands dictionary
        if command_name in enabled_commands:
            enabled_commands[command_name] = False
            await ctx.send(f"Command '**{command_name}**' has been disabled.")
            return  # Exit after disabling the command
        # If the command name was not found
        else:
            await ctx.send(f"No such command '**{command_name}**' found.")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def enable(self, ctx, command_name: str):
        if command_name in enabled_commands:
            enabled_commands[command_name] = True
            await ctx.send(f"Command '**{command_name}**' has been enabled.")
        else:
            await ctx.send(f"No such command '**{command_name}**' found.")


async def setup(bot):
    await bot.add_cog(Admin(bot))
