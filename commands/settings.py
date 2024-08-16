from discord.ext import commands
from utils.checks import enabled_commands


class Settings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def settings(self, ctx):
        settings_message = "**Enabled Commands:**\n" + "\n".join([f"{cmd}: **{status}**" for cmd, status in enabled_commands.items()])
        await ctx.send(settings_message)


async def setup(bot):
    await bot.add_cog(Settings(bot))
