import discord, os, sys, pathlib, base64, json, asyncio
from discord.ext import commands


class Bot(object):

    def __init__(self, token="", command_prefix="gb."):
        botObj.command_prefix=command_prefix
        self.token = token
        self.botObj = commands.Bot(command_prefix=command_prefix, help_command=None)


    def setup(self):
        self.botObj.add_cog(cgs.eventCog.Events(self.botObj))

    def run(self):
        self.botObj.run(self.token)
