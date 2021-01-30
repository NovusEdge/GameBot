import discord, requests, json, asyncio
from discord.ext import commands
import commands as comm
import cogs as cgs

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
        await comm.help.help(ctx)

    @commands.command(aliases=["INVITE", "Invite"])
    async def invite(self, ctx):
        await comm.invite.invite(ctx)
