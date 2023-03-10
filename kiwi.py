import discord, json
from discord.ext import commands

kiwi = discord.Colour.from_rgb(0, 200, 118)
intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix = '!', intents = intents)

# logged in message
@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

# confess command
@client.command()
async def confess(ctx, *args):
    await ctx.message.delete()
    await ctx.send(" ".join(args))

# will fail if answer is not "kiwi" or "beta"
client.run(json.load(open("tokens.json"))[str(input("Select a client: ").lower())])

"""
TODO: Future tasks
* Change status periodically
* React when kiwi is sent
"""