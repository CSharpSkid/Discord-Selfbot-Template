import discord
from discord.ext import commands
import asyncio
import os




TOKEN = "Token here"
prefix = "$"

csharpskid = commands.Bot(command_prefix=prefix, self_bot=True)

@csharpskid.event
async def on_ready():
    print(f"Selfbot logged in as {csharpskid.user}")


    for filename in os.listdir("./commands"):
        if filename.endswith(".py") and filename != "__init__.py":
            await csharpskid.load_extension(f"commands.{filename[:-3]}")

async def main():
    async with csharpskid:
        await load_extensions()
        await csharpskid.start(TOKEN)




if __name__ == "__main__":
    asyncio.run(main())
