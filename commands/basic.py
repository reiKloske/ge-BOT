from discord.ext import commands
from time import sleep
from random import randint
from utils.checks import command_enabled

class Basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @command_enabled('hello')
    async def hello(self, ctx):
        await ctx.send("WASSAMM.. Now.. GE-")

    @commands.command()
    @command_enabled('ge')
    async def ge(self, ctx):
        await ctx.send("OUT!")

    @commands.command()
    @command_enabled('findme')
    async def findme(self, ctx):
        chance = randint(1, 5)
        await ctx.send("Looking for you..")
        sleep(2)
        if chance == 5:
            await ctx.send("GET OUT!")
        else:
            await ctx.send("Lucky.. GE will still find you")

    @commands.command(name="commands")
    async def help_command(self, ctx):
        help_message = (
            "# < Available commands >\n"
            "## Admin:\n"
            "- **ge.disable <command> - Disable the command\n"
            "- **ge.enable <command> - Enable the command\n"
            "## Moderation:\n"
            "- **ge.ban <user> [reason]** - Bans the user\n"
            "- **ge.unban <user>** - Unbans the user\n"
            "- **ge.mute <user>** - Mutes the user\n"
            "- **ge.unmute <user>** - Unmutes the user\n"
            "- **ge.kick <user> [reason]** - Kicks the user\n"
            "- **ge.warn <user> [reason]** - Warns the user\n"
            "## Basic:\n"
            "- **ge.hello**\n"
            "- **ge.ge** - OUT!\n"
            "- **ge.findme** - ge will try to get you\n"
            "- **ge.settings** - Displays enabled commands\n"
            "- **ge.command** - Displays this help message"

        )
        await ctx.send(help_message)


async def setup(bot):
    await bot.add_cog(Basic(bot))
