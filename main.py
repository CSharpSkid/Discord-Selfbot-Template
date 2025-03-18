import discord
from discord.ext import commands
import asyncio
import os




TOKEN = "Token Here"
prefix = "$"

csharpskid = commands.Bot(command_prefix=prefix, self_bot=True)

async def load_extensions():
    for filename in os.listdir("./commands"):
        if filename.endswith(".py") and filename != "__init__.py":
            try:
                await csharpskid.load_extension(f"commands.{filename[:-3]}")
                print(f"Loaded extension: {filename}")
            except Exception as e:
                print(f"Failed to load {filename}: {e}")

@csharpskid.event
async def on_ready():
    print(f"Bot logged in as {csharpskid.user}")

async def main():
    async with csharpskid:
        await load_extensions()
        await csharpskid.start(TOKEN)

if __name__ == "__main__":
    asyncio.run(main())
