import discord
from discord.ext import commands

class PingCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.message.delete()
        latency = round(self.bot.latency * 1000)
        await ctx.send(f"Pong! 🏓 `{latency}ms`", delete_after=5)

async def setup(bot):
    await bot.add_cog(PingCommand(bot))
