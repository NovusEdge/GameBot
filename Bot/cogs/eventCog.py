import discord, requests, json, asyncio
from discord.ext import commands
from cmds import help, invite
from Games import rps

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Ready!')
        print('Logged in as ---->', self.bot.user)
        print('ID:', self.bot.user.id)

    @commands.command(aliases=["h", "HELP", "Help"])
    async def help(self, ctx):
        await help.help(ctx)

    @commands.command(aliases=["INVITE", "Invite"])
    async def invite(self, ctx):
        await invite.invite(ctx)

    @commands.command(aliases=["RockPS", "RPS", "RockPaperSissors"])
    async def rps(self, ctx):
        pass

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content.startswith("Answer") or message.content.startswith("answer"):
            pass

        elif message.content in rps.moves:
            await self._check_answer(message)

        else:
            pass

    async def _check_answer(self, message):
        pass
