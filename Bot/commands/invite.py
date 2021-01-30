import discord, json

async def help(ctx):
    with open("embeds/invite.json", "r") as invite_file:
        embedObj = discord.Embed.from_dict( json.load(invite_file)["embed"] )
    await ctx.send(embed=embedObj)
